"""Renders microsoft-ads-workflow.gif: the Microsoft Ads agents, animated.

Layout: a desktop Bing results page on the left reacts as the team works (UET and
import badge, winning the ad slots with LinkedIn targeting, a Copilot answer with an
ad, falling cost per lead), while the agents sit in four stacked lanes on the right
and a token drops down through them. The JEV model router is part of the workflow
but is deliberately not drawn here.

Run: python3 microsoft-ads-agents/docs/make_gif.py  (needs Pillow and tools/gifkit.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from gifkit import *  # noqa: E402,F403

OUT = os.path.join(HERE, "..", "microsoft-ads-workflow.gif")

# ---- desktop browser with Bing results (left)
PX0, PY0, PX1, PY1 = 40, 140, 440, 500

# ---- lanes (right)
LX0, LX1 = 480, 1080
ORCH = (LX0, 140, LX1, 190)
LANES = [
    ("1 · Import + measure", "Google Import · UET", TEAL, ["Import + tracking"]),
    ("2 · Win search", "Bing · Yahoo · DuckDuckGo", BLUE, ["Search", "LinkedIn B2B"]),
    ("3 · Expand reach", "Copilot · MSN · Shopping", VIOLET, ["Copilot", "Audience Network", "Shopping + PMax"]),
    ("4 · Optimise + prove", "Microsoft vs Google", AMBER, ["Bids, budgets + weekly readout"]),
]
LY = [210 + i * 78 for i in range(4)]
LH = 58
OX0, OX1 = 1100, 1240
OUTS = [("Action list", "check"), ("Paused drafts", "flask"), ("Readout", "doc")]
OY = [226 + i * 52 for i in range(3)]

L = {
    "site>orch": (Path(curve((PX1, 300), (LX0, 165))), BLUE),
    "orch>r0": (Path(poly((550, ORCH[3]), (550, LY[0]))), TEAL),
}
for i in range(3):
    L[f"r{i}>r{i+1}"] = (Path(poly((550, LY[i] + LH), (550, LY[i + 1]))), LANES[i + 1][2])
L["r3>out"] = (Path(curve((LX1, LY[3] + LH / 2), (OX0, OY[2] + 22))), GREEN)
L["out>orch"] = (Path(poly(((OX0 + OX1) / 2, OY[0]), ((OX0 + OX1) / 2, 165), (LX1 + 2, 165))), BLUE)

APPEAR = {"site": 0.15, "orch": 0.5, "out": 1.9, "band": 2.2}
APPEAR.update({f"r{i}": 0.85 + 0.22 * i for i in range(4)})

RULES = ["Every change needs your OK", "Imports start paused", "Bids move ≤20% a step",
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
    # browser window
    c.rect(PX0 + 3, PY0 + 5, PX1 + 3, PY1 + 7, r=14, fill=(15, 23, 42), a=a * 0.08)
    c.rect(PX0, PY0, PX1, PY1, r=14, fill=WHITE, outline=LINE, width=1.2, a=a)
    c.rect(PX0, PY0, PX1, PY0 + 34, r=14, fill=mix(BG, LINE, 0.45), a=a)
    c.rect(PX0, PY0 + 20, PX1, PY0 + 34, r=0, fill=mix(BG, LINE, 0.45), a=a)
    for k, col in enumerate([RED, AMBER, GREEN]):
        c.circle(PX0 + 18 + k * 16, PY0 + 17, 5, fill=col, a=a)
    c.rect(PX0 + 70, PY0 + 7, PX1 - 14, PY0 + 27, r=10, fill=WHITE, a=a)
    q = "crm software for sales teams"[: max(0, min(28, int((t - 0.3) * 14)))]
    c.text(PX0 + 82, PY0 + 17, "bing.com  " + q, 10.5, "medium", DIM, anchor="lm", a=a)
    # search bar row
    c.text(PX0 + 20, PY0 + 56, "Bing", 15, "bold", CYAN, anchor="lm", a=a)
    c.rect(PX0 + 66, PY0 + 44, PX1 - 20, PY0 + 68, r=12, fill=WHITE, outline=LINE, width=1.0, a=a)
    icon(c, "search", PX0 + 80, PY0 + 56, DIM, size=11, a=a)
    c.text(PX0 + 92, PY0 + 56, q, 11, "medium", INK, anchor="lm", a=a)

    won = "r1" in seen
    reach = "r2" in seen
    y = PY0 + 80
    # 3 expand reach: Copilot answer slides in above results
    if reach:
        k = ease_out(u) if act == "r2" else 1.0
        h = 64 * k
        c.rect(PX0 + 16, y, PX1 - 16, y + h, r=10, fill=mix(WHITE, VIOLET, 0.07), outline=VIOLET, width=1.2, a=a * k)
        if k > 0.6:
            icon(c, "spark", PX0 + 32, y + 18, VIOLET, size=13, a=a)
            c.text(PX0 + 46, y + 18, "Copilot answer", 11.5, "bold", VIOLET, anchor="lm", a=a)
            c.text(PX0 + 30, y + 40, "Top picks for sales teams: YourCRM ...", 10.5, "medium", MUTED, anchor="lm", a=a)
            c.pill(PX1 - 92, y + 9, "Sponsored", VIOLET, size=9.5, solid=True, a=a, h=17)
        y += h + 8
    # ad rows
    rows = [("RivalCRM · Free trial" if not won else "YourCRM · Built for Sales VPs", RED if not won else BLUE),
            ("YourCRM · Pricing", BLUE),
            ("Organic result", DIM)]
    if reach:
        rows = rows[:2]
    for k, (title, col) in enumerate(rows):
        hi = won and k < 2
        c.rect(PX0 + 16, y, PX1 - 16, y + 52, r=10, fill=mix(WHITE, col, 0.06 if hi else 0.015),
               outline=col if hi else LINE, width=1.4 if hi else 1.0, a=a)
        if k < 2:
            c.pill(PX0 + 26, y + 8, "Ad", CYAN, size=9.5, solid=True, a=a, h=16)
        c.text(PX0 + (64 if k < 2 else 28), y + 16, title, 12, "bold", col if col != DIM else INK, anchor="lm", a=a)
        c.rect(PX0 + 28, y + 32, PX1 - 90 - k * 30, y + 38, r=3, fill=mix(WHITE, LINE, 0.8), a=a)
        y += 60
    # 1 measure: badge
    if "r0" in seen:
        k = ease_out(u) if act == "r0" else 1.0
        c.pill(PX0 + 20, PY1 - 84, "UET + Google Import synced", TEAL, size=11, solid=True, a=a * k, h=22)
    # 2 win: LinkedIn badge stamp
    if act == "r1":
        k = back_out(min(1, u * 2.5))
        c.pill(PX1 - 178, PY0 + 84, "LinkedIn: Sales VPs", BLUE, size=11, solid=True, a=k, h=20)
    # 4 optimise: cost per lead ticker
    if "r3" in seen:
        k = ease_out(u) if act == "r3" else 1.0
        v = 84 - 32 * k
        c.rect(PX0 + 20, PY1 - 56, PX1 - 20, PY1 - 18, r=10, fill=WHITE, outline=GREEN, width=1.6, a=a)
        c.text(PX0 + 32, PY1 - 37, "Cost per qualified lead", 10.5, "demi", DIM, anchor="lm", a=a)
        c.text(PX1 - 32, PY1 - 37, f"${v:.0f}", 15, "bold", GREEN, anchor="rm", a=a)


def under(c, t, state):
    act = state["act"]
    mock(c, t, state)
    a = window(t, APPEAR["orch"], APPEAR["orch"] + 0.45)
    on = state["amt"] if act == "orch" else 0.0
    if a > 0.01:
        if on:
            c.glow(*ORCH, BLUE, 0.7 * on)
        c.rect(*ORCH, r=12, fill=mix(WHITE, BLUE, 0.08 + 0.08 * on), outline=BLUE, width=1.4, a=a)
        c.circle(ORCH[0] + 26, 165, 14, fill=mix(WHITE, BLUE, 0.18), a=a)
        icon(c, "route", ORCH[0] + 26, 165, BLUE, size=14, a=a)
        c.text(ORCH[0] + 50, 165, "ms-orchestrator", 15, "bold", INK, anchor="lm", a=a)
        c.text(ORCH[0] + 190, 165, "finds the biggest gap · sends work down four lanes", 12.5, "medium", MUTED,
               anchor="lm", a=a)
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
            c.circle(LX0 + 176, y0 + 20, 8, fill=col, a=a)
            icon(c, "check", LX0 + 176, y0 + 20, WHITE, size=9, a=a)
        n = len(agents)
        cx0, gap = 668, 8
        cw = (LX1 - 10 - cx0 - gap * (n - 1)) / n
        for j, ag in enumerate(agents):
            x = cx0 + j * (cw + gap)
            chip(c, x, y0 + 9, x + cw, y1 - 9, ag, None, col,
                 window(t, APPEAR[key] + 0.1 + j * 0.06, APPEAR[key] + 0.5 + j * 0.06), on, 12.5)
    section_label(c, OX0, 204, "You approve", a=window(t, APPEAR["out"], APPEAR["out"] + 0.4))
    for i, (lab, ic) in enumerate(OUTS):
        on = state["amt"] if act == "out" else 0.0
        chip(c, OX0, OY[i], OX1, OY[i] + 44, lab, ic, GREEN,
             window(t, APPEAR["out"] + i * 0.08, APPEAR["out"] + 0.4 + i * 0.08), on, 12.5)
    a = window(t, APPEAR["out"] + 0.3, APPEAR["out"] + 0.7)
    c.text((OX0 + OX1) / 2, 400, "weekly", 12, "bold", BLUE, anchor="mm", a=a)
    c.text((OX0 + OX1) / 2, 416, "loop", 12, "bold", BLUE, anchor="mm", a=a)
    a = window(t, APPEAR["band"], APPEAR["band"] + 0.5)
    band(c, 40, 516, 1240, 632, "Guardrails in every agent", BLUE, a)
    x = 60
    for r in RULES:
        x += c.pill(x, 542, r, BLUE, size=12.5, weight="demi", a=a, h=28) + 10
    x = 60
    for lab, col in [("Bing · Copilot · Audience Network", VIOLET), ("LinkedIn profile targeting", BLUE),
                     ("UET · Clarity · CRM", GREEN), ("8 agents", AMBER)]:
        x += c.pill(x, 584, lab, col, size=12.5, weight="demi", a=a, h=28) + 10


def lane_xy(i):
    return (870, LY[i] + LH)


SC = [
    Scenario("Weekly check", "A Bing results page, four lanes of agents, one ranked action list", BLUE, [
        Step(None, "site", 0, 1.4, "Bing search", "A rival's ad sits above your brand", BLUE,
             side="bottom", callout_xy=(240, PY1)),
        Step("site>orch", "orch", 0.45, 1.2, "Orchestrator", "UET first, then B2B search · 7 tasks", BLUE,
             side="bottom", callout_xy=(780, 190)),
        Step("orch>r0", "r0", 0.35, 1.2, "Import + measure", "12 Google campaigns in, paused · UET matches CRM", TEAL,
             side="bottom", callout_xy=lane_xy(0)),
        Step("r0>r1", "r1", 0.35, 1.8, "Win search", "CPC 38% below Google · VP Sales bid +20%", BLUE,
             side="bottom", callout_xy=lane_xy(1)),
        Step("r1>r2", "r2", 0.35, 1.9, "Expand reach", "Copilot test live · MSN retargeting · Shopping feed", VIOLET,
             side="bottom", callout_xy=lane_xy(2)),
        Step("r2>r3", "r3", 0.35, 1.8, "Optimise + prove", "Cost per lead $84 → $52 · geo lift test", AMBER,
             side="top", callout_xy=(870, LY[3])),
        Step("r3>out", "out", 0.45, 1.7, "Your call", "6 changes waiting · new ones paused", GREEN,
             side="bottom", callout_xy=(1170, OY[2] + 44)),
    ], label=""),
]

if __name__ == "__main__":
    run_scene(out=OUT, accent=BLUE, kicker="MICROSOFT ADS AGENTS",
              title="Win on Bing, Copilot and the Microsoft Audience Network",
              sub="Bing search → orchestrator → import + measure → win search → expand reach → optimise + prove",
              right=[("8 agents", AMBER), ("LinkedIn data", BLUE), ("You approve", GREEN)],
              nodes={}, links=L, appear=APPEAR, scenarios=SC, build_end=2.8, under=under,
              dash_links=("out>orch",),
              build_caption=("WORKFLOW", "A Bing results page on the left, the agent team in four lanes on the right", BLUE),
              outro_caption=("YOU APPROVE", "Paused drafts · capped bids · you switch them on", BLUE))
