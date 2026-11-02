"""Renders programmatic-agents-workflow.gif: the 20 CM360 / DV360 / TTD agents, animated.

Story: the orchestrator finds the biggest leak, the JEV model router picks a model tier
for each task, a token travels through the five stages (measure first -> plan -> buy ->
optimise -> prove), each stage's agents light up with the tier JEV chose, and a ranked
action list comes out for you to approve.

Run: python3 programmatic-ads-agents/docs/make_gif.py  (needs Pillow and tools/gifkit.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from gifkit import *  # noqa: E402,F403

OUT = os.path.join(HERE, "..", "programmatic-agents-workflow.gif")

N = {
    "orch": Node("orch", 40, 140, 260, 290, "Orchestrator", "pg-orchestrator", BLUE, "spark", "LEAD",
                 lines=["Finds the biggest leak", "Ranks every action"]),
    "jev": Node("jev", 40, 318, 260, 470, "JEV router", "pg-jev-router", VIOLET, "shield", "MODEL",
                lines=["Fast · Haiku", "Standard · Sonnet", "Deep · Opus"]),
}

STAGES = [
    ("1 · Measure first", TEAL, ["Floodlight", "Verification", "CM360 trafficking"]),
    ("2 · Plan", BLUE, ["Media plan", "Audiences + UID2", "Deals + supply"]),
    ("3 · Buy", AMBER, ["DV360 buyer", "TTD buyer", "YouTube", "CTV · audio", "Retail media"]),
    ("4 · Optimise", PINK, ["Bidding", "Frequency", "Pacing", "Dynamic creative"]),
    ("5 · Prove", GREEN, ["Attribution", "Lift tests", "Clean room"]),
]
SX0, SW, SG, SY0, SY1 = 290, 144, 10, 140, 470
SX = [SX0 + i * (SW + SG) for i in range(5)]
OX0, OX1 = 1070, 1240
OUTS = [("Ranked actions", "check"), ("Weekly readout", "doc"), ("JEV cost log", "chart")]
OY = [200 + i * 54 for i in range(3)]

L = {
    "orch>jev": (Path(curve(N["orch"].B(-40), N["jev"].T(-40), "v")), VIOLET),
    "jev>s0": (Path(curve(N["jev"].R(-20), (SX[0], 250))), VIOLET),
}
for i in range(4):
    L[f"s{i}>s{i+1}"] = (Path(curve((SX[i] + SW, 300), (SX[i + 1], 300))), STAGES[i + 1][1])
L["s4>out"] = (Path(curve((SX[4] + SW, 300), (OX0, OY[1] + 20))), GREEN)
L["out>orch"] = (Path(poly(((OX0 + OX1) / 2, OY[2] + 44), ((OX0 + OX1) / 2, 490), (275, 490), (275, 215),
                           (262, 215))), BLUE)

APPEAR = {"orch": 0.2, "jev": 0.45, "out": 1.95, "band": 2.25}
APPEAR.update({f"s{i}": 0.8 + 0.2 * i for i in range(5)})
RULES = ["Every write needs your OK", "New items built paused", "Never changes budgets",
         "Never accepts deal terms", "Never deletes data", "Items labelled AI ·"]
TIERS = [("Fast · Haiku", TEAL), ("Standard · Sonnet", BLUE), ("Deep · Opus", VIOLET)]
DATA = [("CM360", BLUE), ("DV360", GREEN), ("The Trade Desk", AMBER), ("Windsor.ai / exports", CYAN)]


def under(c, t, state):
    act = state["act"]
    for i, (lab, col, agents) in enumerate(STAGES):
        key = f"s{i}"
        x0, x1 = SX[i], SX[i] + SW
        on = state["amt"] if act == key else 0.0
        if on:
            c.glow(x0, SY0, x1, SY1, col, 0.7 * on)
        band(c, x0, SY0, x1, SY1, lab, col, window(t, APPEAR[key], APPEAR[key] + 0.5))
        for j, ag in enumerate(agents):
            y = SY0 + 36 + j * 52
            chip(c, x0 + 8, y, x1 - 8, y + 42, ag, None, col,
                 window(t, APPEAR[key] + 0.1 + j * 0.06, APPEAR[key] + 0.5 + j * 0.06), on, 12.5)
    section_label(c, OX0, 172, "You approve", a=window(t, APPEAR["out"], APPEAR["out"] + 0.4))
    for i, (lab, ic) in enumerate(OUTS):
        on = state["amt"] if act == "out" else 0.0
        chip(c, OX0, OY[i], OX1, OY[i] + 44, lab, ic, GREEN,
             window(t, APPEAR["out"] + i * 0.08, APPEAR["out"] + 0.4 + i * 0.08), on, 12.5)
    c.text(680, 497, "weekly loop", 12, "bold", BLUE, anchor="mm", a=window(t, 2.3, 2.7))
    a = window(t, APPEAR["band"], APPEAR["band"] + 0.5)
    band(c, 40, 512, 1240, 632, "Guardrails in every agent", BLUE, a)
    x = 60
    for r in RULES:
        x += c.pill(x, 540, r, BLUE, size=12.5, weight="demi", a=a, h=28) + 10
    c.text(60, 594, "Data:", 13, "demi", INK, anchor="lm", a=a)
    x = 60 + c.text_w("Data:", 13, "demi") + 12
    for lab, col in DATA:
        x += c.pill(x, 580, lab, col, size=12.5, weight="demi", a=a, h=28) + 10
    x += 14
    c.text(x, 594, "JEV tiers:", 13, "demi", INK, anchor="lm", a=a)
    x += c.text_w("JEV tiers:", 13, "demi") + 12
    for lab, col in TIERS:
        x += c.pill(x, 580, lab, col, size=12.5, weight="demi", a=a, h=28) + 10


def cb(i, dx=0):
    return (SX[i] + SW / 2 + dx, SY1)


SC = [
    Scenario("Weekly check", "Orchestrator finds the leak · JEV picks the cheapest model that can do each task", BLUE, [
        Step(None, "orch", 0, 1.1, "Leak found", "CPA up 18% · DV360 and TTD both claim the same sales", BLUE,
             side="top", callout_xy=(150, 140)),
        Step("orch>jev", "jev", 0.4, 1.3, "JEV routes 9 tasks", "5 fast · 3 standard · 1 deep (attribution)", VIOLET,
             side="bottom", callout_xy=(150, 470)),
        Step("jev>s0", "s0", 0.45, 1.2, "Measure first · Fast", "Floodlight OK · IVT 2.1% · tags QA'd", TEAL,
             side="bottom", callout_xy=cb(0, 60)),
        Step("s0>s1", "s1", 0.4, 1.2, "Plan · Standard", "Move CTV to TTD · keep YouTube on DV360", BLUE,
             side="bottom", callout_xy=cb(1)),
        Step("s1>s2", "s2", 0.4, 1.2, "Buy · Standard", "New line items built paused · 3 PG deals", AMBER,
             side="bottom", callout_xy=cb(2)),
        Step("s2>s3", "s3", 0.4, 1.2, "Optimise · Fast", "Freq cap 4/wk · 2 lines under-pacing", PINK,
             side="bottom", callout_xy=cb(3)),
        Step("s3>s4", "s4", 0.4, 1.3, "Prove · Deep (Opus)", "CM360 dedup: 31% of DSP claims overlap", GREEN,
             side="bottom", callout_xy=cb(4, -40)),
        Step("s4>out", "out", 0.45, 1.6, "Your call", "Ranked actions · JEV saved ~70% vs all-Opus", GREEN,
             side="bottom", callout_xy=(1080, OY[2] + 44)),
    ], label=""),
]

if __name__ == "__main__":
    run_scene(out=OUT, accent=BLUE, kicker="PROGRAMMATIC AGENTS", title="An AI team for CM360, DV360 and TTD",
              sub="Orchestrator → JEV router → measure → plan → buy → optimise → prove",
              right=[("20 agents", AMBER), ("CM360 · DV360 · TTD", GREEN), ("JEV router", VIOLET),
                     ("You approve", BLUE)],
              nodes=N, links=L, appear=APPEAR, scenarios=SC, build_end=3.0, under=under,
              dash_links=("out>orch",),
              build_caption=("WORKFLOW", "20 agents in 5 stages, led by one orchestrator and routed by JEV", BLUE),
              outro_caption=("YOU APPROVE", "Built paused · you launch, unpause and change budgets", BLUE))
