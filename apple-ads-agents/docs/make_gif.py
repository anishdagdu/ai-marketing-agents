"""Renders apple-ads-workflow.gif: the Apple Ads agents, animated.

Layout: an iPhone App Store search on the left reacts as the team works (attribution
badge, keywords, winning both ad slots, falling cost per install), while the agents sit
in four stacked lanes on the right and a token drops down through them.

Run: python3 apple-ads-agents/docs/make_gif.py  (needs Pillow and tools/gifkit.py)
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from gifkit import *  # noqa: E402,F403

OUT = os.path.join(HERE, "..", "apple-ads-workflow.gif")

# ---- iPhone App Store search (left)
PX0, PY0, PX1, PY1 = 90, 132, 390, 506
MX1, MY1 = PX1, PY1

# ---- lanes (right)
LX0, LX1 = 470, 1080
ORCH = (LX0, 140, LX1, 190)
LANES = [
    ("1 · Measure", "AdServices + MMP", TEAL, ["Attribution", "Account setup"]),
    ("2 · Discover", "Search Popularity", BLUE, ["Keywords", "Search Match"]),
    ("3 · Win the search", "App Store · News · Maps", AMBER, ["Brand", "Competitors", "Custom pages", "News + Maps"]),
    ("4 · Optimise + prove", "Apple Ads + MMP", PINK, ["Bids", "Lift tests", "Countries", "Report"]),
]
LY = [210 + i * 78 for i in range(4)]
LH = 58
OX0, OX1 = 1100, 1240
OUTS = [("Action list", "check"), ("Paused drafts", "flask"), ("Readout", "doc")]
OY = [226 + i * 52 for i in range(3)]

L = {
    "site>orch": (Path(curve((PX1, 300), (LX0, 165))), CYAN),
    "orch>r0": (Path(poly((540, ORCH[3]), (540, LY[0]))), TEAL),
}
for i in range(3):
    L[f"r{i}>r{i+1}"] = (Path(poly((540, LY[i] + LH), (540, LY[i + 1]))), LANES[i + 1][2])
L["r3>out"] = (Path(curve((LX1, LY[3] + LH / 2), (OX0, OY[2] + 22))), GREEN)
L["out>orch"] = (Path(poly(((OX0 + OX1) / 2, OY[0]), ((OX0 + OX1) / 2, 165), (LX1 + 2, 165))), CYAN)

APPEAR = {"site": 0.15, "orch": 0.5, "out": 1.9, "band": 2.2}
APPEAR.update({f"r{i}": 0.85 + 0.22 * i for i in range(4)})

RULES = ["Every change needs your OK", "New campaigns start paused", "Bids move ≤20% a step",
         "Never touches billing", "Never deletes, only pauses"]
seen = set()


def mock(c, t, state):
    a = window(t, APPEAR["site"], APPEAR["site"] + 0.5)
    if a <= 0.01:
        return
    act, st = state["act"], state["st"]
    u = st["u"] if st and st["phase"] == "dwell" else 0.0
    if act:
        seen.add(act)
    # phone frame
    c.rect(PX0 + 3, PY0 + 5, PX1 + 3, PY1 + 7, r=34, fill=(15, 23, 42), a=a * 0.08)
    c.rect(PX0, PY0, PX1, PY1, r=34, fill=INK, a=a)
    c.rect(PX0 + 8, PY0 + 8, PX1 - 8, PY1 - 8, r=28, fill=WHITE, a=a)
    c.rect((PX0 + PX1) / 2 - 36, PY0 + 16, (PX0 + PX1) / 2 + 36, PY0 + 30, r=7, fill=INK, a=a)
    # search bar
    c.rect(PX0 + 22, PY0 + 44, PX1 - 22, PY0 + 74, r=10, fill=mix(BG, LINE, 0.5), a=a)
    icon(c, "search", PX0 + 38, PY0 + 59, DIM, size=12, a=a)
    q = "budget app"[: max(0, min(10, int((t - 0.3) * 8)))]
    c.text(PX0 + 52, PY0 + 59, q, 12.5, "medium", INK, anchor="lm", a=a)
    won = "r2" in seen
    fixed = "r3" in seen
    # result rows: ad slot 1, ad slot 2, organic
    rows = [("Ad", "Pennywise" if won else "RivalBudget", VIOLET if won else RED),
            ("Ad", "Pennywise · Track bills" if won else "Pennywise", VIOLET),
            ("", "Other app", DIM)]
    for k, (tag, name, col) in enumerate(rows):
        y = PY0 + 88 + k * 66
        hi = won and k < 2
        c.rect(PX0 + 18, y, PX1 - 18, y + 58, r=12, fill=mix(WHITE, col, 0.07 if hi else 0.02),
               outline=col if hi else LINE, width=1.4 if hi else 1.0, a=a)
        c.rect(PX0 + 28, y + 10, PX0 + 72, y + 50, r=11, fill=mix(WHITE, col, 0.25), a=a)
        icon(c, "chart" if col != RED else "x", PX0 + 50, y + 29, col, size=16, a=a)
        c.text(PX0 + 82, y + 19, name, 12.5, "bold", INK, anchor="lm", a=a)
        if tag:
            c.pill(PX0 + 82, y + 30, tag, CYAN, size=10, solid=True, a=a, h=17)
        c.rect(PX1 - 78, y + 17, PX1 - 30, y + 41, r=12, fill=CYAN, a=a)
        c.text(PX1 - 54, y + 29, "Get", 11.5, "demi", WHITE, anchor="mm", a=a)
    # 1 measure: attribution badge
    if "r0" in seen:
        k = ease_out(u) if act == "r0" else 1.0
        c.pill(PX0 + 22, PY1 - 84, "AdServices + MMP matched", TEAL, size=11, solid=True, a=a * k, h=22)
    # 2 discover: keyword chips float up
    if act == "r1":
        for j, kw in enumerate(["budget app", "bill tracker", "save money"]):
            g = ease_out(clamp(u * 2 - j * 0.2))
            c.pill(PX0 + 30 + j * 4, PY0 + 330 - j * 26 - g * 10, kw, BLUE, size=11, a=g, h=20)
    # 3 win: stamp on brand slots
    if act == "r2":
        k = back_out(min(1, u * 2.5))
        c.pill(PX1 - 150, PY0 + 80, "both ad slots", AMBER, size=11, solid=True, a=k, h=20)
    # 4 optimise: CPI ticker
    if fixed:
        k = ease_out(u) if act == "r3" else 1.0
        v = 3.40 - 1.10 * k
        c.rect(PX0 + 22, PY1 - 56, PX1 - 22, PY1 - 20, r=10, fill=WHITE, outline=GREEN, width=1.6, a=a)
        c.text(PX0 + 34, PY1 - 38, "Cost per install", 10.5, "demi", DIM, anchor="lm", a=a)
        c.text(PX1 - 34, PY1 - 38, f"${v:.2f}", 15, "bold", GREEN, anchor="rm", a=a)


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
        c.text(ORCH[0] + 50, 165, "aa-orchestrator", 15, "bold", INK, anchor="lm", a=a)
        c.text(ORCH[0] + 190, 165, "finds the biggest gap · JEV picks the model per task", 12.5, "medium", MUTED,
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
    for lab, col in [("JEV: Haiku · Sonnet · Opus", BLUE), ("App Store · Apple News · Apple Maps", AMBER),
                     ("AdServices · MMP", GREEN), ("14 agents", VIOLET)]:
        x += c.pill(x, 584, lab, col, size=12.5, weight="demi", a=a, h=28) + 10


def lane_xy(i):
    return (850, LY[i] + LH)


SC = [
    Scenario("Weekly check", "An App Store search, four lanes of agents, one ranked action list", CYAN, [
        Step(None, "site", 0, 1.4, "App Store search", "Rival ad sits above your brand", CYAN,
             side="bottom", callout_xy=(240, PY1)),
        Step("site>orch", "orch", 0.45, 1.2, "Orchestrator + JEV", "Brand leak first · 9 tasks routed", CYAN,
             side="bottom", callout_xy=(775, 190)),
        Step("orch>r0", "r0", 0.35, 1.2, "Measure", "AdServices and MMP agree within 4%", TEAL,
             side="bottom", callout_xy=lane_xy(0)),
        Step("r0>r1", "r1", 0.35, 1.7, "Discover", "38 new exact keywords · 120 negatives", BLUE,
             side="bottom", callout_xy=lane_xy(1)),
        Step("r1>r2", "r2", 0.35, 1.9, "Win the search", "Both ad slots won · News + Maps planned", AMBER,
             side="bottom", callout_xy=lane_xy(2)),
        Step("r2>r3", "r3", 0.35, 1.8, "Optimise + prove", "CPI $3.40 → $2.30 · brand lift test", PINK,
             side="top", callout_xy=(850, LY[3])),
        Step("r3>out", "out", 0.45, 1.7, "Your call", "5 changes waiting · new ones paused", GREEN,
             side="bottom", callout_xy=(1170, OY[2] + 44)),
    ], label=""),
]

if __name__ == "__main__":
    run_scene(out=OUT, accent=CYAN, kicker="APPLE ADS AGENTS",
              title="Win on the App Store, Apple News and Apple Maps",
              sub="App Store search → orchestrator + JEV → measure → discover → win the search → optimise + prove",
              right=[("14 agents", AMBER), ("JEV router", GREEN), ("You approve", BLUE)],
              nodes={}, links=L, appear=APPEAR, scenarios=SC, build_end=2.8, under=under,
              dash_links=("out>orch",),
              build_caption=("WORKFLOW", "An App Store search on the left, the agent team in four lanes on the right", CYAN),
              outro_caption=("YOU APPROVE", "Paused drafts · capped bids · you switch them on", CYAN))
