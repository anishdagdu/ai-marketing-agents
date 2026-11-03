"""Renders linkedin-ads-workflow.gif: the 15 LinkedIn Ads agents, animated.

Layout: the five stages are stacked as horizontal lanes and the token snakes down
through them (foundations -> target -> create -> launch + optimise -> prove pipeline),
then drops a ranked action list for you to approve.

Run: python3 linkedin-ads-agents/docs/make_gif.py  (needs Pillow and tools/gifkit.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from gifkit import *  # noqa: E402,F403

OUT = os.path.join(HERE, "..", "linkedin-ads-workflow.gif")
LI = (10, 102, 194)

N = {
    "orch": Node("orch", 40, 140, 250, 330, "Orchestrator", "li-orchestrator", LI, "spark", "LEAD",
                 lines=["Finds the pipeline leak", "Briefs 1-4 agents", "Ranks every action"]),
}

STAGES = [
    ("1 · Foundations", TEAL, ["Account setup", "Insight Tag + CAPI"]),
    ("2 · Target", LI, ["ICP + persona", "ABM lists", "Audiences"]),
    ("3 · Create", VIOLET, ["Copy", "Formats", "Thought leader", "Lead forms"]),
    ("4 · Launch + optimise", AMBER, ["Campaign builder", "Bids + pacing", "Fatigue"]),
    ("5 · Prove pipeline", GREEN, ["CRM pipeline", "Reporting"]),
]
LX0, LX1, LH, LG, LY0 = 290, 1020, 88, 9, 138
LY = [LY0 + i * (LH + LG) for i in range(5)]
LC = [y + LH / 2 + 10 for y in LY]          # lane centre line (below the label)
CX0 = LX0 + 196                             # chips start after the lane title
RX0, RX1 = 1058, 1240
OUTS = [("Ranked actions", "check"), ("Weekly report", "doc"), ("Drafts to launch", "chart")]
OY = [LY[3] + 2 + i * 54 for i in range(3)]

L = {"orch>s0": (Path(curve(N["orch"].R(-50), (LX0, LC[0]))), TEAL)}
for i in range(4):  # serpentine: right edge, left edge, right edge, left edge
    x, d = (LX1, 18) if i % 2 == 0 else (LX0, -18)
    L[f"s{i}>s{i+1}"] = (Path(poly((x, LC[i]), (x + d, LC[i]), (x + d, LC[i + 1]), (x, LC[i + 1]))),
                         STAGES[i + 1][1])
L["s4>out"] = (Path(curve((LX1, LC[4]), (RX0, OY[2] + 22))), GREEN)

APPEAR = {"orch": 0.2, "out": 1.9, "guard": 2.2}
APPEAR.update({f"s{i}": 0.6 + 0.22 * i for i in range(5)})
RULES = ["Your OK on every write", "Built as drafts / paused", "You change budgets",
         "Consented lists only", "Never deletes", "Items named AI ·"]
DATA = [("Campaign Manager", LI), ("HubSpot / Salesforce", AMBER), ("Windsor.ai", CYAN)]


def under(c, t, state):
    act = state["act"]
    for i, (lab, col, agents) in enumerate(STAGES):
        key = f"s{i}"
        y0, y1 = LY[i], LY[i] + LH
        on = state["amt"] if act == key else 0.0
        if on:
            c.glow(LX0, y0, LX1, y1, col, 0.7 * on)
        ap = window(t, APPEAR[key], APPEAR[key] + 0.5)
        band(c, LX0, y0, LX1, y1, "", col, ap)
        c.text(LX0 + 18, y0 + LH / 2, lab, 15, "bold", mix(INK, col, 0.35), anchor="lm", a=ease_out(ap))
        n = len(agents)
        w = (LX1 - 14 - CX0 - 10 * (n - 1)) / n
        for j, ag in enumerate(agents):
            x = CX0 + j * (w + 10)
            chip(c, x, y0 + 20, x + w, y1 - 20, ag, None, col,
                 window(t, APPEAR[key] + 0.1 + j * 0.06, APPEAR[key] + 0.5 + j * 0.06), on, 13)
    # data sources under the orchestrator
    a = window(t, APPEAR["orch"] + 0.3, APPEAR["orch"] + 0.8)
    section_label(c, 40, 352, "Data", a=a)
    for i, (lab, col) in enumerate(DATA):
        chip(c, 40, 374 + i * 50, 250, 414 + i * 50, lab, None, col,
             window(t, APPEAR["orch"] + 0.4 + i * 0.08, APPEAR["orch"] + 0.8 + i * 0.08), 0, 12.5)
    # guardrails, top right
    a = window(t, APPEAR["guard"], APPEAR["guard"] + 0.5)
    band(c, RX0, LY[0], RX1, LY[0] + 246, "Guardrails", LI, a)
    for i, r in enumerate(RULES):
        c.pill(RX0 + 12, LY[0] + 30 + i * 35, r, LI, size=11.5, weight="demi", a=a, h=26)
    # outputs, bottom right
    section_label(c, RX0, OY[0] - 26, "You approve", a=window(t, APPEAR["out"], APPEAR["out"] + 0.4))
    for i, (lab, ic) in enumerate(OUTS):
        on = state["amt"] if act == "out" else 0.0
        chip(c, RX0, OY[i], RX1, OY[i] + 44, lab, ic, GREEN,
             window(t, APPEAR["out"] + i * 0.08, APPEAR["out"] + 0.4 + i * 0.08), on, 12.5)


def mid(i, dx=0, top=False):
    return ((LX0 + LX1) / 2 + dx, LY[i] if top else LY[i] + LH)


SC = [
    Scenario("Weekly check", "Orchestrator finds the pipeline leak · the token snakes through all five lanes", LI, [
        Step(None, "orch", 0, 1.1, "Leak found", "CPL $142 · only 9% of leads become SQLs", LI,
             side="bottom", callout_xy=(145, 330)),
        Step("orch>s0", "s0", 0.45, 1.2, "Foundations", "Audience Expansion off · CAPI sends SQLs back", TEAL,
             side="bottom", callout_xy=mid(0, 120)),
        Step("s0>s1", "s1", 0.4, 1.2, "Target", "3 personas · 412 Tier-1 accounts · exclusions set", LI,
             side="bottom", callout_xy=mid(1, 120)),
        Step("s1>s2", "s2", 0.4, 1.2, "Create", "12 ads · 2 CEO posts · form cut to 4 fields", VIOLET,
             side="top", callout_xy=mid(2, 120, top=True)),
        Step("s2>s3", "s3", 0.4, 1.2, "Launch + optimise", "Built paused · cost cap · 3 tired ads swapped", AMBER,
             side="top", callout_xy=mid(3, 120, top=True)),
        Step("s3>s4", "s4", 0.4, 1.3, "Prove pipeline", "Cost per SQL down 31% · $480K pipeline", GREEN,
             side="top", callout_xy=mid(4, 120, top=True)),
        Step("s4>out", "out", 0.45, 1.6, "Your call", "Ranked actions · you launch the drafts", GREEN,
             side="top", callout_xy=(900, LY[4] + 4)),
    ], label="in"),
]

if __name__ == "__main__":
    run_scene(out=OUT, accent=LI, kicker="LINKEDIN ADS AGENTS", title="An AI team for B2B pipeline on LinkedIn",
              sub="Orchestrator → foundations → target → create → launch + optimise → prove pipeline",
              right=[("15 agents", AMBER), ("Campaign Manager · CRM", GREEN), ("You approve", LI)],
              nodes=N, links=L, appear=APPEAR, scenarios=SC, build_end=3.0, under=under,
              build_caption=("WORKFLOW", "15 agents in 5 lanes, led by one orchestrator", LI),
              outro_caption=("YOU APPROVE", "Drafts and paused campaigns · you launch and change budgets", LI))
