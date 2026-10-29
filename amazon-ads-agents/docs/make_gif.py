"""Render the 12-agent Amazon Ads workflow as an animated GIF."""
from PIL import Image, ImageDraw, ImageFont
import os

S = 2                       # supersample factor for crisp edges
W, H = 1600, 900
F = "/System/Library/Fonts/Avenir Next.ttc"
def font(size, idx): return ImageFont.truetype(F, size * S, index=idx)
BOLD, DEMI, MED, REG = 0, 2, 5, 7

BG, DOT, INK, MUTED = (243, 245, 250), (205, 210, 222), (20, 24, 38), (95, 102, 118)
STAGES = {
    "SETUP":    ((22, 163, 74),  (220, 245, 228)),
    "BUILD":    ((217, 119, 6),  (254, 239, 214)),
    "OPTIMIZE": ((109, 74, 214), (234, 228, 252)),
}
AGENTS = [
    ("Product research", "Break-even ACoS, max CPC, hero ASINs", "SETUP"),
    ("Keyword research", "Intent clusters, relevance, negatives", "SETUP"),
    ("Competitor intel", "Attack / avoid ASINs, brand defense", "SETUP"),
    ("Listing readiness", "Retail score /100 — go or fix first", "SETUP"),
    ("Account architect", "Portfolios, naming, budget split", "BUILD"),
    ("Sponsored Products", "Bulk CSV, bids, placements", "BUILD"),
    ("Sponsored Brands", "Headline + video ads, briefs", "BUILD"),
    ("Display & DSP", "Retargeting, audiences, contextual", "BUILD"),
    ("Search term harvest", "Winners → Exact, waste → negatives", "OPTIMIZE"),
    ("Bid optimizer", "Target-ACoS bids, placement shifts", "OPTIMIZE"),
    ("Budget & pacing", "Out-of-budget fixes, Prime Day ramps", "OPTIMIZE"),
    ("Reporting", "ACoS, TACoS, ROAS, organic rank", "OPTIMIZE"),
]

M, GAP, TOP = 48, 24, 230
CW = (W - 2 * M - 3 * GAP) // 4
CH = 196
def card_xy(i):
    r, c = divmod(i, 4)
    return M + c * (CW + GAP), TOP + r * (CH + 22)

def s(v): return int(v * S)

