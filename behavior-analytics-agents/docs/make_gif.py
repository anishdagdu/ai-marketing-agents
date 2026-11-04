"""Renders behavior-analytics-workflow.gif: the Clarity / Hotjar agents, animated.

Layout (different from the other sets): a live checkout page on the left reacts as the
team works (masking, heatmap blobs, rage-click ripples, an exit survey, the fix), while
the agents sit in four stacked lanes on the right and a token drops down through them.

Run: python3 behavior-analytics-agents/docs/make_gif.py  (needs Pillow and tools/gifkit.py)
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from gifkit import *  # noqa: E402,F403

OUT = os.path.join(HERE, "..", "behavior-analytics-workflow.gif")

# ---- live site mock (left)
MX0, MY0, MX1, MY1 = 40, 140, 440, 500
ADD = (255, 262, 420, 294)
PROMO = (60, 338, 300, 370)
APPLY = (308, 338, 420, 370)
CHECKOUT = (60, 392, 420, 428)

# ---- lanes (right)
LX0, LX1 = 470, 1080
ORCH = (LX0, 140, LX1, 190)
LANES = [
    ("1 · Capture", "Clarity + Hotjar", TEAL, ["Install + privacy", "Masking + consent"]),
    ("2 · Observe what", "Clarity", BLUE, ["Heatmaps", "Replays", "Rage + dead", "JS errors"]),
    ("3 · Ask why", "Hotjar", AMBER, ["Surveys", "Feedback", "Interviews"]),
    ("4 · Fix + prove", "Both + GA4", PINK, ["Funnels", "CRO report"]),
]
LY = [210 + i * 78 for i in range(4)]
LH = 58
OX0, OX1 = 1100, 1240
OUTS = [("Ranked fixes", "check"), ("Test ideas", "flask"), ("Readout", "doc")]
OY = [226 + i * 52 for i in range(3)]

L = {
    "site>orch": (Path(curve((MX1, 300), (LX0, 165))), CYAN),
    "orch>r0": (Path(poly((540, ORCH[3]), (540, LY[0]))), TEAL),
}
for i in range(3):
    L[f"r{i}>r{i+1}"] = (Path(poly((540, LY[i] + LH), (540, LY[i + 1]))), LANES[i + 1][2])
L["r3>out"] = (Path(curve((LX1, LY[3] + LH / 2), (OX0, OY[2] + 22))), GREEN)
L["out>orch"] = (Path(poly(((OX0 + OX1) / 2, OY[0]), ((OX0 + OX1) / 2, 165), (LX1 + 2, 165))), CYAN)

APPEAR = {"site": 0.15, "orch": 0.5, "out": 1.9, "band": 2.2}
APPEAR.update({f"r{i}": 0.85 + 0.22 * i for i in range(4)})

RULES = ["Every change needs your OK", "Masking stays on", "Surveys saved as drafts",
         "Never edits your site", "Never deletes recordings"]
seen = set()


def mock(c, t, state):
    a = window(t, APPEAR["site"], APPEAR["site"] + 0.5)
    if a <= 0.01:
        return
    act, st = state["act"], state["st"]
    u = st["u"] if st and st["phase"] == "dwell" else 0.0
    if act:
        seen.add(act)
    c.rect(MX0 + 2, MY0 + 4, MX1 + 2, MY1 + 6, r=14, fill=(15, 23, 42), a=a * 0.06)
    c.rect(MX0, MY0, MX1, MY1, r=14, fill=WHITE, outline=LINE, width=1.4, a=a)
    c.rect(MX0, MY0, MX1, MY0 + 30, r=14, fill=mix(BG, LINE, 0.3), a=a)
    for k, col in enumerate([RED, AMBER, GREEN]):
        c.circle(MX0 + 18 + k * 14, MY0 + 15, 4.5, fill=col, a=a)
    c.pill(MX0 + 70, MY0 + 6, "shop.example / checkout", DIM, size=11, weight="medium", a=a, h=19)
    # product
    c.rect(60, 185, 240, 320, r=10, fill=mix(WHITE, VIOLET, 0.10), a=a)
    icon(c, "tag", 150, 252, VIOLET, size=30, a=a)
    c.text(255, 192, "Trail Runner 2", 15, "bold", INK, a=a)
    c.text(255, 216, "$49.00", 14, "demi", MUTED, a=a)
    c.rect(255, 240, 400, 248, r=4, fill=LINE, a=a)
    c.rect(*ADD, r=8, fill=INK, a=a)
    c.text((ADD[0] + ADD[2]) / 2, (ADD[1] + ADD[3]) / 2, "Add to cart", 12.5, "demi", WHITE, anchor="mm", a=a)
    # promo + apply
    fixed = "r3" in seen
    c.text(60, 326, "Promo code", 11.5, "demi", DIM, anchor="lm", a=a)
    c.rect(*PROMO, r=8, fill=WHITE, outline=GREEN if fixed else LINE, width=1.4, a=a)
    c.text(72, 354, "SPRING15", 12.5, "medium", INK, anchor="lm", a=a)
    col = GREEN if fixed else mix(LINE, DIM, 0.4)
    c.rect(*APPLY, r=8, fill=col, a=a)
    c.text((APPLY[0] + APPLY[2]) / 2, 354, "Applied" if fixed else "Apply", 12.5, "demi", WHITE, anchor="mm", a=a)
    c.rect(*CHECKOUT, r=9, fill=CYAN, a=a)
    c.text(240, 410, "Checkout  ·  card ending ••••", 12.5, "demi", WHITE, anchor="mm", a=a)
    for k, w in enumerate([300, 220, 260]):
        c.rect(60, 446 + k * 14, 60 + w, 452 + k * 14, r=3, fill=mix(WHITE, LINE, 0.7), a=a)

    # ambient cursor wandering until the fix
    if not fixed or act == "r3":
        ph = t * 0.9
        cx = 250 + 130 * math.sin(ph) * math.cos(ph * 0.4)
        cy = 320 + 70 * math.sin(ph * 1.7)
        c.circle(cx, cy, 6, fill=INK, outline=WHITE, width=2, a=a)

    # 1 capture: masking shield
    if "r0" in seen:
        k = ease_out(u) if act == "r0" else 1.0
        c.rect(330, 438, 420, 460, r=6, fill=TEAL, a=a * 0.92 * k)
        c.text(375, 449, "masked", 11.5, "demi", WHITE, anchor="mm", a=a * k)
    # 2 observe: heatmap blobs + rage ripples
    if "r1" in seen and not fixed:
        k = ease_out(u * 2) if act == "r1" else 1.0
        c.soft_dot(364, 354, 44, RED, a=0.55 * k)
        c.soft_dot(337, 278, 34, AMBER, a=0.45 * k)
        c.soft_dot(150, 252, 30, AMBER, a=0.30 * k)
        c.soft_dot(240, 410, 24, BLUE, a=0.25 * k)
        for j in range(3):
            p = ((t * 1.4) + j / 3) % 1
            c.circle(364, 354, 8 + 34 * p, outline=RED, width=2, a=(1 - p) * 0.8 * k)
        c.pill(318, 300, "rage ×7", RED, size=11, solid=True, a=k, h=20)
    if "r1" in seen and act == "r1":
        c.pill(MX0 + 12, MY1 - 30, "JS error: promo.js:42", RED, size=11, a=ease_out(u * 2), h=20)
    # 3 ask why: exit survey popup
    if act == "r2":
        k = back_out(min(1, u * 2.5))
        x0, y0, x1, y1 = 110, 190 + (1 - k) * 20, 420, 330 + (1 - k) * 20
        c.rect(x0 + 3, y0 + 5, x1 + 3, y1 + 6, r=12, fill=(15, 23, 42), a=0.12 * k)
        c.rect(x0, y0, x1, y1, r=12, fill=WHITE, outline=AMBER, width=1.6, a=k)
        c.text(x0 + 16, y0 + 22, "What stopped you today?", 13, "bold", INK, anchor="lm", a=k)
        c.text(x1 - 14, y0 + 22, "Hotjar", 10.5, "demi", AMBER, anchor="rm", a=k)
        for j, (lab, v) in enumerate([("Code didn't apply", 0.41), ("Shipping cost", 0.22), ("Just browsing", 0.18)]):
            yy = y0 + 48 + j * 28
            g = ease_out(clamp(u * 2 - 0.3 - j * 0.1))
            c.text(x0 + 16, yy + 8, lab, 11.5, "medium", MUTED, anchor="lm", a=k)
            c.rect(x0 + 140, yy + 2, x0 + 140 + 120 * v / 0.41 * g, yy + 14, r=5, fill=AMBER, a=k)
            c.text(x0 + 148 + 120 * v / 0.41 * g, yy + 8, f"{int(v * 100 * g)}%", 11, "demi", INK, anchor="lm", a=k * g)
    # 4 fix: conversion ticker
    if fixed:
        k = ease_out(u) if act == "r3" else 1.0
        v = 2.1 + 0.5 * k
        c.rect(70, 192, 230, 242, r=10, fill=WHITE, outline=GREEN, width=1.6, a=a)
        c.text(82, 206, "Mobile conv. rate", 10.5, "demi", DIM, anchor="lm", a=a)
        c.text(82, 227, f"{v:.1f}%", 17, "bold", GREEN, anchor="lm", a=a)
        c.text(220, 227, f"+{v - 2.1:.1f} pt", 11.5, "demi", GREEN, anchor="rm", a=a)


def under(c, t, state):
    act = state["act"]
    mock(c, t, state)
    # orchestrator bar
    a = window(t, APPEAR["orch"], APPEAR["orch"] + 0.45)
    on = state["amt"] if act == "orch" else 0.0
    if a > 0.01:
        if on:
            c.glow(*ORCH, CYAN, 0.7 * on)
        c.rect(*ORCH, r=12, fill=mix(WHITE, CYAN, 0.08 + 0.08 * on), outline=CYAN, width=1.4, a=a)
        c.circle(ORCH[0] + 26, 165, 14, fill=mix(WHITE, CYAN, 0.18), a=a)
        icon(c, "spark", ORCH[0] + 26, 165, CYAN, size=14, a=a)
        c.text(ORCH[0] + 50, 165, "ba-orchestrator", 15, "bold", INK, anchor="lm", a=a)
        c.text(ORCH[0] + 190, 165, "finds the biggest friction point · ranks every fix", 12.5, "medium", MUTED,
               anchor="lm", a=a)
    # lanes
    for i, (lab, tool, col, agents) in enumerate(LANES):
        key = f"r{i}"
        a = window(t, APPEAR[key], APPEAR[key] + 0.5)
        if a <= 0.01:
            continue
        y0, y1 = LY[i], LY[i] + LH
        on = state["amt"] if act == key else 0.0
        done = key in seen and act != key
        if on:
            c.glow(LX0, y0, LX1, y1, col, 0.7 * on)
        c.rect(LX0, y0, LX1, y1, r=12, fill=mix(BG, col, 0.07 + 0.06 * on), outline=mix(BG, col, 0.5), width=1.2, a=a)
        c.rect(LX0, y0, LX0 + 6, y1, r=3, fill=col, a=a)
        c.text(LX0 + 20, y0 + 20, lab.upper(), 12, "bold", col, anchor="lm", a=a)
        c.text(LX0 + 20, y0 + 40, tool, 11.5, "medium", DIM, anchor="lm", a=a)
        if done:
            c.circle(LX0 + 150, y0 + 20, 8, fill=col, a=a)
            icon(c, "check", LX0 + 150, y0 + 20, WHITE, size=9, a=a)
        n = len(agents)
        cx0, cw, gap = 640, (LX1 - 10 - 640 - 8 * (n - 1)) / n, 8
        for j, ag in enumerate(agents):
            x = cx0 + j * (cw + gap)
            chip(c, x, y0 + 9, x + cw, y1 - 9, ag, None, col,
                 window(t, APPEAR[key] + 0.1 + j * 0.06, APPEAR[key] + 0.5 + j * 0.06), on, 12.5)
    # outputs
    section_label(c, OX0, 204, "You approve", a=window(t, APPEAR["out"], APPEAR["out"] + 0.4))
    for i, (lab, ic) in enumerate(OUTS):
        on = state["amt"] if act == "out" else 0.0
        chip(c, OX0, OY[i], OX1, OY[i] + 44, lab, ic, GREEN,
             window(t, APPEAR["out"] + i * 0.08, APPEAR["out"] + 0.4 + i * 0.08), on, 12.5)
    a = window(t, APPEAR["out"] + 0.3, APPEAR["out"] + 0.7)
    c.text((OX0 + OX1) / 2, 400, "weekly", 12, "bold", CYAN, anchor="mm", a=a)
    c.text((OX0 + OX1) / 2, 416, "loop", 12, "bold", CYAN, anchor="mm", a=a)
    # guardrails band
    a = window(t, APPEAR["band"], APPEAR["band"] + 0.5)
    band(c, 40, 516, 1240, 632, "Guardrails in every agent", CYAN, a)
    x = 60
    for r in RULES:
        x += c.pill(x, 542, r, CYAN, size=12.5, weight="demi", a=a, h=28) + 10
    x = 60
    for lab, col in [("Clarity shows what", BLUE), ("Hotjar asks why", AMBER), ("GA4 · Microsoft Ads", GREEN),
                     ("12 agents · drafts only", VIOLET)]:
        x += c.pill(x, 584, lab, col, size=12.5, weight="demi", a=a, h=28) + 10


def lane_xy(i):
    return (850, LY[i] + LH)


SC = [
    Scenario("Weekly check", "A live page, four lanes of agents, one ranked fix list", CYAN, [
        Step(None, "site", 0, 1.4, "Live visitors", "1,240 sessions/day · mobile checkout −12%", CYAN,
             side="bottom", callout_xy=(240, MY1)),
        Step("site>orch", "orch", 0.45, 1.2, "Orchestrator", "Biggest leak: mobile checkout step", CYAN,
             side="bottom", callout_xy=(775, 190)),
        Step("orch>r0", "r0", 0.35, 1.2, "Capture", "Both tools firing · card fields masked", TEAL,
             side="bottom", callout_xy=lane_xy(0)),
        Step("r0>r1", "r1", 0.35, 1.9, "Observe what", "Rage clicks on Apply · JS error in promo.js", BLUE,
             side="bottom", callout_xy=lane_xy(1)),
        Step("r1>r2", "r2", 0.35, 2.0, "Ask why", "41% say \"my code didn't apply\"", AMBER,
             side="bottom", callout_xy=lane_xy(2)),
        Step("r2>r3", "r3", 0.35, 1.8, "Fix + prove", "Promo bug fixed · conv. 2.1% → 2.6%", PINK,
             side="top", callout_xy=(850, LY[3])),
        Step("r3>out", "out", 0.45, 1.7, "Your call", "3 ranked fixes · tests drafted", GREEN,
             side="bottom", callout_xy=(1170, OY[2] + 44)),
    ], label=""),
]

if __name__ == "__main__":
    run_scene(out=OUT, accent=CYAN, kicker="BEHAVIOUR ANALYTICS AGENTS",
              title="See what visitors do, ask them why, fix it",
              sub="Live page → orchestrator → capture → observe (Clarity) → ask why (Hotjar) → fix + prove",
              right=[("12 agents", AMBER), ("Clarity · Hotjar", GREEN), ("You approve", BLUE)],
              nodes={}, links=L, appear=APPEAR, scenarios=SC, build_end=2.8, under=under,
              dash_links=("out>orch",),
              build_caption=("WORKFLOW", "A live page on the left, the agent team in four lanes on the right", CYAN),
              outro_caption=("YOU APPROVE", "Drafts only · masking stays on · you ship the fixes", CYAN))
