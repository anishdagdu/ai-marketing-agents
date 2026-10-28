import sys
from PIL import Image, ImageDraw, ImageFont

OUT = sys.argv[1]
W, H = 1200, 900
BG = (14, 17, 28)
CARD = (27, 32, 50)
CHIP = (35, 41, 63)
EDGE = (52, 60, 88)
TXT = (236, 239, 247)
MUTED = (150, 158, 184)
ACCENTS = [(56, 189, 248), (167, 139, 250), (52, 211, 153), (251, 191, 36), (244, 114, 182)]
LEAD = (149, 191, 71)  # Shopify green

F = "/System/Library/Fonts/Avenir Next.ttc"
def font(size, bold=False):
    return ImageFont.truetype(F, size, index=2 if bold else 0)

f_title = font(44, True); f_sub = font(21); f_num = font(18, True); f_stage = font(16, True); f_lead = font(20, True)
f_agent = font(15, True); f_desc = font(14); f_tag = font(14, True); f_small = font(17); f_body = font(18)

STAGES = [
    ("Fix the store", [("sh-store-setup", "Settings, theme, apps"), ("sh-debugger", "Root cause + fix"),
                       ("sh-catalog", "Products + feed"), ("sh-inventory", "Stockout risk")]),
    ("Convert", [("sh-conversion", "Pages, cart, checkout"), ("sh-support", "FAQs + chatbot"),
                 ("sh-shipping-returns", "Costs + returns")]),
    ("Bring traffic", [("sh-seo", "Google + AI search"), ("sh-content-social", "Organic calendar"),
                       ("sh-paid-ads", "Meta, Google, TikTok")]),
    ("Bring them back", [("sh-email-sms", "Klaviyo flows (drafts)"), ("sh-retention-reviews", "LTV, loyalty, reviews")]),
    ("Measure + profit", [("sh-analytics-tracking", "Weekly readout"), ("sh-profit-pricing", "Margin + break-even")]),
]
COL_W, GAP, X0, Y0, Y1 = 200, 20, 60, 300, 690
COLS = [(X0 + i * (COL_W + GAP), Y0, X0 + i * (COL_W + GAP) + COL_W, Y1) for i in range(5)]
ORCH = (60, 170, 1140, 250)

def mix(c, k):
    return tuple(int(BG[i] + (c[i] - BG[i]) * k) for i in range(3))

def arrow_r(d, x0, x1, y, col):
    d.line([(x0, y), (x1, y)], fill=col, width=4)
    d.polygon([(x1, y), (x1 - 12, y - 8), (x1 - 12, y + 8)], fill=col)

def arrow_d(d, x, y0, y1, col):
    d.line([(x, y0), (x, y1)], fill=col, width=4)
    d.polygon([(x, y1), (x - 8, y1 - 12), (x + 8, y1 - 12)], fill=col)

def frame(lit, active=None, loop=False):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.text((60, 48), "Shopify AI Agents", font=f_title, fill=TXT)
    d.text((60, 110), "Fix the store  >  convert  >  bring traffic  >  bring them back  >  measure + profit", font=f_sub, fill=MUTED)
    d.text((1140, 62), "15 agents · 1 workflow", font=f_small, fill=MUTED, anchor="ra")

    # orchestrator
    on = bool(lit) or active == -1
    d.rounded_rectangle(ORCH, 18, fill=CARD, outline=LEAD if on else EDGE, width=3 if active == -1 else 2)
    d.ellipse((84, 192, 118, 226), fill=LEAD if on else EDGE)
    d.text((101, 209), "AI", font=f_tag, fill=BG, anchor="mm")
    d.text((134, 186), "sh-orchestrator", font=f_lead, fill=TXT if on else MUTED)
    d.text((134, 214), "Finds the biggest revenue leak, briefs the right agents, ranks every action", font=f_desc, fill=LEAD if on else MUTED)
    d.text((1116, 210), "SHOPIFY STORE DATA", font=f_tag, fill=LEAD if on else MUTED, anchor="rm")

    # orchestrator -> stage 1, stage arrows, loop back
    arrow_d(d, 160, 250, 296, ACCENTS[0] if 0 in lit else EDGE)
    for i in range(4):
        arrow_r(d, COLS[i][2] + 2, COLS[i + 1][0] - 2, 330, ACCENTS[i + 1] if i + 1 in lit else EDGE)
    lc = LEAD if loop else EDGE
    d.line([(1040, 296), (1040, 270), (1090, 270), (1090, 254)], fill=lc, width=4)
    d.polygon([(1090, 252), (1082, 264), (1098, 264)], fill=lc)
    d.text((1100, 274), "weekly", font=f_desc, fill=lc)

    for i, (stage, agents) in enumerate(STAGES):
        x0, y0, x1, y1 = COLS[i]
        c = ACCENTS[i]
        on = i in lit
        if i == active:
            for g in range(10, 0, -2):
                d.rounded_rectangle((x0 - g, y0 - g, x1 + g, y1 + g), 18 + g, outline=mix(c, 0.10 + (10 - g) * 0.03), width=2)
        d.rounded_rectangle(COLS[i], 18, fill=CARD if on else mix(CARD, 0.6), outline=c if on else EDGE, width=3 if i == active else 2)
        d.ellipse((x0 + 14, y0 + 18, x0 + 40, y0 + 44), fill=c if on else EDGE)
        d.text((x0 + 27, y0 + 31), str(i + 1), font=f_num, fill=BG, anchor="mm")
        d.text((x0 + 48, y0 + 31), stage, font=f_stage, fill=TXT if on else MUTED, anchor="lm")
        for j, (agent, desc) in enumerate(agents):
            cy = y0 + 64 + j * 78
            d.rounded_rectangle((x0 + 12, cy, x1 - 12, cy + 66), 12, fill=CHIP if on else mix(CHIP, 0.6), outline=mix(c, 0.5) if on else EDGE, width=1)
            d.text((x0 + 24, cy + 12), agent, font=f_agent, fill=c if on else MUTED)
            d.text((x0 + 24, cy + 36), desc, font=f_desc, fill=TXT if on else MUTED)

    # guardrails
    d.rounded_rectangle((60, 730, 1140, 860), 18, fill=CARD, outline=EDGE, width=2)
    d.text((84, 748), "AI RECOMMENDS. YOU APPROVE.", font=f_tag, fill=ACCENTS[2])
    rules = ["Every write needs your OK", "Drafts + duplicate theme", "Never changes ad budgets",
             "Never sends emails or SMS", "Never deletes data", "Assets labelled  AI ·"]
    for j, r in enumerate(rules):
        cx = 84 + (j % 3) * 352
        cy = 782 + (j // 3) * 34
        d.line([(cx, cy + 13), (cx + 6, cy + 19), (cx + 17, cy + 5)], fill=ACCENTS[2], width=3)
        d.text((cx + 28, cy), r, font=f_body, fill=TXT)
    return im.quantize(colors=48, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)

frames, durs = [frame(set())], [900]
frames.append(frame(set(), -1)); durs.append(1300)
lit = set()
for i in range(5):
    lit = lit | {i}
    frames.append(frame(lit, i)); durs.append(1300)
frames.append(frame(lit, loop=True)); durs.append(3200)

frames[0].save(OUT, save_all=True, append_images=frames[1:], duration=durs, loop=0, optimize=True, disposal=1)
print(OUT, len(frames))
