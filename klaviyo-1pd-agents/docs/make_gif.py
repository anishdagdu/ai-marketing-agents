import sys
from PIL import Image, ImageDraw, ImageFont

OUT = sys.argv[1]
W, H = 1200, 900
BG = (14, 17, 28)
CARD = (27, 32, 50)
EDGE = (52, 60, 88)
TXT = (236, 239, 247)
MUTED = (150, 158, 184)
ACCENTS = [(56, 189, 248), (167, 139, 250), (52, 211, 153), (251, 191, 36), (244, 114, 182)]
DATA_C = (148, 163, 184)

F = "/System/Library/Fonts/Avenir Next.ttc"
def font(size, bold=False):
    return ImageFont.truetype(F, size, index=(0 if bold else 7) if False else (2 if bold else 0))

f_title = font(44, True); f_sub = font(21); f_num = font(20, True)
f_name = font(25, True); f_body = font(18); f_tag = font(14, True); f_small = font(17)

STEPS = [
    ("kl-data-foundation", "Data foundation", ["Audit events, catalog, consent", "Readiness score + setup plan"], "READ-ONLY"),
    ("kl-segment-architect", "Segment architect", ["RFM, intent, VIP, at-risk", "Ad seed + exclusion audiences"], "CREATES ON APPROVAL"),
    ("kl-flow-builder", "Flow builder", ["Welcome, cart, browse flows", "Post-buy, win-back, sunset"], "DRAFTS ONLY"),
    ("kl-campaign-strategist", "Campaign strategist", ["4-week calendar per segment", "Personalised copy + A/B tests"], "DRAFTS · YOU SEND"),
    ("kl-performance-analyst", "Performance analyst", ["Weekly RPR + deliverability", "Routes fixes to each agent"], "READ-ONLY · WEEKLY"),
]
# card boxes (x0, y0, x1, y1)
BOX = [(60, 200, 380, 420), (440, 200, 760, 420), (820, 200, 1140, 420),
       (820, 480, 1140, 700), (440, 480, 760, 700)]
DATA = (60, 480, 380, 700)
# paths: into step i from previous node
PATHS = [
    [(220, 480), (220, 420)],             # data -> 1
    [(380, 310), (440, 310)],             # 1 -> 2
    [(760, 310), (820, 310)],             # 2 -> 3
    [(980, 420), (980, 480)],             # 3 -> 4
    [(820, 590), (760, 590)],             # 4 -> 5
]
LOOP = [(440, 590), (380, 590)]           # 5 -> data

def lerp_path(pts, t):
    (x0, y0), (x1, y1) = pts
    return (x0 + (x1 - x0) * t, y0 + (y1 - y0) * t)

def mix(c, k):
    return tuple(int(BG[i] + (c[i] - BG[i]) * k) for i in range(3))

def arrow(d, pts, col, w=4):
    d.line(pts, fill=col, width=w)
    (x0, y0), (x1, y1) = pts
    if x1 == x0:
        s = 1 if y1 > y0 else -1
        d.polygon([(x1, y1), (x1 - 9, y1 - 14 * s), (x1 + 9, y1 - 14 * s)], fill=col)
    else:
        s = 1 if x1 > x0 else -1
        d.polygon([(x1, y1), (x1 - 14 * s, y1 - 9), (x1 - 14 * s, y1 + 9)], fill=col)

def frame(lit, active=None, dot=None):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.text((60, 48), "Klaviyo 1PD AI Agents", font=f_title, fill=TXT)
    d.text((60, 110), "First-party data  >  segments  >  flows  >  campaigns  >  weekly loop", font=f_sub, fill=MUTED)
    d.text((1140, 62), "5 agents · 1 workflow", font=f_small, fill=MUTED, anchor="ra")

    # connectors
    for i, p in enumerate(PATHS):
        arrow(d, p, ACCENTS[i] if i in lit else EDGE)
    arrow(d, LOOP, ACCENTS[4] if 4 in lit and len(lit) == 5 else EDGE)

    # data box
    x0, y0, x1, y1 = DATA
    d.rounded_rectangle(DATA, 18, fill=CARD, outline=DATA_C if 0 in lit else EDGE, width=2)
    d.text((x0 + 24, y0 + 22), "YOUR KLAVIYO DATA", font=f_tag, fill=DATA_C)
    d.text((x0 + 24, y0 + 50), "First-party signals", font=f_name, fill=TXT)
    for j, l in enumerate(["Product views · cart adds", "Placed Order · email + SMS", "Form answers (zero-party)", "Consent status"]):
        d.text((x0 + 24, y0 + 94 + j * 26), "· " + l, font=f_body, fill=MUTED)

    for i, (agent, name, lines, tag) in enumerate(STEPS):
        x0, y0, x1, y1 = BOX[i]
        on = i in lit
        c = ACCENTS[i]
        if i == active:
            for g in range(10, 0, -2):
                d.rounded_rectangle((x0 - g, y0 - g, x1 + g, y1 + g), 18 + g, outline=mix(c, 0.10 + (10 - g) * 0.03), width=2)
        d.rounded_rectangle(BOX[i], 18, fill=CARD if on else mix(CARD, 0.6), outline=c if on else EDGE, width=3 if i == active else 2)
        d.ellipse((x0 + 22, y0 + 20, x0 + 56, y0 + 54), fill=c if on else EDGE)
        d.text((x0 + 39, y0 + 37), str(i + 1), font=f_num, fill=BG, anchor="mm")
        d.text((x0 + 70, y0 + 24), name, font=f_name, fill=TXT if on else MUTED)
        d.text((x0 + 24, y0 + 72), agent, font=f_small, fill=c if on else EDGE)
        for j, l in enumerate(lines):
            d.text((x0 + 24, y0 + 108 + j * 28), "· " + l, font=f_body, fill=TXT if on else MUTED)
        tw = d.textlength(tag, font=f_tag)
        d.rounded_rectangle((x0 + 24, y1 - 44, x0 + 44 + tw, y1 - 18), 8, fill=mix(c, 0.25) if on else EDGE)
        d.text((x0 + 34, y1 - 31), tag, font=f_tag, fill=c if on else MUTED, anchor="lm")

    if dot:
        x, y, col = dot
        d.ellipse((x - 9, y - 9, x + 9, y + 9), fill=col)

    # guardrails
    d.rounded_rectangle((60, 740, 1140, 860), 18, fill=CARD, outline=EDGE, width=2)
    d.text((84, 758), "AI RECOMMENDS. YOU APPROVE.", font=f_tag, fill=ACCENTS[2])
    rules = ["Every write needs your OK", "Flows saved as drafts", "Never sends campaigns",
             "Never suppresses or deletes", "Consented profiles only", "Assets labelled  AI ·"]
    for j, r in enumerate(rules):
        cx = 84 + (j % 3) * 352
        cy = 790 + (j // 3) * 32
        d.line([(cx, cy + 13), (cx + 6, cy + 19), (cx + 17, cy + 5)], fill=ACCENTS[2], width=3)
        d.text((cx + 28, cy), r, font=f_body, fill=TXT)
    return im.quantize(colors=32, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)

frames, durs = [], []
frames.append(frame(set())); durs.append(900)
lit = set()
for i in range(5):
    lit = lit | {i}
    frames.append(frame(lit, i)); durs.append(1300)
frames.append(frame(lit)); durs.append(3200)

frames[0].save(OUT, save_all=True, append_images=frames[1:], duration=durs, loop=0, optimize=True, disposal=1)
print(OUT, len(frames))
