"""Renders mmp-agents-workflow.gif: the 20 MMP agents, animated.

Story: the orchestrator finds the biggest measurement gap, a token travels through the five
stages (measure -> signals -> protect -> analyze -> activate), each stage's agents light up,
and a ranked action list comes out for you to approve.

Run: python3 mmp-agents/docs/make_gif.py  (needs Pillow and tools/gifkit.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from gifkit import *  # noqa: E402,F403

OUT = os.path.join(HERE, "..", "mmp-agents-workflow.gif")

N = {
    "orch": Node("orch", 40, 150, 260, 330, "Orchestrator", "mmp-orchestrator", BLUE, "spark", "LEAD",
                 lines=["Finds the biggest gap", "Briefs 1–4 specialists", "Ranks every action"]),
}
DATA = [("AppsFlyer / Adjust", "db"), ("Ad networks + cost", "chart"), ("Warehouse + CRM", "doc")]
DY = [368 + i * 40 for i in range(3)]

STAGES = [
    ("1 · Measure", BLUE, ["Attribution", "SAN reconcile", "Lookback windows", "SKAN + AAK"]),
    ("2 · Signals", VIOLET, ["Postbacks", "In-app events", "Ad revenue", "Raw data export"]),
    ("3 · Protect", RED, ["Fraud: real time", "Fraud: after", "Privacy + consent", "Clean room"]),
    ("4 · Analyze", AMBER, ["Cost + ROAS", "Cohorts + LTV", "Creative", "Incrementality"]),
    ("5 · Activate", TEAL, ["Deep linking", "Web, CTV, PC", "Audiences", "AI copilot"]),
]
SX0, SW, SG, SY0, SY1 = 290, 144, 10, 140, 470
SX = [SX0 + i * (SW + SG) for i in range(5)]
OX0, OX1 = 1070, 1240
OUTS = [("Ranked actions", "check"), ("Weekly readout", "doc"), ("Changes to approve", "shield")]
OY = [200 + i * 54 for i in range(3)]

L = {"orch>s0": (Path(curve(N["orch"].R(-30), (SX[0], 210))), BLUE)}
for i in range(4):
    L[f"s{i}>s{i+1}"] = (Path(curve((SX[i] + SW, 300), (SX[i + 1], 300))), STAGES[i + 1][1])
L["s4>out"] = (Path(curve((SX[4] + SW, 300), (OX0, OY[1] + 20))), GREEN)
L["out>orch"] = (Path(poly(((OX0 + OX1) / 2, OY[2] + 44), ((OX0 + OX1) / 2, 490), (275, 490), (275, 290),
                           (262, 290))), BLUE)
L["d0>orch"] = (Path(curve((150, DY[0]), (150, 332), "v")), CYAN)

APPEAR = {"orch": 0.2, "out": 1.9, "band": 2.2}
APPEAR.update({f"s{i}": 0.75 + 0.2 * i for i in range(5)})
APPEAR.update({f"d{i}": 0.4 + 0.1 * i for i in range(3)})
RULES = ["Every MMP change needs your OK", "Never changes budgets", "Never touches the SDK",
         "No user-level data in chat", "Consent respected", "Assets labelled AI ·"]
HANDOFF = [("AI Paid Traffic", AMBER), ("AI UGC Ads", PINK), ("Klaviyo 1PD", VIOLET),
           ("GTM Health", TEAL), ("CRM Agents", BLUE)]


def under(c, t, state):
    act = state["act"]
    section_label(c, 170, 342, "Data", a=window(t, 0.35, 0.7))
    for i, (lab, ic) in enumerate(DATA):
        chip(c, 40, DY[i], 260, DY[i] + 34, lab, ic, CYAN, window(t, APPEAR[f"d{i}"], APPEAR[f"d{i}"] + 0.4), 0.0, 13)
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
    c.text(620, 497, "weekly loop", 12, "bold", BLUE, anchor="mm", a=window(t, 2.3, 2.7))
    a = window(t, APPEAR["band"], APPEAR["band"] + 0.5)
    band(c, 40, 512, 1240, 632, "Guardrails in every agent", GREEN, a)
    x = 60
    for r in RULES:
        x += c.pill(x, 540, r, GREEN, size=12.5, weight="demi", a=a, h=28) + 10
    c.text(60, 594, "Hands off to:", 13, "demi", INK, anchor="lm", a=a)
    x = 60 + c.text_w("Hands off to:", 13, "demi") + 12
    for lab, col in HANDOFF:
        x += c.pill(x, 580, lab, col, size=12.5, weight="demi", a=a, h=28) + 10


SC = [
    Scenario("Weekly check", "The orchestrator finds the biggest measurement gap and sends the right agents", BLUE, [
        Step(None, "orch", 0, 1.1, "Gap found", "Meta claims 2x the installs the MMP credits", BLUE, side="top",
             callout_xy=(150, 150)),
        Step("orch>s0", "s0", 0.45, 1.2, "Measure", "Dedupe SAN claims · fix the 28-day view window", BLUE,
             side="bottom", callout_xy=(SX[0] + SW / 2 + 60, SY1)),
        Step("s0>s1", "s1", 0.4, 1.2, "Signals", "Send purchases, not installs, to TikTok", VIOLET,
             side="bottom", callout_xy=(SX[1] + SW / 2, SY1)),
        Step("s1>s2", "s2", 0.4, 1.2, "Protect", "Click injection on one partner · block list drafted", RED,
             side="bottom", callout_xy=(SX[2] + SW / 2, SY1)),
        Step("s2>s3", "s3", 0.4, 1.2, "Analyze", "D30 ROAS by source · geo holdout planned", AMBER,
             side="bottom", callout_xy=(SX[3] + SW / 2, SY1)),
        Step("s3>s4", "s4", 0.4, 1.2, "Activate", "Lapsed-payer audience + deep link as drafts", TEAL,
             side="bottom", callout_xy=(SX[4] + SW / 2 - 40, SY1)),
        Step("s4>out", "out", 0.45, 1.6, "Your call", "Ranked actions · nothing changes without your OK", GREEN,
             side="bottom", callout_xy=(1080, OY[2] + 44)),
    ], label=""),
]

if __name__ == "__main__":
    run_scene(out=OUT, accent=BLUE, kicker="MMP AGENTS", title="An AI team for AppsFlyer, Adjust and every MMP",
              sub="Orchestrator → measure → signals → protect → analyze → activate",
              right=[("21 agents", AMBER), ("AppsFlyer · Adjust", BLUE), ("You approve", GREEN)],
              nodes=N, links=L, appear=APPEAR, scenarios=SC, build_end=3.0, under=under,
              dash_links=("out>orch",),
              build_caption=("WORKFLOW", "20 specialists in 5 stages, led by one orchestrator", BLUE),
              outro_caption=("YOU APPROVE", "Reports and drafts only · you change settings, budgets and the SDK", GREEN))
