"""Renders docs/workflow.gif - the animated infographic of the agent workflow.
    pip install pillow && python docs/make_gif.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 820
BG, INK, MUTED, LINE = (15, 23, 42), (241, 245, 249), (148, 163, 184), (51, 65, 85)
BLUE, GREEN, AMBER, PURPLE, PINK = (59, 130, 246), (34, 197, 94), (245, 158, 11), (168, 85, 247), (236, 72, 153)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "workflow.gif")


def font(size, bold=False):
    for p in (["/System/Library/Fonts/Supplemental/Arial Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]
              if bold else ["/System/Library/Fonts/Supplemental/Arial.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


F_T, F_H, F_B, F_S = font(34, True), font(19, True), font(16), font(14)

STAGES = [  # (label, x, color, items)
    ("1  TRIGGER", 30, BLUE, ["GitHub Actions", "Weekly: Mon 06:00", "  speed agents", "Monthly: 1st", "  full audit", "Manual run"]),
    ("2  DATA (free)", 240, AMBER, ["PageSpeed Insights", "  API (Google)", "Ahrefs Webmaster", "  Tools exports", "Search Console", "Built-in crawler"]),
    ("4  COMBINE", 790, PURPLE, ["run.py collects", "  all 10 results", "Compares with", "  last run", "Claude writes", "  exec summary"]),
    ("5  DELIVER", 1000, GREEN, ["Scorecard (.md)", "GitHub Issue", "Slack alerts", "Owner tasks", "History saved", ""]),
]
AGENTS = [
    ("1", "Core Web Vitals baseline", BLUE), ("2", "Conversion leakage (LCP)", BLUE),
    ("3", "Speed fix backlog", BLUE), ("4", "Marketing tag bloat", BLUE),
    ("5", "Accessibility & compliance", BLUE), ("6", "Site health score", PINK),
    ("7", "Crawl budget & link equity", PINK), ("8", "Striking-distance keywords", PINK),
    ("9", "Backlink authority", PINK), ("10", "Early-warning alerts", PINK),
]
TOP, BOT = 150, 640


def dim(c, a):
    return tuple(int(BG[i] + (c[i] - BG[i]) * a) for i in range(3))


def stage_box(d, label, x, color, items, on, w=170):
    a = 1.0 if on else 0.28
    d.rounded_rectangle([x, TOP, x + w, BOT], 14, fill=dim(color, 0.12 * a + 0.04), outline=dim(color, a), width=3 if on else 1)
    d.text((x + 14, TOP + 16), label, font=F_H, fill=dim(color, a))
    y = TOP + 64
    for it in items:
        d.text((x + 14, y), it, font=F_B if not it.startswith("  ") else F_S,
               fill=dim(INK if not it.startswith("  ") else MUTED, a))
        y += 34 if not it.startswith("  ") else 40


def arrow(d, x1, x2, y, on):
    c = INK if on else LINE
    d.line([x1, y, x2 - 10, y], fill=c, width=4)
    d.polygon([(x2, y), (x2 - 14, y - 9), (x2 - 14, y + 9)], fill=c)


def frame(step, active_agent=-1):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.text((30, 26), "AI Website Audit Agents", font=F_T, fill=INK)
    d.text((30, 74), "10 agents  ·  PageSpeed Insights + Ahrefs Webmaster Tools  ·  fully automated with GitHub Actions + Claude",
           font=F_B, fill=MUTED)
    d.line([30, 118, W - 30, 118], fill=LINE, width=1)
    for i, (label, x, color, items) in enumerate(STAGES[:2]):
        stage_box(d, label, x, color, items, step >= i)
    # agent grid
    on = step >= 2
    gx, gw = 450, 310
    d.rounded_rectangle([gx, TOP, gx + gw, BOT], 14, fill=dim(PINK, 0.06 if on else 0.02),
                        outline=INK if on else LINE, width=3 if on else 1)
    d.text((gx + 14, TOP + 16), "3  RUN 10 AI AGENTS", font=F_H, fill=INK if on else MUTED)
    for i, (n, name, color) in enumerate(AGENTS):
        y = TOP + 58 + i * 42
        lit = on and (active_agent < 0 or i <= active_agent)
        hot = i == active_agent
        d.rounded_rectangle([gx + 12, y, gx + gw - 12, y + 34], 8,
                            fill=dim(color, 0.55 if hot else (0.22 if lit else 0.06)),
                            outline=dim(color, 1 if lit else 0.3), width=2 if hot else 1)
        d.ellipse([gx + 20, y + 5, gx + 44, y + 29], fill=dim(color, 1 if lit else 0.3))
        d.text((gx + 32, y + 17), n, font=F_S, fill=BG, anchor="mm")
        d.text((gx + 54, y + 8), name, font=F_B, fill=dim(INK, 1 if lit else 0.35))
    for i, (label, x, color, items) in enumerate(STAGES[2:]):
        stage_box(d, label, x, color, items, step >= 3 + i)
    mid = (TOP + BOT) // 2
    arrow(d, 202, 238, mid, step >= 1)
    arrow(d, 412, 448, mid, step >= 2)
    arrow(d, 762, 788, mid, step >= 3)
    arrow(d, 962, 998, mid, step >= 4)
    # legend + KPI band
    d.text((30, 668), "Speed & experience (PageSpeed)", font=F_S, fill=BLUE)
    d.text((300, 668), "Search visibility & health (Ahrefs / crawler)", font=F_S, fill=PINK)
    d.rounded_rectangle([30, 700, W - 30, 790], 12, fill=(30, 41, 59))
    kpis = ["CWV pass ≥75%", "LCP < 2.5s", "Tags < 250ms", "A11y ≥ 90", "Health ≥ 90", "0 broken pages", "+ top-3 keywords", "+ ref. domains"]
    d.text((50, 712), "KPIs tracked every run", font=F_H, fill=INK if step >= 4 else MUTED)
    x = 50
    for k in kpis:
        tw = d.textlength(k, font=F_S) + 22
        d.rounded_rectangle([x, 748, x + tw, 776], 14, fill=dim(GREEN, 0.25 if step >= 4 else 0.08))
        d.text((x + 11, 754), k, font=F_S, fill=INK if step >= 4 else MUTED)
        x += tw + 10
    return im


def _palette():
    """Fixed palette built from the design colors, so brand colors stay exact and the file stays small."""
    cols = []
    for c in (INK, MUTED, BLUE, GREEN, AMBER, PURPLE, PINK, (30, 41, 59), LINE):
        for a in (0, .06, .12, .2, .28, .4, .55, .7, .85, 1):
            cols.append(dim(c, a))
    flat = [v for c in dict.fromkeys(cols) for v in c]
    pal = Image.new("P", (1, 1))
    pal.putpalette(flat + [0] * (768 - len(flat)))
    return pal


def main(full="--full" in __import__("sys").argv):
    """Default: 6-frame GIF (~100KB). --full: 15 frames, agents light up one by one (~500KB)."""
    if full:
        frames = [frame(0), frame(1)] + [frame(2, i) for i in range(10)] + [frame(2), frame(3), frame(4), frame(5)]
        durs = [900, 900] + [380] * 10 + [600, 900, 900, 3500]
    else:
        frames = [frame(0), frame(1), frame(2, 4), frame(2), frame(3), frame(5)]
        durs = [1000, 1000, 1200, 1200, 1000, 3500]
    pal = _palette()
    out = [f.quantize(palette=pal, dither=Image.NONE) for f in frames]
    out[0].save(OUT, save_all=True, append_images=out[1:], duration=durs, loop=0, optimize=True)
    print("Saved", OUT, "({} frames)".format(len(frames)))


if __name__ == "__main__":
    main()
