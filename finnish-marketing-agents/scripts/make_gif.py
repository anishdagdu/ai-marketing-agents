#!/usr/bin/env python3
"""Render docs/workflow.gif — animated overview of the Finnish marketing agents.

Drawn at 2x and scaled down so text stays crisp. Run: python3 scripts/make_gif.py
"""
import re
from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 900          # output size
S = 2                     # supersampling factor
AVENIR = "/System/Library/Fonts/Avenir Next.ttc"
SF = "/System/Library/Fonts/SFNS.ttf"
SYMS = "→↔↻"

_cache = {}


def font(style, size):
    key = (style, size)
    if key not in _cache:
        f = None
        for i in range(12):
            try:
                cand = ImageFont.truetype(AVENIR, size * S, index=i)
            except OSError:
                break
            if cand.getname()[1] == style:
                f = cand
                break
        _cache[key] = f or ImageFont.truetype(AVENIR, size * S)
    return _cache[key]


def sym_font(size_px):
    key = ("sf", size_px)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(SF, size_px)
    return _cache[key]


def parts(t):
    return [p for p in re.split("([" + SYMS + "])", t) if p]


def tlen(d, t, f):
    return sum(d.textlength(p, font=sym_font(f.size) if p in SYMS else f) for p in parts(t))


def text(d, x, y, t, f, fill, anchor="l"):
    """Draw text at (x, y) in 1x coords; arrows drawn with SF (Avenir lacks them)."""
    x, y = x * S, y * S
    w = tlen(d, t, f)
    if anchor == "m":
        x -= w / 2
    elif anchor == "r":
        x -= w
    for p in parts(t):
        ff = sym_font(f.size) if p in SYMS else f
        d.text((x, y), p, font=ff, fill=fill)
        x += d.textlength(p, font=ff)
    return w / S


def rrect(d, box, r, **kw):
    d.rounded_rectangle([v * S for v in box], r * S, **{k: (v * S if k == "width" else v) for k, v in kw.items()})


# ---- palette -------------------------------------------------------------
BG = (244, 246, 250)
DOT = (220, 225, 233)
INK = (11, 18, 36)
BODY = (45, 55, 72)
LINE = (148, 158, 175)
GREEN = (22, 163, 74)
WHITE = (255, 255, 255)

GROUPS = {
    "orch": dict(name="Orchestrator", main=(55, 65, 81), soft=(229, 231, 235), dark=(31, 41, 55)),
    "cal": dict(name="Calendar agent", main=(13, 148, 110), soft=(209, 245, 230), dark=(6, 95, 70)),
    "ads": dict(name="Ads copywriter", main=(91, 72, 214), soft=(229, 225, 255), dark=(60, 45, 160)),
    "you": dict(name="You", main=(217, 119, 6), soft=(254, 236, 204), dark=(146, 64, 14)),
}

STAGES = [
    ("Brief & routing", ["Goals, competitors,", "channels, budget"], [], "orch", None),
    ("Research", ["Your website +", "competitor sentiment"], ["Reviews", "Meta Ad Library"], "cal", "Gate 1"),
    ("Strategy", ["Content pillars,", "organic vs paid split"], [], "cal", "Gate 2"),
    ("Content calendar", ["Dated posts with", "Finnish + English copy"], [], "cal", "Gate 3"),
    ("Ad copy", ["Every campaign type"], ["Google", "Meta", "LinkedIn", "Snapchat"], "ads", None),
    ("Translate & QA", ["fi ↔ en, character", "limits, compliance"], [], "ads", None),
    ("You approve", ["Nothing is published", "without your OK"], [], "you", "Gate 4"),
    ("Measure", ["Winners → new briefs,", "every month"], [], "orch", None),
]

CW, CH, GAP = 350, 258, 33
X0 = (W - (4 * CW + 3 * GAP)) // 2
ROW_Y = [212, 528]


def pos(i):
    r, c = divmod(i, 4)
    return X0 + c * (CW + GAP), ROW_Y[r]


def mix(c, a, bg=BG):
    return tuple(int(bg[k] + (c[k] - bg[k]) * a) for k in range(3))


# ---- static background + header (rendered once) ---------------------------
def header():
    im = Image.new("RGB", (W * S, H * S), BG)
    d = ImageDraw.Draw(im)
    for x in range(18, W, 30):
        for y in range(18, H, 30):
            d.ellipse([x * S, y * S, (x + 3) * S, (y + 3) * S], fill=DOT)
    # badge
    f = font("Bold", 17)
    w = tlen(d, "FINNISH MARKETING AGENTS", f) / S
    rrect(d, (48, 34, 48 + w + 28, 66), 16, fill=GREEN)
    text(d, 62, 37, "FINNISH MARKETING AGENTS", f, WHITE)
    text(d, 46, 74, "An AI team for Finnish ads & content", font("Bold", 50), INK)
    text(d, 48, 146, "Orchestrator → research → strategy → calendar → ad copy → translate & QA → measure",
         font("Demi Bold", 22), BODY)
    # pills
    pills = [("3 agents", GROUPS["you"]), ("fi ↔ en", GROUPS["cal"]), ("You approve", GROUPS["ads"])]
    x = W - 48
    pf = font("Demi Bold", 18)
    for label, g in reversed(pills):
        pw = tlen(d, label, pf) / S + 32
        x -= pw
        rrect(d, (x, 38, x + pw, 74), 18, fill=g["soft"], outline=g["main"], width=2)
        text(d, x + 16, 43, label, pf, g["dark"])
        x -= 12
    return im


