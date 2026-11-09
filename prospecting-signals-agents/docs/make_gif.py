"""Renders prospecting-signals-workflow.gif: the Clay / Common Room / Apollo agents, animated.

Layout: a Clay-style account table on the left fills in column by column as the team works
(accounts, verified emails, signals, scores, a draft email), while JEV sits beside the
orchestrator and the agents run in five lanes on the right. Replies loop back to scoring.

Run: python3 prospecting-signals-agents/docs/make_gif.py  (needs Pillow and tools/gifkit.py)
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from gifkit import *  # noqa: E402,F403

OUT = os.path.join(HERE, "..", "prospecting-signals-workflow.gif")

MX0, MY0, MX1, MY1 = 40, 140, 440, 500
LX0, LX1 = 470, 1080
ORCH = (LX0, 140, 810, 190)
JEV = (826, 140, LX1, 190)
LANES = [
    ("1 · Target", "Apollo · Clay", BLUE, ["ICP + lookalikes", "List builder", "Buying committee"]),
    ("2 · Enrich", "Clay waterfall", TEAL, ["Email waterfall", "Enrichment", "AI researcher"]),
    ("3 · Signals", "Common Room", AMBER, ["Intent", "Community", "Triggers"]),
    ("4 · Score", "Fit × intent", VIOLET, ["Lead scorer", "Routing"]),
    ("5 · Engage", "Drafts only", PINK, ["CRM sync", "Outreach writer"]),
]
TIERS = ["sonnet", "haiku", "sonnet", "sonnet", "sonnet"]
NL = len(LANES)
LY = [206 + i * 60 for i in range(NL)]
LH = 50
OX0, OX1 = 1100, 1240
OUTS = [("Ranked accounts", "chart"), ("Draft outreach", "mail"), ("CRM updates", "db")]
OY = [226 + i * 52 for i in range(3)]

L = {
    "site>orch": (Path(curve((MX1, 300), (LX0, 165))), CYAN),
    "orch>jev": (Path(poly((ORCH[2], 165), (JEV[0], 165))), VIOLET),
    "jev>r0": (Path(poly(((JEV[0] + JEV[2]) / 2, JEV[3]), ((JEV[0] + JEV[2]) / 2, 198), (540, 198), (540, LY[0]))), BLUE),
}
for i in range(NL - 1):
    L[f"r{i}>r{i+1}"] = (Path(poly((540, LY[i] + LH), (540, LY[i + 1]))), LANES[i + 1][2])
L["r4>out"] = (Path(curve((LX1, LY[4] + LH / 2), (OX0, OY[2] + 22))), GREEN)
L["reply>r3"] = (Path(poly((LX0 + 4, LY[4] + LH / 2), (LX0 - 14, LY[4] + LH / 2), (LX0 - 14, LY[3] + LH / 2), (LX0 + 4, LY[3] + LH / 2))), PINK)
L["out>orch"] = (Path(poly(((OX0 + OX1) / 2, OY[0]), ((OX0 + OX1) / 2, 165), (LX1 + 2, 165))), CYAN)

APPEAR = {"site": 0.15, "orch": 0.5, "jev": 0.7, "out": 2.1, "band": 2.4}
APPEAR.update({f"r{i}": 0.95 + 0.2 * i for i in range(NL)})

ROWS = [("Northwind", "Maya R. · VP Sales", "Pricing ×3", RED, 92),
        ("Acme Cloud", "Leo K. · Head Growth", "Job change", AMBER, 81),
        ("Brightlane", "Ana P. · CMO", "Raised $20M", GREEN, 74),
        ("Kestrel IO", "Tom B. · RevOps", "Slack ×12", BLUE, 63),
        ("Fernway", "Ida S. · Founder", "—", DIM, 38)]
COLS = [56, 150, 284, 318, 414]
RULES = ["Nothing sent without your OK", "Drafts only", "Opt-outs + customers excluded",
         "Business data only", "Never deletes records"]
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
    c.pill(MX0 + 70, MY0 + 6, "Accounts table · Q4 pipeline", DIM, size=11, weight="medium", a=a, h=19)
    hy = 186
    for x, lab in zip(COLS, ["Company", "Contact", "Email", "Signal", "Score"]):
        c.text(x, hy, lab, 10.5, "bold", DIM, anchor="lm" if lab != "Score" else "mm", a=a)
    c.rect(52, hy + 12, 428, hy + 13, r=0, fill=LINE, a=a)
    for i, (co, ct, sig, scol, sc) in enumerate(ROWS):
        y = 220 + i * 46
        def k_of(key, d=0.0):
            if key not in seen:
                return 0.0
            return ease_out(clamp(u * 2.2 - i * 0.18 - d)) if act == key else 1.0
        k0, k1, k2, k3 = k_of("r0"), k_of("r1"), k_of("r2"), k_of("r3")
        top = "r3" in seen and i == 0
        if top:
            c.rect(50, y - 20, 430, y + 22, r=8, fill=mix(WHITE, VIOLET, 0.10), a=a * k3)
        if k0:
            c.text(COLS[0], y - 6, co, 12, "bold", INK, anchor="lm", a=a * k0)
            c.text(COLS[0], y + 10, ct, 10, "medium", MUTED, anchor="lm", a=a * k0)
        else:
            c.rect(COLS[0], y - 10, COLS[0] + 120, y, r=3, fill=mix(WHITE, LINE, 0.7), a=a)
        if k1:
            ok = i != 4
            c.circle(COLS[2] + 8, y, 8, fill=GREEN if ok else AMBER, a=a * k1)
            icon(c, "check" if ok else "x", COLS[2] + 8, y, WHITE, size=8, a=a * k1)
        if k2:
            c.pill(COLS[3] - 6, y - 10, sig, scol, size=10, weight="demi", a=a * k2, h=20)
        if k3:
            col = GREEN if sc >= 80 else AMBER if sc >= 60 else DIM
            c.circle(COLS[4], y, 15, fill=col, a=a * k3)
            c.text(COLS[4], y, str(int(sc * k3)), 11, "bold", WHITE, anchor="mm", a=a * k3)
    if "r1" in seen:
        k = ease_out(u * 2) if act == "r1" else 1.0
        c.pill(MX0 + 12, MY1 - 30, "4/5 verified · 0.6 credits each", TEAL, size=11, a=k * a, h=20)
    if act == "r4":
        k = back_out(min(1, u * 2.5))
        x0, y0, x1, y1 = 90, 250 + (1 - k) * 20, 430, 400 + (1 - k) * 20
        c.rect(x0 + 3, y0 + 5, x1 + 3, y1 + 6, r=12, fill=(15, 23, 42), a=0.12 * k)
        c.rect(x0, y0, x1, y1, r=12, fill=WHITE, outline=PINK, width=1.6, a=k)
        icon(c, "mail", x0 + 22, y0 + 22, PINK, size=14, a=k)
        c.text(x0 + 38, y0 + 22, "Draft · to Maya R.", 13, "bold", INK, anchor="lm", a=k)
        c.pill(x1 - 74, y0 + 11, "not sent", PINK, size=10, a=k, h=20)
        lines = ["Saw your team checked our pricing", "page three times this week, and", "you're hiring 4 AEs in Berlin.",
                 "Worth 15 min on ramping them faster?"]
        for j, ln in enumerate(lines):
            g = ease_out(clamp(u * 2.5 - 0.3 - j * 0.15))
            c.text(x0 + 18, y0 + 52 + j * 21, ln, 12, "medium", MUTED, anchor="lm", a=k * g)
    if "r4" in seen and act != "r4":
        c.pill(MX0 + 220, MY1 - 30, "2 replies → re-score", PINK, size=11, a=a, h=20)


def under(c, t, state):
    act = state["act"]
    mock(c, t, state)
    a = window(t, APPEAR["orch"], APPEAR["orch"] + 0.45)
    on = state["amt"] if act == "orch" else 0.0
    if a > 0.01:
        if on:
            c.glow(*ORCH, CYAN, 0.7 * on)
        c.rect(*ORCH, r=12, fill=mix(WHITE, CYAN, 0.08 + 0.08 * on), outline=CYAN, width=1.4, a=a)
        c.circle(ORCH[0] + 26, 165, 14, fill=mix(WHITE, CYAN, 0.18), a=a)
        icon(c, "spark", ORCH[0] + 26, 165, CYAN, size=14, a=a)
        c.text(ORCH[0] + 50, 165, "pr-orchestrator", 15, "bold", INK, anchor="lm", a=a)
        c.text(ORCH[0] + 186, 165, "play · budget · ranked list", 12, "medium", MUTED, anchor="lm", a=a)
    a = window(t, APPEAR["jev"], APPEAR["jev"] + 0.45)
    on = state["amt"] if act == "jev" else 0.0
    if a > 0.01:
        if on:
            c.glow(*JEV, VIOLET, 0.7 * on)
        c.rect(*JEV, r=12, fill=mix(WHITE, VIOLET, 0.08 + 0.08 * on), outline=VIOLET, width=1.4, a=a)
        c.text(JEV[0] + 14, 165, "JEV", 15, "bold", VIOLET, anchor="lm", a=a)
        x = JEV[0] + 56
        for lab, col in [("Haiku", TEAL), ("Sonnet", BLUE), ("Opus", PINK)]:
            x += c.pill(x, 154, lab, col, size=10.5, weight="demi", a=a, h=22) + 5
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
        c.text(LX0 + 20, y0 + 17, lab.upper(), 12, "bold", col, anchor="lm", a=a)
        c.text(LX0 + 20, y0 + 35, tool, 11, "medium", DIM, anchor="lm", a=a)
        c.text(LX0 + 158, y0 + 35, TIERS[i], 10, "demi", VIOLET, anchor="rm", a=a * 0.85)
        if done:
            c.circle(LX0 + 150, y0 + 17, 7, fill=col, a=a)
            icon(c, "check", LX0 + 150, y0 + 17, WHITE, size=8, a=a)
        n = len(agents)
        cx0, gap = 640, 6
        cw = (LX1 - 8 - cx0 - gap * (n - 1)) / n
        for j, ag in enumerate(agents):
            x = cx0 + j * (cw + gap)
            chip(c, x, y0 + 8, x + cw, y1 - 8, ag, None, col,
                 window(t, APPEAR[key] + 0.1 + j * 0.06, APPEAR[key] + 0.5 + j * 0.06), on, 12)
    section_label(c, OX0, 204, "You approve", a=window(t, APPEAR["out"], APPEAR["out"] + 0.4))
    for i, (lab, ic) in enumerate(OUTS):
        on = state["amt"] if act == "out" else 0.0
        chip(c, OX0, OY[i], OX1, OY[i] + 44, lab, ic, GREEN,
             window(t, APPEAR["out"] + i * 0.08, APPEAR["out"] + 0.4 + i * 0.08), on, 12)
    a = window(t, APPEAR["out"] + 0.3, APPEAR["out"] + 0.7)
    c.text((OX0 + OX1) / 2, 400, "weekly", 12, "bold", CYAN, anchor="mm", a=a)
    c.text((OX0 + OX1) / 2, 416, "loop", 12, "bold", CYAN, anchor="mm", a=a)
    a = window(t, APPEAR["band"], APPEAR["band"] + 0.5)
    band(c, 40, 516, 1240, 632, "Guardrails in every agent", CYAN, a)
    x = 60
    for r in RULES:
        x += c.pill(x, 542, r, CYAN, size=12.5, weight="demi", a=a, h=28) + 10
    x = 60
    for lab, col in [("Clay enriches", TEAL), ("Common Room signals", AMBER), ("Apollo finds + verifies", BLUE),
                     ("14 agents · JEV routing", VIOLET)]:
        x += c.pill(x, 584, lab, col, size=12.5, weight="demi", a=a, h=28) + 10


def lane_xy(i):
    return (850, LY[i] + LH)


SC = [
    Scenario("Weekly run", "Signals in, ranked accounts and draft outreach out", CYAN, [
        Step(None, "site", 0, 1.3, "Pipeline goal", "40 meetings this quarter · 2,000 credits", CYAN,
             side="bottom", callout_xy=(240, MY1)),
        Step("site>orch", "orch", 0.45, 1.1, "Orchestrator", "Play: new accounts + warm signals", CYAN,
             side="bottom", callout_xy=(640, 190)),
        Step("orch>jev", "jev", 0.3, 1.3, "JEV router", "Apollo first · Clay only for fit 70+", VIOLET,
             side="bottom", callout_xy=((JEV[0] + JEV[2]) / 2, 190)),
        Step("jev>r0", "r0", 0.35, 1.6, "Target", "ICP lookalikes · 5 accounts · buyers mapped", BLUE,
             side="bottom", callout_xy=lane_xy(0)),
        Step("r0>r1", "r1", 0.35, 1.6, "Enrich", "Waterfall: 4 of 5 emails verified", TEAL,
             side="bottom", callout_xy=lane_xy(1)),
        Step("r1>r2", "r2", 0.35, 1.8, "Signals", "Pricing visits · job change · funding", AMBER,
             side="bottom", callout_xy=lane_xy(2)),
        Step("r2>r3", "r3", 0.35, 1.6, "Score", "Northwind 92 · Acme 81 → reps assigned", VIOLET,
             side="top", callout_xy=(850, LY[3])),
        Step("r3>r4", "r4", 0.35, 2.0, "Engage", "CRM checked · first lines drafted, not sent", PINK,
             side="top", callout_xy=(850, LY[4])),
        Step("r4>out", "out", 0.45, 1.6, "Your call", "Approve, send · replies re-score", GREEN,
             side="bottom", callout_xy=(1170, OY[2] + 44)),
    ], label=""),
]

if __name__ == "__main__":
    run_scene(out=OUT, accent=CYAN, kicker="PROSPECTING & SIGNALS AGENTS",
              title="Find who to talk to, know why now, write the first line",
              sub="Goal → orchestrator → JEV → target → enrich (Clay) → signals (Common Room) → score → engage",
              right=[("14 agents", AMBER), ("Clay · Common Room · Apollo", GREEN), ("You approve", BLUE)],
              nodes={}, links=L, appear=APPEAR, scenarios=SC, build_end=3.0, under=under,
              dash_links=("out>orch", "reply>r3"),
              build_caption=("WORKFLOW", "An account table on the left, JEV routes the team through five lanes on the right", CYAN),
              outro_caption=("YOU APPROVE", "Drafts only · nothing sent or synced without your OK", CYAN))
