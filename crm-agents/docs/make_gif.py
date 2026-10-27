"""Renders the CRM Agents architecture as an animated GIF."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 900
BG, INK, MUTED = "#0f1b2d", "#ffffff", "#9fb3c8"
COL = {"data": "#3a506b", "core": "#1f6feb", "rt": "#8957e5",
       "rg": "#d1242f", "cp": "#bf8700", "del": "#1a7f37", "learn": "#0e7490"}


def font(size, bold=False):
    for f in (["/System/Library/Fonts/Supplemental/Arial Bold.ttf"] if bold else []) + \
             ["/System/Library/Fonts/Supplemental/Arial.ttf", "/System/Library/Fonts/Helvetica.ttc"]:
        try:
            return ImageFont.truetype(f, size)
        except OSError:
            pass
    return ImageFont.load_default()


F_T, F_B, F_S = font(30, True), font(17, True), font(13)

# (key, x, y, w, h, title, subtitle, colour)
BOX = [
    ("data", 60, 90, 1080, 70, "DATA LAYER",
     "Gaming platform · Retail (loyalty card) · App/web events · Payments · RG limits", "data"),
    ("a1", 330, 195, 540, 60, "1  Player 360 & Segmentation", "one profile + micro-segments", "core"),
    ("a2", 330, 285, 540, 60, "2  Predictive Scoring", "churn · LTV · next best action", "core"),
    ("a3", 180, 375, 380, 60, "3  Journey Orchestrator", "multi-step journeys", "core"),
    ("a4", 640, 375, 380, 60, "4  Real-Time Trigger", "events → send in seconds", "rt"),
    ("a8", 180, 475, 380, 70, "8  RG GUARDIAN  (VETO)", "promo → care message if at risk", "rg"),
    ("a9", 640, 475, 380, 70, "9  Contact Policy", "caps · quiet hours · best uplift wins", "cp"),
    ("a7", 330, 585, 540, 60, "7  Personalisation", "email · push · SMS · in-app · web  (fi/sv/en)", "del"),
    ("a5", 60, 700, 340, 70, "5  Uplift & Control", "holdout · incremental revenue", "learn"),
    ("a6", 430, 700, 340, 70, "6  Self-Optimising Test", "bandits on uplift, not spend", "learn"),
    ("a10", 800, 700, 340, 70, "10  Insights & Calendar", "weekly summary · Q&A", "learn"),
]
B = {b[0]: b for b in BOX}
ORDER = ["data", "a1", "a2", "a3", "a4", "a8", "a9", "a7", "a5", "a6", "a10"]
EDGES = [("data", "a1"), ("a1", "a2"), ("a2", "a3"), ("a2", "a4"), ("a3", "a4"),
         ("a3", "a8"), ("a4", "a8"), ("a8", "a9"), ("a9", "a7"),
         ("a7", "a5"), ("a7", "a6"), ("a7", "a10")]
STEPS = [
    ("a2", "Churn risk 0.30 → 0.75 after 3 missed Lotto draws"),
    ("a8", "RG check: low risk → continue (high risk → care message, stop)"),
    ("a9", "1 message this week → send allowed"),
    ("a3", "Win-back journey starts, 10% held back as control"),
    ("a7", "Hook: their usual game (Lotto) + next jackpot"),
    ("a6", "Tests push vs email, evening vs morning"),
    ("a5", "Day 14: +4.2 pts reactivation vs control"),
    ("a10", "Weekly summary: suggest making it always-on"),
]


def centre(k, side):
    _, x, y, w, h, *_ = B[k]
    return (x + w // 2, y + h) if side == "b" else (x + w // 2, y)


def lerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


def frame(shown, active=None, pulse=None, caption="", step_no=None):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.text((60, 28), "CRM Agents · AI Architecture", font=F_T, fill=INK)
    d.text((W - 60, 40), "RG Guardian can veto any message", font=F_S, fill="#ff8a8a", anchor="ra")
    for a, b in EDGES:
        if a in shown and b in shown:
            p, q = centre(a, "b"), centre(b, "t")
            if a == "a3" and b == "a4":
                p, q = (560, 405), (640, 405)
            if a == "a8" and b == "a9":
                p, q = (560, 510), (640, 510)
            if a == "a4" and b == "a8":
                p, q = (720, 435), (500, 475)
            d.line([p, q], fill="#4b6584", width=3)
            d.polygon([(q[0] - 6, q[1] - 9), (q[0] + 6, q[1] - 9), q] if q[1] > p[1]
                      else [(q[0] - 9, q[1] - 6), (q[0] - 9, q[1] + 6), q], fill="#4b6584")
    for k in ORDER:
        if k not in shown:
            continue
        _, x, y, w, h, t, s, c = B[k]
        fill = COL[c]
        if k == active:
            d.rounded_rectangle([x - 6, y - 6, x + w + 6, y + h + 6], 16, outline="#ffd33d", width=4)
        d.rounded_rectangle([x, y, x + w, y + h], 12, fill=fill)
        d.text((x + w // 2, y + h // 2 - 10), t, font=F_B, fill=INK, anchor="mm")
        d.text((x + w // 2, y + h // 2 + 13), s, font=F_S, fill="#e6edf3", anchor="mm")
    # learning loop arrow back to data
    if "a10" in shown:
        d.line([(1140, 735), (1170, 735), (1170, 125), (1140, 125)], fill="#0e7490", width=3)
        d.polygon([(1140, 125), (1150, 119), (1150, 131)], fill="#0e7490")
        d.text((1170, 410), "learn", font=F_S, fill="#7dd3fc", anchor="mm")
    if pulse:
        x, y = pulse
        d.ellipse([x - 9, y - 9, x + 9, y + 9], fill="#ffd33d")
    if caption:
        d.rounded_rectangle([60, 800, 1140, 870], 12, fill="#16263d", outline="#ffd33d")
        label = f"Churn win-back · step {step_no}/8" if step_no else "Governance"
        d.text((80, 812), label, font=F_S, fill="#ffd33d")
        d.text((80, 834), caption, font=F_B, fill=INK)
    return im


frames, durations = [], []
shown = []
for k in ORDER:                       # build-up
    shown.append(k)
    frames.append(frame(list(shown), active=k)); durations.append(350)
frames.append(frame(shown)); durations.append(900)

path = ["data", "a1", "a2", "a3", "a8", "a9", "a7"]   # a player flowing through
for a, b in zip(path, path[1:]):
    p, q = centre(a, "b"), centre(b, "t")
    for i in range(5):
        frames.append(frame(shown, active=b, pulse=lerp(p, q, i / 4))); durations.append(70)

for n, (k, cap) in enumerate(STEPS, 1):   # worked example
    frames.append(frame(shown, active=k, caption=cap, step_no=n)); durations.append(1600)

frames.append(frame(shown, active="a8",
                    caption="People approve journeys & RG thresholds · every decision logged (GDPR)"))
durations.append(2500)

frames[0].save(__import__("os").path.join(__import__("os").path.dirname(__import__("os").path.dirname(__import__("os").path.abspath(__file__))), "crm-agents-architecture.gif"), save_all=True, append_images=frames[1:],
               duration=durations, loop=0, optimize=True)
print(f"{len(frames)} frames written")