def pill(d, x, y, text, fg, fill, outline, f, right=False):
    tw = d.textlength(text, font=f)
    w, h = tw + s(32), s(36)
    if right: x = x - w
    d.rounded_rectangle([x, y, x + w, y + h], radius=h // 2, fill=fill, outline=outline, width=s(2))
    d.text((x + w / 2, y + h / 2), text, font=f, fill=fg, anchor="mm")
    return x

ARW = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
def atext(d, xy, text, font, fill, anchor="la"):
    """Draw text; arrows are drawn as vector lines (Avenir has no arrow glyph)."""
    x, y = xy
    f = font
    asc, desc = f.getmetrics()
    mid = y + asc * 0.62
    aw, gap, lw = f.size * 0.7, f.size * 0.35, max(2, f.size // 11)
    for k, part in enumerate(text.split("→")):
        part = part.strip()
        if k:
            x += gap
            d.line([(x, mid), (x + aw, mid)], fill=fill, width=lw)
            d.line([(x + aw * 0.6, mid - aw * 0.35), (x + aw, mid), (x + aw * 0.6, mid + aw * 0.35)],
                   fill=fill, width=lw, joint="curve")
            x += aw + gap
        d.text((x, y), part, font=f, fill=fill); x += d.textlength(part, font=f)

def wrap(d, text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else: lines.append(cur); cur = w
    lines.append(cur)
    return lines

def base():
    im = Image.new("RGB", (s(W), s(H)), BG)
    from PIL import ImageFilter
    glow = Image.new("L", (s(W), s(H)), 0)
    ImageDraw.Draw(glow).ellipse([s(W*0.55), s(-H*0.6), s(W*1.35), s(H*0.55)], fill=120)
    glow = glow.filter(ImageFilter.GaussianBlur(s(90)))
    im.paste(Image.new("RGB", im.size, (233, 226, 250)), mask=glow)
    d = ImageDraw.Draw(im)
    for y in range(12, H, 30):
        for x in range(12, W, 30):
            d.ellipse([s(x) - S, s(y) - S, s(x) + S, s(y) + S], fill=DOT)
    pill(d, s(M), s(34), "AMAZON ADS AGENTS", (255, 255, 255), (22, 163, 74), (22, 163, 74), font(15, BOLD))
    d.text((s(M - 2), s(76)), "An AI team for Amazon Ads", font=font(50, BOLD), fill=INK)
    atext(d, (s(M), s(148)), "Research → setup → build → harvest → bid → budget → report",
           font=font(21, MED), fill=(60, 66, 82))
    x = s(W - M)
    for t, fg, bg in [("You approve", (91, 64, 190), (237, 233, 254)),
                      ("Weekly loop", (21, 128, 61), (220, 245, 228)),
                      ("12 agents", (180, 83, 9), (254, 239, 214))]:
        x = pill(d, x, s(40), t, fg, bg, fg, font(17, DEMI), right=True) - s(12)
    # stage labels
    for r, st in enumerate(STAGES):
        col = STAGES[st][0]
        d.text((s(W - M), s(TOP - 26)) if False else (s(M), s(TOP - 30 + r * (CH + 22))) ,
               "", font=font(1, REG))
    return im

def draw_card(i, active):
    name, desc, st = AGENTS[i]
    col, tint = STAGES[st]
    layer = Image.new("RGBA", (s(CW + 16), s(CH + 16)), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    o = s(8)
    d.rounded_rectangle([o, o + s(4), o + s(CW), o + s(CH) + s(4)], radius=s(18), fill=(20, 24, 38, 28))
    border = col if active else (210, 214, 224)
    d.rounded_rectangle([o, o, o + s(CW), o + s(CH)], radius=s(18), fill=(250, 251, 253), outline=border, width=s(3))
    d.rounded_rectangle([o, o, o + s(CW), o + s(66)], radius=s(18), fill=col)
    d.rectangle([o + s(3), o + s(40), o + s(CW) - s(3), o + s(66)], fill=col)
    d.text((o + s(22), o + s(33)), f"{i + 1:02d}", font=font(20, BOLD), fill=(255, 255, 255, 150), anchor="lm")
    d.text((o + s(62), o + s(33)), name, font=font(23, DEMI), fill=(255, 255, 255), anchor="lm")
    fy = o + s(82)
    for ln in wrap(d, desc, font(18, MED), s(CW - 44))[:2]:
        atext(d, (o + s(22), fy), ln, font=font(18, MED), fill=MUTED); fy += s(28)
    pill(d, o + s(20), o + s(CH - 48), st, col, tint, tint, font(12, BOLD))
    if active:
        d.ellipse([o + s(CW - 34), o + s(CH - 38), o + s(CW - 20), o + s(CH - 24)], fill=col)
    return layer

import math
_BASE = None
def base_cached():
    global _BASE
    if _BASE is None: _BASE = base().convert("RGBA")
    return _BASE.copy()

def color_of(i): return STAGES[AGENTS[i][2]][0]

def conn_path(i):
    """Arrow path (unscaled px) from card i to card i+1."""
    x0, y0 = card_xy(i); x1, y1 = card_xy(i + 1)
    if y0 == y1:                                   # same row → straight right
        ym = y0 + 33
        return [(x0 + CW + 2, ym), (x1 - 4, ym)]
    gy = y0 + CH + 11                              # row change → elbow through gap
    return [(x0 + CW / 2, y0 + CH + 2), (x0 + CW / 2, gy), (x1 + CW / 2, gy), (x1 + CW / 2, y1 - 4)]

def loop_path():
    x9, y9 = card_xy(8); x12, _ = card_xy(11)
    by = y9 + CH + 22
    return [(x12 + CW / 2, y9 + CH + 2), (x12 + CW / 2, by), (x9 + CW / 2, by), (x9 + CW / 2, y9 + CH + 4)]

def seg_lengths(pts):
    return [math.dist(pts[k], pts[k + 1]) for k in range(len(pts) - 1)]

def partial(pts, t):
    """Points of the path drawn up to fraction t, plus the tip."""
    L = seg_lengths(pts); tot = sum(L); want = tot * t; out = [pts[0]]
    for k, l in enumerate(L):
        if want <= l:
            a, b = pts[k], pts[k + 1]; r = want / l if l else 0
            tip = (a[0] + (b[0] - a[0]) * r, a[1] + (b[1] - a[1]) * r)
            out.append(tip); return out, tip, (b[0] - a[0], b[1] - a[1])
        want -= l; out.append(pts[k + 1])
    a, b = pts[-2], pts[-1]
    return out, pts[-1], (b[0] - a[0], b[1] - a[1])

def draw_arrow(im, pts, t, col, head=True, dot=True, dash=False):
    d = ImageDraw.Draw(im)
    drawn, tip, vec = partial(pts, t)
    sp = [(s(x), s(y)) for x, y in drawn]
    if dash:
        for k in range(len(sp) - 1):
            (ax, ay), (bx, by) = sp[k], sp[k + 1]
            n = max(1, int(math.dist(sp[k], sp[k + 1]) // s(12)))
            for j in range(0, n, 2):
                d.line([(ax + (bx - ax) * j / n, ay + (by - ay) * j / n),
                        (ax + (bx - ax) * (j + 1) / n, ay + (by - ay) * (j + 1) / n)], fill=col, width=s(3))
    else:
        d.line(sp, fill=col, width=s(3), joint="curve")
    if head and t >= 0.999:
        ang = math.atan2(vec[1], vec[0]); hx, hy = s(tip[0]), s(tip[1]); L = s(11)
        d.polygon([(hx, hy), (hx - L * math.cos(ang - 0.5), hy - L * math.sin(ang - 0.5)),
                   (hx - L * math.cos(ang + 0.5), hy - L * math.sin(ang + 0.5))], fill=col)
    if dot and t < 0.999:
        hx, hy = s(tip[0]), s(tip[1])
        glow = Image.new("RGBA", im.size, (0, 0, 0, 0)); g = ImageDraw.Draw(glow)
        g.ellipse([hx - s(14), hy - s(14), hx + s(14), hy + s(14)], fill=col + (70,))
        im.alpha_composite(glow)
        d.ellipse([hx - s(6), hy - s(6), hx + s(6), hy + s(6)], fill=(255, 255, 255), outline=col, width=s(3))

def put_card(im, i, active=False, alpha=1.0, dy=0.0, pulse=0.0):
    x, y = card_xy(i)
    if active and pulse > 0:                       # soft colored halo
        halo = Image.new("RGBA", im.size, (0, 0, 0, 0))
        r = s(6 + 8 * pulse)
        ImageDraw.Draw(halo).rounded_rectangle(
            [s(x) - r, s(y + dy) - r, s(x + CW) + r, s(y + CH + dy) + r], radius=s(22),
            fill=color_of(i) + (int(55 * pulse),))
        im.alpha_composite(halo)
    lay = draw_card(i, active)
    if alpha < 1:
        lay.putalpha(lay.getchannel("A").point(lambda v: int(v * alpha)))
    im.alpha_composite(lay, (s(x - 8), int(s(y - 8 + dy))))

def scene(n_cards, arrows_full, arrow_t=None, new_card=None, new_t=0, active=None, pulse=0,
          loop_t=None, runner=None):
    im = base_cached()
    for k in range(arrows_full):
        draw_arrow(im, conn_path(k), 1.0, color_of(k + 1))
    if arrow_t is not None:
        draw_arrow(im, conn_path(arrows_full), arrow_t, color_of(arrows_full + 1))
    if loop_t is not None:
        draw_arrow(im, loop_path(), loop_t, STAGES["OPTIMIZE"][0], dot=loop_t < 1, dash=True)
    for i in range(n_cards):
        if i == active:
            put_card(im, i, True, dy=-6 * pulse, pulse=pulse)
        else:
            put_card(im, i)
    if new_card is not None:
        e = 1 - (1 - new_t) ** 3
        over = math.sin(new_t * math.pi) * 0.25     # small overshoot = "pop"
        put_card(im, new_card, True, alpha=e, dy=28 * (1 - e) - 6 * over, pulse=e)
    if runner is not None:                          # dot travelling the weekly loop
        pts, t = runner
        _, tip, _ = partial(pts, t)
        hx, hy = s(tip[0]), s(tip[1]); col = STAGES["OPTIMIZE"][0]
        g = Image.new("RGBA", im.size, (0, 0, 0, 0))
        ImageDraw.Draw(g).ellipse([hx - s(16), hy - s(16), hx + s(16), hy + s(16)], fill=col + (70,))
        im.alpha_composite(g)
        ImageDraw.Draw(im).ellipse([hx - s(7), hy - s(7), hx + s(7), hy + s(7)],
                                   fill=(255, 255, 255), outline=col, width=s(3))
    return im.convert("RGB").resize((W, H), Image.LANCZOS)

frames, durs = [], []
def add(im, ms): frames.append(im); durs.append(ms)

add(scene(0, 0), 500)
for i in range(12):
    if i > 0:                                       # arrow draws itself from previous card
        for k in range(1, 7):
            add(scene(i, i - 1, arrow_t=k / 6, active=i - 1, pulse=0.6), 35)
    for k in range(1, 8):                           # card pops in
        add(scene(i, i, new_card=i, new_t=k / 7), 38)
    for k in range(6):                              # lift + pulse while "working"
        p = 0.6 + 0.4 * math.sin(k / 5 * math.pi)
        add(scene(i + 1, i, active=i, pulse=p), 70)
# weekly loop: dashed return arrow 12 → 9, then a dot runs 9→10→11→12→9
for k in range(1, 9):
    add(scene(12, 11, loop_t=k / 8), 40)
ring = [conn_path(8)[0], conn_path(8)[1], conn_path(9)[1], conn_path(10)[1]] + loop_path()[1:]
for lap in range(2):
    for k in range(24):
        t = k / 24
        act = 8 + min(3, int(t * 4.6))
        add(scene(12, 11, loop_t=1, active=act, pulse=0.8, runner=(ring, t)), 55)
add(scene(12, 11, loop_t=1), 2400)

# one shared palette so colors stay stable (no flicker)
strip = Image.new("RGB", (W, H * 3))
for j, idx in enumerate([len(frames) - 1, len(frames) - 20, 60]):
    strip.paste(frames[idx], (0, H * j))
pal = strip.quantize(colors=256, method=Image.Quantize.MEDIANCUT)
q = [f.quantize(palette=pal, dither=Image.Dither.NONE) for f in frames]

out = os.path.join(os.path.dirname(__file__), "../amazon-ads-agents-workflow.gif")
q[0].save(out, save_all=True, append_images=q[1:], duration=durs, loop=0, optimize=True, disposal=1)
frames[-1].save(out.replace(".gif", "-final.png"))
print(out, len(q), "frames", os.path.getsize(out) // 1024, "KB")