# ---- cards ----------------------------------------------------------------
def card(d, i, a, active):
    title, lines, chips, gk, gate = STAGES[i]
    g = GROUPS[gk]
    x, y = pos(i)
    y += int((1 - a) * 30)
    if active:
        rrect(d, (x - 6, y - 6, x + CW + 6, y + CH + 6), 24, fill=mix(g["soft"], a))
    border = g["main"] if active else (210, 216, 226)
    rrect(d, (x, y, x + CW, y + CH), 20, fill=mix(WHITE, a), outline=mix(border, a), width=4 if active else 2)
    # coloured header band
    rrect(d, (x + 2, y + 2, x + CW - 2, y + 82), 18, fill=mix(g["main"], a))
    d.rectangle([(x + 2) * S, (y + 60) * S, (x + CW - 2) * S, (y + 82) * S], fill=mix(g["main"], a))
    # number badge
    d.ellipse([(x + 18) * S, (y + 18) * S, (x + 64) * S, (y + 64) * S], fill=mix(WHITE, a, g["main"]))
    text(d, x + 41, y + 22, str(i + 1), font("Bold", 26), mix(g["dark"], a), anchor="m")
    text(d, x + 78, y + 21, title, font("Bold", 29), mix(WHITE, a))
    # body
    for k, ln in enumerate(lines):
        text(d, x + 24, y + 100 + k * 31, ln, font("Medium", 22), mix(BODY, a))
    cx, cy = x + 24, y + 104 + len(lines) * 31 + 6
    cf = font("Demi Bold", 17)
    for ch in chips:
        cw = tlen(d, ch, cf) / S + 24
        if cx + cw > x + CW - 20:
            cx, cy = x + 24, cy + 40
        rrect(d, (cx, cy, cx + cw, cy + 32), 16, fill=mix(g["soft"], a), outline=mix(g["main"], a), width=2)
        text(d, cx + 12, cy + 4, ch, cf, mix(g["dark"], a))
        cx += cw + 8
    # footer: owner + gate
    ff = font("Demi Bold", 16)
    text(d, x + 24, y + CH - 40, g["name"], ff, mix(g["main"], a))
    if gate:
        gw = tlen(d, gate, ff) / S + 24
        rrect(d, (x + CW - 20 - gw, y + CH - 44, x + CW - 20, y + CH - 14), 15, fill=mix(GROUPS["you"]["soft"], a),
              outline=mix(GROUPS["you"]["main"], a), width=2)
        text(d, x + CW - 20 - gw + 12, y + CH - 41, gate, ff, mix(GROUPS["you"]["dark"], a))


def arrow(d, i, a, hot):
    c = mix((20, 30, 50) if hot else LINE, a)
    w = 5 * S
    if i == 3:
        x1 = pos(3)[0] + CW // 2
        x2 = pos(4)[0] + CW // 2
        ym = ROW_Y[0] + CH + 28
        pts = [(x1, ROW_Y[0] + CH + 8), (x1, ym), (x2, ym), (x2, ROW_Y[1] - 18)]
        d.line([(px * S, py * S) for px, py in pts], fill=c, width=w, joint="curve")
        d.polygon([((x2 - 11) * S, (ROW_Y[1] - 22) * S), ((x2 + 11) * S, (ROW_Y[1] - 22) * S), (x2 * S, (ROW_Y[1] - 6) * S)], fill=c)
        return
    x, y = pos(i)
    ax, ay = x + CW + 5, y + CH // 2
    d.line([(ax * S, ay * S), ((ax + GAP - 18) * S, ay * S)], fill=c, width=w)
    d.polygon([((ax + GAP - 20) * S, (ay - 10) * S), ((ax + GAP - 20) * S, (ay + 10) * S), ((ax + GAP - 6) * S, ay * S)], fill=c)


HEAD = header()


def frame(revealed, active=None, footer=0.0):
    im = HEAD.copy()
    d = ImageDraw.Draw(im)
    n = len(STAGES)
    for i in range(n - 1):
        if revealed - i > 1:
            arrow(d, i, min(1.0, revealed - i - 1), active is not None and active == i + 1)
    for i in range(n):
        a = max(0.0, min(1.0, revealed - i))
        if a > 0:
            card(d, i, a, active == i)
    if footer > 0:
        g = GROUPS["you"]
        f = font("Demi Bold", 22)
        t = "↻  Results feed back into ad copy and the calendar every month"
        w = tlen(d, t, f) / S + 48
        x = (W - w) / 2
        rrect(d, (x, H - 62, x + w, H - 18), 22, fill=mix(g["soft"], footer), outline=mix(g["main"], footer), width=2)
        text(d, W / 2, H - 58, t, f, mix(g["dark"], footer), anchor="m")
    return im.resize((W, H), Image.LANCZOS)


def ease(t):
    return 1 - (1 - t) ** 3


frames, dur = [], []
n = len(STAGES)
STEPS = 5
for i in range(n):
    for k in range(1, STEPS + 1):
        frames.append(frame(i + ease(k / STEPS), active=i))
        dur.append(45)
    dur[-1] = 260
for k in range(1, 5):
    frames.append(frame(n + 1, footer=k / 4))
    dur.append(50)
for i in range(n):
    frames.append(frame(n + 1, active=i, footer=1))
    dur.append(700)
frames.append(frame(n + 1, footer=1))
dur.append(2500)

pal = [f.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE) for f in frames]
pal[0].save("docs/workflow.gif", save_all=True, append_images=pal[1:], duration=dur, loop=0, optimize=True)
frames[-1].save("docs/workflow-preview.png")
frames[n * STEPS + 4 + 4].save("docs/workflow-active.png")
print("saved", len(frames), "frames")
