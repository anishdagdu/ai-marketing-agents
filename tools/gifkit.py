"""gifkit: shared renderer for the animated workflow GIFs in this repo.

Draws at 2x and scales down, so every line and letter is anti-aliased.
Gives you cards, curved connectors with flowing dots, a moving "token",
callouts, stamps and a caption bar, plus easing and a GIF writer that
keeps one shared palette so colours don't flicker between frames.

Needs Pillow. Fonts: Avenir Next on macOS, DejaVu Sans elsewhere.
"""
from __future__ import annotations

import math
import os
from dataclasses import dataclass, field

from PIL import Image, ImageDraw, ImageFilter, ImageFont

SS = 2  # supersampling factor

# ------------------------------------------------------------------ palette
BG = (246, 248, 252)
BG2 = (236, 240, 247)
CARD = (255, 255, 255)
CARD_HI = (250, 252, 255)
LINE = (203, 211, 225)
INK = (12, 20, 38)
MUTED = (45, 58, 82)
DIM = (88, 102, 128)
WHITE = (255, 255, 255)

BLUE = (37, 99, 235)
VIOLET = (124, 58, 237)
TEAL = (13, 148, 136)
GREEN = (22, 163, 74)
AMBER = (217, 119, 6)
RED = (220, 38, 38)
PINK = (219, 39, 119)
CYAN = (2, 132, 199)


def mix(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def alpha(c, a):
    return (*c[:3], int(255 * max(0, min(1, a))))


# ------------------------------------------------------------------ easing
def clamp(x, lo=0.0, hi=1.0):
    return max(lo, min(hi, x))


def ease_out(t):
    t = clamp(t)
    return 1 - (1 - t) ** 3


def ease_in_out(t):
    t = clamp(t)
    return 4 * t ** 3 if t < 0.5 else 1 - (-2 * t + 2) ** 3 / 2


def back_out(t):
    t = clamp(t)
    c1, c3 = 1.70158, 2.70158
    return 1 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2


def window(t, a, b):
    """0 before a, 1 after b, linear in between."""
    if b <= a:
        return 1.0 if t >= b else 0.0
    return clamp((t - a) / (b - a))


# ------------------------------------------------------------------ fonts
_FONT_CACHE: dict = {}
_AVENIR = "/System/Library/Fonts/Avenir Next.ttc"
_WEIGHT_INDEX = {"bold": 0, "demi": 2, "medium": 5, "regular": 7}


def font(size, weight="regular"):
    key = (size, weight)
    if key not in _FONT_CACHE:
        f = None
        if os.path.exists(_AVENIR):
            f = ImageFont.truetype(_AVENIR, size * SS, index=_WEIGHT_INDEX[weight])
        else:
            for p in (["DejaVuSans-Bold.ttf"] if weight in ("bold", "demi") else []) + ["DejaVuSans.ttf"]:
                try:
                    f = ImageFont.truetype(p, size * SS)
                    break
                except OSError:
                    pass
        _FONT_CACHE[key] = f or ImageFont.load_default()
    return _FONT_CACHE[key]


# ------------------------------------------------------------------ geometry
def bezier(p0, p1, p2, p3, n=48):
    pts = []
    for i in range(n + 1):
        t = i / n
        mt = 1 - t
        x = mt ** 3 * p0[0] + 3 * mt ** 2 * t * p1[0] + 3 * mt * t ** 2 * p2[0] + t ** 3 * p3[0]
        y = mt ** 3 * p0[1] + 3 * mt ** 2 * t * p1[1] + 3 * mt * t ** 2 * p2[1] + t ** 3 * p3[1]
        pts.append((x, y))
    return pts


def curve(a, b, axis="h", bend=0.5):
    """Smooth S-curve from a to b. axis 'h' leaves/enters horizontally, 'v' vertically."""
    if axis == "h":
        dx = (b[0] - a[0]) * bend
        return bezier(a, (a[0] + dx, a[1]), (b[0] - dx, b[1]), b)
    dy = (b[1] - a[1]) * bend
    return bezier(a, (a[0], a[1] + dy), (b[0], b[1] - dy), b)


def poly(*pts, n=24):
    """Straight segments through the points, resampled."""
    out = []
    for a, b in zip(pts, pts[1:]):
        for i in range(n):
            t = i / n
            out.append((a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t))
    out.append(pts[-1])
    return out


class Path:
    def __init__(self, pts):
        self.pts = pts
        self.cum = [0.0]
        for a, b in zip(pts, pts[1:]):
            self.cum.append(self.cum[-1] + math.dist(a, b))
        self.length = self.cum[-1] or 1.0

    def at(self, t):
        d = clamp(t) * self.length
        for i in range(1, len(self.cum)):
            if self.cum[i] >= d:
                seg = self.cum[i] - self.cum[i - 1] or 1
                u = (d - self.cum[i - 1]) / seg
                a, b = self.pts[i - 1], self.pts[i]
                return (a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u)
        return self.pts[-1]

    def upto(self, t):
        d = clamp(t) * self.length
        out = [self.pts[0]]
        for i in range(1, len(self.cum)):
            if self.cum[i] <= d:
                out.append(self.pts[i])
            else:
                out.append(self.at(t))
                break
        return out


def join(*paths):
    pts = []
    for p in paths:
        pts.extend(p.pts if isinstance(p, Path) else p)
    return Path(pts)


# ------------------------------------------------------------------ canvas
class Canvas:
    """One frame. All coordinates are in output pixels; scaled by SS internally."""

    def __init__(self, w, h, base=None):
        self.w, self.h = w, h
        self.img = base.copy() if base is not None else Image.new("RGBA", (w * SS, h * SS), BG + (255,))
        self.d = ImageDraw.Draw(self.img)

    # helpers ---------------------------------------------------------
    @staticmethod
    def s(v):
        return int(round(v * SS))

    def box(self, x0, y0, x1, y1):
        return [self.s(x0), self.s(y0), self.s(x1), self.s(y1)]

    def overlay(self):
        layer = Image.new("RGBA", self.img.size, (0, 0, 0, 0))
        return layer, ImageDraw.Draw(layer)

    def merge(self, layer):
        self.img.alpha_composite(layer)
        self.d = ImageDraw.Draw(self.img)

    # primitives ------------------------------------------------------
    def rect(self, x0, y0, x1, y1, r=12, fill=None, outline=None, width=1, a=1.0):
        if a >= 0.999:
            self.d.rounded_rectangle(self.box(x0, y0, x1, y1), self.s(r), fill=fill,
                                     outline=outline, width=self.s(width))
            return
        layer, d = self.overlay()
        d.rounded_rectangle(self.box(x0, y0, x1, y1), self.s(r),
                            fill=alpha(fill, a) if fill else None,
                            outline=alpha(outline, a) if outline else None, width=self.s(width))
        self.merge(layer)

    def glow(self, x0, y0, x1, y1, color, r=14, strength=0.6, spread=14):
        if strength <= 0.01:
            return
        layer, d = self.overlay()
        d.rounded_rectangle(self.box(x0 - 2, y0 - 2, x1 + 2, y1 + 2), self.s(r),
                            outline=alpha(color, strength), width=self.s(6))
        layer = layer.filter(ImageFilter.GaussianBlur(self.s(spread) / 2))
        self.merge(layer)

    def circle(self, cx, cy, r, fill=None, outline=None, width=1, a=1.0):
        bb = self.box(cx - r, cy - r, cx + r, cy + r)
        if a >= 0.999:
            self.d.ellipse(bb, fill=fill, outline=outline, width=self.s(width))
            return
        layer, d = self.overlay()
        d.ellipse(bb, fill=alpha(fill, a) if fill else None,
                  outline=alpha(outline, a) if outline else None, width=self.s(width))
        self.merge(layer)

    def soft_dot(self, cx, cy, r, color, a=1.0):
        layer, d = self.overlay()
        d.ellipse(self.box(cx - r * 2.4, cy - r * 2.4, cx + r * 2.4, cy + r * 2.4), fill=alpha(color, 0.35 * a))
        layer = layer.filter(ImageFilter.GaussianBlur(self.s(r)))
        d = ImageDraw.Draw(layer)
        d.ellipse(self.box(cx - r, cy - r, cx + r, cy + r), fill=alpha(mix(color, (255, 255, 255), 0.35), a))
        self.merge(layer)

    def line(self, pts, color, width=2, a=1.0, dash=None):
        sp = [(self.s(x), self.s(y)) for x, y in pts]
        if len(sp) < 2:
            return
        if a >= 0.999 and not dash:
            self.d.line(sp, fill=color, width=self.s(width), joint="curve")
            return
        layer, d = self.overlay()
        if dash:
            on, off = dash
            acc, draw_on, seg = 0.0, True, [sp[0]]
            for p, q in zip(sp, sp[1:]):
                acc += math.dist(p, q)
                seg.append(q)
                if acc >= (on if draw_on else off) * SS:
                    if draw_on:
                        d.line(seg, fill=alpha(color, a), width=self.s(width))
                    draw_on, acc, seg = not draw_on, 0.0, [q]
            if draw_on and len(seg) > 1:
                d.line(seg, fill=alpha(color, a), width=self.s(width))
        else:
            d.line(sp, fill=alpha(color, a), width=self.s(width), joint="curve")
        self.merge(layer)

    def arrowhead(self, tip, prev, color, size=8, a=1.0):
        ang = math.atan2(tip[1] - prev[1], tip[0] - prev[0])
        p1 = (tip[0] - size * math.cos(ang - 0.45), tip[1] - size * math.sin(ang - 0.45))
        p2 = (tip[0] - size * math.cos(ang + 0.45), tip[1] - size * math.sin(ang + 0.45))
        pts = [(self.s(x), self.s(y)) for x, y in (tip, p1, p2)]
        if a >= 0.999:
            self.d.polygon(pts, fill=color)
        else:
            layer, d = self.overlay()
            d.polygon(pts, fill=alpha(color, a))
            self.merge(layer)

    def text(self, x, y, s, size=14, weight="regular", color=INK, anchor="la", a=1.0):
        if "→" in s:  # many fonts lack the arrow glyph, so draw it as a vector
            return self._text_arrows(x, y, s, size, weight, color, anchor, a)
        f = font(size, weight)
        if a >= 0.999:
            self.d.text((self.s(x), self.s(y)), s, font=f, fill=color, anchor=anchor)
            return
        layer, d = self.overlay()
        d.text((self.s(x), self.s(y)), s, font=f, fill=alpha(color, a), anchor=anchor)
        self.merge(layer)

    def _text_arrows(self, x, y, s, size, weight, color, anchor, a):
        parts = s.split("→")
        aw = size * 1.15
        total = self.text_w(s, size, weight)
        h, v = anchor[0], anchor[1]
        cx = x - (total / 2 if h == "m" else total if h == "r" else 0)
        mid = {"m": y, "a": y + size * 0.62, "t": y + size * 0.62, "s": y - size * 0.33}.get(v, y)
        for i, p in enumerate(parts):
            if p:
                self.text(cx, y, p, size, weight, color, anchor="l" + v, a=a)
                cx += self.text_w(p, size, weight)
            if i < len(parts) - 1:
                x0, x1 = cx + size * 0.18, cx + aw - size * 0.18
                self.line([(x0, mid), (x1, mid)], color, max(1.1, size / 11), a)
                self.line([(x1 - size * 0.3, mid - size * 0.26), (x1, mid), (x1 - size * 0.3, mid + size * 0.26)],
                          color, max(1.1, size / 11), a)
                cx += aw

    def text_w(self, s, size=14, weight="regular"):
        n = s.count("→")
        return font(size, weight).getlength(s.replace("→", "")) / SS + n * size * 1.15

    def pill(self, x, y, s, color, size=11, weight="demi", a=1.0, solid=False, pad=8, h=None):
        w = self.text_w(s, size, weight) + pad * 2
        h = h or size + 10
        if solid:
            self.rect(x, y, x + w, y + h, r=h / 2, fill=color, a=a)
            self.text(x + w / 2, y + h / 2 + 0.5, s, size, weight, WHITE, anchor="mm", a=a)
        else:
            self.rect(x, y, x + w, y + h, r=h / 2, fill=mix(WHITE, color, 0.12), outline=mix(WHITE, color, 0.5), a=a)
            self.text(x + w / 2, y + h / 2 + 0.5, s, size, weight, mix(color, INK, 0.3), anchor="mm", a=a)
        return w

    def finish(self):
        return self.img.resize((self.w, self.h), Image.LANCZOS).convert("RGB")


# ------------------------------------------------------------------ icons
def icon(c: Canvas, kind, cx, cy, color, size=18, a=1.0):
    """Tiny line icons drawn from primitives (no image files needed)."""
    s = size / 18
    w = max(1.6, 2 * s)
    L = lambda pts: c.line([(cx + x * s, cy + y * s) for x, y in pts], color, w, a)
    if kind == "db":
        for yy in (-6, 0, 6):
            c.line([(cx + x * s, cy + (yy + 2.5 * math.sin(math.pi * (x + 8) / 16)) * s) for x in range(-8, 9)], color, w, a)
        L([(-8, -6), (-8, 6)]); L([(8, -6), (8, 6)])
    elif kind == "user":
        c.circle(cx, cy - 4 * s, 4 * s, outline=color, width=w, a=a)
        c.line([(cx + 9 * s * math.cos(t), cy + 9 * s + 9 * s * math.sin(t) - 1 * s)
                for t in [math.pi + i * math.pi / 16 for i in range(17)]], color, w, a)
    elif kind == "gauge":
        c.line([(cx + 9 * s * math.cos(t), cy + 4 * s + 9 * s * math.sin(t))
                for t in [math.pi + i * math.pi / 20 for i in range(21)]], color, w, a)
        L([(0, 4), (5, -3)])
    elif kind == "route":
        c.circle(cx - 7 * s, cy + 6 * s, 2.5 * s, fill=color, a=a)
        c.circle(cx + 7 * s, cy - 6 * s, 2.5 * s, fill=color, a=a)
        c.line(curve((cx - 7 * s, cy + 6 * s), (cx + 7 * s, cy - 6 * s), "h", 0.9), color, w, a)
    elif kind == "bolt":
        L([(2, -9), (-5, 1), (1, 1), (-2, 9), (6, -2), (0, -2), (2, -9)])
    elif kind == "shield":
        L([(0, -9), (8, -6), (7, 3), (0, 9), (-7, 3), (-8, -6), (0, -9)])
        L([(-3, 0), (-1, 3), (4, -3)])
    elif kind == "filter":
        L([(-8, -7), (8, -7), (2, 1), (2, 8), (-2, 6), (-2, 1), (-8, -7)])
    elif kind == "spark":
        L([(0, -9), (0, 9)]); L([(-9, 0), (9, 0)]); L([(-5, -5), (5, 5)]); L([(-5, 5), (5, -5)])
    elif kind == "chart":
        L([(-8, 8), (-8, -8)]); L([(-8, 8), (8, 8)])
        L([(-5, 4), (-1, -1), (2, 2), (7, -6)])
    elif kind == "flask":
        L([(-3, -8), (3, -8)]); L([(-2, -8), (-2, -2), (-8, 8), (8, 8), (2, -2), (2, -8)])
    elif kind == "cal":
        c.rect(cx - 8 * s, cy - 7 * s, cx + 8 * s, cy + 8 * s, r=2 * s, outline=color, width=w, a=a)
        L([(-8, -2), (8, -2)]); L([(-4, -10), (-4, -5)]); L([(4, -10), (4, -5)])
    elif kind == "send":
        L([(-8, 0), (8, -7), (2, 8), (0, 1), (-8, 0)]); L([(0, 1), (8, -7)])
    elif kind == "check":
        L([(-6, 0), (-2, 5), (7, -6)])
    elif kind == "x":
        L([(-6, -6), (6, 6)]); L([(-6, 6), (6, -6)])
    elif kind == "heart":
        c.line([(cx + s * 8 * math.sin(t) ** 3,
                 cy - s * (6.5 * math.cos(t) - 2.5 * math.cos(2 * t) - math.cos(3 * t) - 1))
                for t in [i * 2 * math.pi / 40 for i in range(41)]], color, w, a)
    elif kind == "clock":
        c.circle(cx, cy, 8 * s, outline=color, width=w, a=a)
        L([(0, 0), (0, -5)]); L([(0, 0), (4, 2)])
    elif kind == "tag":
        L([(-8, -2), (-2, -8), (8, -8), (8, 2), (2, 8), (-8, -2)])
        c.circle(cx + 4 * s, cy - 4 * s, 1.6 * s, fill=color, a=a)
    elif kind == "mail":
        c.rect(cx - 9 * s, cy - 6 * s, cx + 9 * s, cy + 6 * s, r=2 * s, outline=color, width=w, a=a)
        L([(-9, -5), (0, 2), (9, -5)])
    elif kind == "video":
        c.rect(cx - 9 * s, cy - 6 * s, cx + 4 * s, cy + 6 * s, r=2 * s, outline=color, width=w, a=a)
        L([(4, -2), (9, -5), (9, 5), (4, 2)])
    elif kind == "search":
        c.circle(cx - 2 * s, cy - 2 * s, 6 * s, outline=color, width=w, a=a)
        L([(3, 3), (8, 8)])
    elif kind == "speed":
        c.line([(cx + 9 * s * math.cos(t), cy + 3 * s + 9 * s * math.sin(t))
                for t in [math.pi * 0.85 + i * math.pi * 1.3 / 24 for i in range(25)]], color, w, a)
        L([(0, 3), (6, -3)])
    elif kind == "doc":
        L([(-6, -9), (3, -9), (7, -5), (7, 9), (-6, 9), (-6, -9)])
        L([(-3, -2), (4, -2)]); L([(-3, 2), (4, 2)]); L([(-3, 6), (2, 6)])


# ------------------------------------------------------------------ components
@dataclass
class Node:
    key: str
    x0: float
    y0: float
    x1: float
    y1: float
    title: str
    sub: str = ""
    color: tuple = BLUE
    icon: str = ""
    num: str = ""
    tag: str = ""
    lines: list = field(default_factory=list)

    @property
    def cx(self):
        return (self.x0 + self.x1) / 2

    @property
    def cy(self):
        return (self.y0 + self.y1) / 2

    def L(self, dy=0):
        return (self.x0, self.cy + dy)

    def R(self, dy=0):
        return (self.x1, self.cy + dy)

    def T(self, dx=0):
        return (self.cx + dx, self.y0)

    def B(self, dx=0):
        return (self.cx + dx, self.y1)


def draw_node(c: Canvas, n: Node, appear=1.0, active=0.0, dim=0.0):
    """Card with accent bar, icon chip, number, title, subtitle and optional bullet lines."""
    if appear <= 0.01:
        return
    e = ease_out(appear)
    dy = (1 - e) * 14
    a = e * (1 - 0.55 * dim)
    x0, y0, x1, y1 = n.x0, n.y0 + dy, n.x1, n.y1 + dy
    if active > 0.01:
        c.glow(x0, y0, x1, y1, n.color, strength=0.85 * active, spread=16)
    fill = mix(CARD, mix(WHITE, n.color, 0.07), active)
    outline = mix(LINE, n.color, 0.25 + 0.75 * active)
    c.rect(x0 + 1, y0 + 3, x1 + 1, y1 + 4, r=14, fill=(15, 23, 42), a=a * 0.06)  # soft shadow
    c.rect(x0, y0, x1, y1, r=14, fill=fill, outline=outline, width=1.4 + 0.8 * active, a=a)
    c.rect(x0 + 1, y0 + 1, x0 + 5, y1 - 1, r=2, fill=n.color, a=a)  # accent bar
    ix = x0 + 30
    iy = y0 + 30
    c.circle(ix, iy, 16, fill=mix(WHITE, n.color, 0.14), outline=mix(WHITE, n.color, 0.45), width=1.2, a=a)
    if n.icon:
        icon(c, n.icon, ix, iy, n.color, size=15, a=a)
    tx = ix + 24
    room = x1 - tx - 10 - ((c.text_w(n.tag, 10.5, "bold") + 26) if n.tag else 0)
    tsize = 16.5
    while tsize > 12 and c.text_w(n.title, tsize, "bold") > room:
        tsize -= 0.5
    if n.num:
        c.text(tx, y0 + 11, n.num, 10.5, "bold", n.color, a=a)
        c.text(tx, y0 + 26 + (16.5 - tsize) * 0.6, n.title, tsize, "bold", INK, a=a)
    else:
        c.text(tx, iy, n.title, tsize, "bold", INK, anchor="lm", a=a)
    yy = y0 + 56
    if n.sub:
        c.text(x0 + 16, yy, n.sub, 13, "demi", MUTED, a=a)
        yy += 20
    for ln in n.lines:
        c.circle(x0 + 21, yy + 8, 2.6, fill=n.color, a=a)
        c.text(x0 + 30, yy, ln, 12.5, "medium", MUTED, a=a)
        yy += 17.5
    if n.tag:
        tw = c.text_w(n.tag, 10.5, "bold") + 16
        c.pill(x1 - tw - 10, y0 + 11, n.tag, n.color, size=10.5, weight="bold", a=a, solid=True)


def draw_link(c: Canvas, path: Path, color, grow=1.0, a=1.0, flow_t=None, dots=3, arrow=True, dash=None):
    """Connector that draws itself in (grow) and carries flowing dots (flow_t in seconds)."""
    if grow <= 0.01:
        return
    pts = path.upto(grow)
    c.line(pts, mix(BG, color, 0.6), 2.2, a, dash=dash)
    if arrow and grow >= 0.98 and len(path.pts) > 2:
        c.arrowhead(path.pts[-1], path.pts[-3], color, 9, a)
    if flow_t is not None and grow >= 0.98:
        speed = 120 / path.length  # px per second -> path units
        for k in range(dots):
            u = (flow_t * speed + k / dots) % 1.0
            x, y = path.at(u)
            fade = math.sin(math.pi * u)
            c.circle(x, y, 3.2, fill=color, a=a * (0.35 + 0.65 * fade))


def draw_token(c: Canvas, pos, color, label="P", a=1.0, ring=0.0):
    x, y = pos
    c.soft_dot(x, y, 9, color, a)
    c.circle(x, y, 12, fill=color, outline=WHITE, width=2.5, a=a)
    c.text(x, y + 0.5, label, 11.5, "bold", WHITE, anchor="mm", a=a)
    if ring > 0:
        r = 11 + 18 * ring
        c.circle(x, y, r, outline=color, width=2, a=a * (1 - ring))


def callout(c: Canvas, x, y, title, body, color, appear=1.0, w=None, side="top"):
    """Speech-bubble card pointing at (x, y)."""
    if appear <= 0.01:
        return
    e = back_out(appear)
    a = clamp(appear * 1.6)
    w = w or max(c.text_w(title, 14, "bold"), c.text_w(body, 13, "demi")) + 32
    h = 58
    bx = x - w / 2
    by = (y - h - 16 - (1 - e) * 10) if side == "top" else (y + 16 + (1 - e) * 10)
    c.rect(bx + 1, by + 3, bx + w + 1, by + h + 4, r=10, fill=(15, 23, 42), a=a * 0.08)
    c.rect(bx, by, bx + w, by + h, r=10, fill=WHITE, outline=color, width=2, a=a)
    c.rect(bx, by, bx + 5, by + h, r=2, fill=color, a=a)
    tip = [(x - 7, by + h), (x + 7, by + h), (x, by + h + 8)] if side == "top" else \
          [(x - 7, by), (x + 7, by), (x, by - 8)]
    layer, d = c.overlay()
    d.polygon([(c.s(px), c.s(py)) for px, py in tip], fill=alpha(color, a))
    c.merge(layer)
    c.text(bx + 16, by + 10, title, 14, "bold", mix(color, INK, 0.25), a=a)
    c.text(bx + 16, by + 32, body, 13, "demi", INK, a=a)


def stamp(c: Canvas, cx, cy, text, color, appear=1.0, angle=-12):
    """Rubber-stamp effect (e.g. VETO)."""
    if appear <= 0.01:
        return
    sc = 1.6 - 0.6 * ease_out(appear)
    a = clamp(appear * 2)
    f = font(int(22 * sc), "bold")
    tw = f.getlength(text) / SS
    w, h = tw + 30 * sc, 40 * sc
    layer = Image.new("RGBA", (c.s(w + 20), c.s(h + 20)), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.rounded_rectangle([c.s(10), c.s(10), c.s(10 + w), c.s(10 + h)], c.s(6), fill=alpha(WHITE, a * 0.92),
                        outline=alpha(color, a), width=c.s(3))
    d.text((c.s(10 + w / 2), c.s(10 + h / 2)), text, font=f, fill=alpha(color, a), anchor="mm")
    layer = layer.rotate(angle, resample=Image.BICUBIC, expand=True)
    c.img.alpha_composite(layer, (c.s(cx) - layer.width // 2, c.s(cy) - layer.height // 2))
    c.d = ImageDraw.Draw(c.img)


def caption_bar(c: Canvas, y, label, text, color, appear=1.0, progress=None):
    """Narration bar at the bottom: coloured label pill + sentence + optional progress line."""
    if appear <= 0.01:
        return
    a = ease_out(appear)
    x0, x1 = 40, c.w - 40
    c.rect(x0, y, x1, y + 44, r=12, fill=WHITE, outline=LINE, width=1.2, a=a)
    pw = c.pill(x0 + 12, y + 10, label, color, size=12, weight="bold", a=a, solid=True, h=24)
    c.text(x0 + 26 + pw, y + 22, text, 16, "demi", INK, anchor="lm", a=a)
    if progress is not None:
        c.rect(x0 + 12, y + 36, x0 + 12 + (x1 - x0 - 24) * clamp(progress), y + 38, r=1, fill=color, a=a)


def header(c: Canvas, kicker, title, sub, color, right=None):
    c.pill(40, 24, kicker, color, size=12, weight="bold", solid=True, h=24)
    c.text(40, 54, title, 30, "bold", INK)
    c.text(40, 94, sub, 15, "demi", MUTED)
    if right:
        x = c.w - 40
        for s, col in reversed(right):
            w = c.text_w(s, 12.5, "bold") + 16
            x -= w
            c.pill(x, 28, s, col, size=12.5, weight="bold", h=26)
            x -= 8


def background(w, h, accent=BLUE):
    """Static backdrop: vertical gradient, dot grid and a soft accent glow."""
    img = Image.new("RGBA", (w * SS, h * SS), BG + (255,))
    d = ImageDraw.Draw(img)
    for y in range(0, h * SS, 4):
        d.rectangle([0, y, w * SS, y + 4], fill=mix(BG, BG2, y / (h * SS)) + (255,))
    step = 24 * SS
    for y in range(step, h * SS, step):
        for x in range(step, w * SS, step):
            d.ellipse([x - SS, y - SS, x + SS, y + SS], fill=(215, 222, 234, 255))
    glow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([int(w * SS * 0.55), -int(h * SS * 0.5), int(w * SS * 1.2), int(h * SS * 0.45)], fill=alpha(accent, 0.07))
    glow = glow.filter(ImageFilter.GaussianBlur(80 * SS))
    img.alpha_composite(glow)
    return img


def section_label(c: Canvas, x, y, text, color=DIM, a=1.0):
    c.text(x, y, text.upper(), 12, "bold", color, a=a)


# ------------------------------------------------------------------ story timeline
@dataclass
class Step:
    """Token travels along `link`, then dwells on `node` while a callout shows."""
    link: str
    node: str
    travel: float = 0.4
    dwell: float = 0.9
    title: str = ""
    body: str = ""
    color: tuple = BLUE
    side: str = "top"
    token: tuple = None          # token colour (defaults to scenario colour)
    label: str = None            # token letter
    extra: object = None         # fn(canvas, u) drawn during dwell, u = 0..1
    callout_xy: tuple = None     # override callout anchor


@dataclass
class Scenario:
    name: str
    caption: str
    color: tuple
    steps: list
    label: str = "P"


class Story:
    """Plays: build-up -> scenarios -> outro, and returns frames + durations."""

    def __init__(self, w, h, links, fps=12.5):
        self.w, self.h, self.links, self.fps = w, h, links, fps

    def timeline(self, scenarios, gap=0.35):
        out, t = [], 0.0
        for sc in scenarios:
            for st in sc.steps:
                out.append((sc, st, t, t + st.travel, t + st.travel + st.dwell))
                t += st.travel + st.dwell
            t += gap
        return out, t

    @staticmethod
    def state_at(tl, t):
        for sc, st, t0, t1, t2 in tl:
            if t0 <= t < t2:
                if t < t1:
                    return dict(sc=sc, st=st, phase="travel", u=ease_in_out((t - t0) / (t1 - t0)))
                return dict(sc=sc, st=st, phase="dwell", u=(t - t1) / max(t2 - t1, 1e-6), age=t - t1)
        return None


def chip(c: Canvas, x0, y0, x1, y1, label, ic, color, appear=1.0, active=0.0, size=13, status=None):
    """Small single-line card (data source, output, sub-agent). status: colour dot on the right."""
    if appear <= 0.01:
        return
    e = ease_out(appear)
    dy = (1 - e) * 10
    y0, y1 = y0 + dy, y1 + dy
    h = y1 - y0
    if active > 0.01:
        c.glow(x0, y0, x1, y1, color, strength=0.8 * active, spread=12)
    c.rect(x0 + 1, y0 + 2, x1 + 1, y1 + 3, r=10, fill=(15, 23, 42), a=e * 0.05)
    c.rect(x0, y0, x1, y1, r=10, fill=mix(CARD, mix(WHITE, color, 0.08), active),
           outline=mix(LINE, color, 0.3 + 0.7 * active), width=1.4, a=e)
    r = min(13, h / 2 - 6)
    tx = x0 + 14
    if ic:
        c.circle(x0 + 8 + r, (y0 + y1) / 2, r, fill=mix(WHITE, color, 0.14), a=e)
        icon(c, ic, x0 + 8 + r, (y0 + y1) / 2, color, size=r * 0.95, a=e)
        tx = x0 + 16 + 2 * r
    c.text(tx, (y0 + y1) / 2, label, size, "demi", INK, anchor="lm", a=e)
    if status is not None:
        sc, amt = status
        if amt > 0.01:
            c.circle(x1 - 14, (y0 + y1) / 2, 6 * back_out(amt), fill=sc)


def band(c: Canvas, x0, y0, x1, y1, label, color, appear=1.0):
    """Tinted group box with an uppercase label."""
    if appear <= 0.01:
        return
    a = ease_out(appear)
    c.rect(x0, y0, x1, y1, r=16, fill=mix(BG, color, 0.06), outline=mix(BG, color, 0.45), width=1.2, a=a)
    if label:
        section_label(c, x0 + 16, y0 + 8, label, color, a=a)


def run_scene(*, out, accent, kicker, title, sub, right, nodes, links, appear, scenarios,
              build_caption, outro_caption, build_end=3.0, sections=(), under=None, over=None,
              link_ends=None, W=1280, H=720, fps=12.5, outro=1.8, caption_y=650, dash_links=()):
    """Generic player: build-up (cards + connectors appear), scenarios (token + callouts), outro.

    links: {name: (Path, colour)}; name 'a>b' means it connects appear-keys a and b.
    under/over: fn(canvas, t, state) for scene-specific drawing below/above the cards.
    """
    import sys

    def ends(name):
        if link_ends and name in link_ends:
            return link_ends[name]
        return tuple(name.split(">")[:2])

    def lstart(name):
        a, b = ends(name)
        return max(appear.get(a, 0), appear.get(b, 0)) + 0.15

    tl, story_len = Story(W, H, links, fps).timeline(scenarios)
    t0, t1 = build_end, build_end + story_len
    end_t = t1 + outro

    base = background(W, H, accent)
    hc = Canvas(W, H, base)
    header(hc, kicker, title, sub, accent, right=right)
    base = hc.img

    def frame(t):
        c = Canvas(W, H, base)
        st = Story.state_at(tl, t - t0) if t0 <= t < t1 else None
        flow_all = not (t0 <= t < t1)
        cur = st["st"].link if st else None
        act = st["st"].node if st and st["phase"] == "dwell" else None
        amt = ease_out(min(1, st.get("age", 0) / 0.25)) if act else 0.0
        state = dict(st=st, act=act, amt=amt)
        for name, (path, col) in links.items():
            g = ease_out(window(t, lstart(name), lstart(name) + 0.45))
            draw_link(c, path, col, grow=g, flow_t=t if (flow_all or name == cur) else None,
                      dash=(6, 5) if name in dash_links else None)
        for x, y, lab, key in sections:
            section_label(c, x, y, lab, a=window(t, appear[key] - 0.1, appear[key] + 0.3))
        if under:
            under(c, t, state)
        for k, n in nodes.items():
            draw_node(c, n, appear=window(t, appear[k], appear[k] + 0.45), active=amt if act == k else 0.0)
        if over:
            over(c, t, state)
        if st:
            s, sc = st["st"], st["sc"]
            if st["phase"] == "travel" and s.link:
                draw_token(c, links[s.link][0].at(st["u"]), s.token or sc.color, s.label if s.label is not None else sc.label)
            elif st["phase"] == "dwell":
                if s.extra:
                    s.extra(c, st["u"])
                if s.title:
                    n = nodes.get(s.node)
                    ax, ay = s.callout_xy or ((n.cx, n.y0 if s.side == "top" else n.y1) if n else (W / 2, H / 2))
                    callout(c, ax, ay, s.title, s.body, s.color, appear=window(st["age"], 0.05, 0.35), side=s.side)
            caption_bar(c, caption_y, sc.name.upper(), sc.caption, sc.color)
        elif t < t0:
            caption_bar(c, caption_y, *build_caption, appear=window(t, build_end - 0.7, build_end - 0.3))
        else:
            caption_bar(c, caption_y, *outro_caption)
        return c.finish()

    if len(sys.argv) > 2 and sys.argv[1] == "--preview":  # --preview DIR t1 t2 ...
        for ts in sys.argv[3:]:
            frame(float(ts)).save(os.path.join(sys.argv[2], f"p_{ts}.png"))
        for sc, s, a, b, c2 in tl:
            print(f"{sc.name:11} {s.link or '-':10} {a + t0:6.2f}-{c2 + t0:6.2f}  {s.title}")
        return
    frames, durs, t = [], [], 0.0
    while t < end_t:
        frames.append(frame(t))
        durs.append(int(round(1000 / fps)))
        t += 1 / fps
    durs[-1] = 3200
    size = save_gif(frames, durs, out)
    print(f"{len(frames)} frames, {size / 1e6:.2f} MB -> {os.path.normpath(out)}")


# ------------------------------------------------------------------ writer
def save_gif(frames, durations, path, colors=200):
    """Shared palette across all frames keeps colours stable and the file small."""
    sample_idx = sorted(set([0, len(frames) // 4, len(frames) // 2, 3 * len(frames) // 4, len(frames) - 1]))
    strip = Image.new("RGB", (frames[0].width, frames[0].height * len(sample_idx)))
    for i, k in enumerate(sample_idx):
        strip.paste(frames[k], (0, i * frames[0].height))
    pal = strip.quantize(colors=colors, method=Image.MEDIANCUT)
    q = [f.quantize(palette=pal, dither=Image.Dither.NONE) for f in frames]
    q[0].save(path, save_all=True, append_images=q[1:], duration=durations, loop=0,
              optimize=True, disposal=1)
    return os.path.getsize(path)
