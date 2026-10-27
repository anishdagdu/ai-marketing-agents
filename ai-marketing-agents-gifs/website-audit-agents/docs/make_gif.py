"""Renders website-audit-agents-workflow.gif: the website audit agents, animated.

Story: GitHub Actions starts the Monday speed check, PageSpeed data flows into
the 10 agents (each lights up pass / warn / fail / skipped), Claude summarises
the regressions, and the scorecard, GitHub Issue and Slack alert go out.

Run: python3 website-audit-agents/docs/make_gif.py  (needs Pillow; not needed by run.py)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from gifkit import *  # noqa: E402,F403

OUT = os.path.join(HERE, "website-audit-agents-workflow.gif")

N = {
    "trig": Node("trig", 40, 150, 250, 300, "Trigger", "GitHub Actions", BLUE, "clock", "STEP 1",
                 lines=["Mon 06:00 · speed check", "1st of month · full audit", "Or run manually"]),
    "comb": Node("comb", 990, 150, 1240, 284, "Combine", "run.py + Claude", VIOLET, "spark", "STEP 4",
                 lines=["Compare with last run", "Summary for leadership"]),
}
DATA = [("PageSpeed Insights", "speed"), ("Ahrefs Webmaster", "chart"), ("Search Console", "search"),
        ("Built-in crawler", "route")]
DX0, DX1 = 285, 480
DY = [160 + i * 58 for i in range(4)]
PX0, PY0, PX1, PY1 = 515, 140, 955, 470
AG = [("1 Core Web Vitals", GREEN), ("2 Conversion leakage", RED), ("3 Speed fix backlog", AMBER),
      ("4 Marketing tag bloat", RED), ("5 Accessibility", GREEN), ("6 Site health", None),
      ("7 Crawl & links", None), ("8 Striking keywords", None), ("9 Backlinks", None), ("10 Early warning", RED)]
AX = [530, 745]
AY = [176 + i * 56 for i in range(5)]
OUTS = [("Scorecard in reports/", "doc"), ("GitHub Issue + checklist", "check"), ("Slack regression alert", "bolt")]
OX0, OX1 = 990, 1240
OY = [330 + i * 50 for i in range(3)]

L = {f"trig>d{i}": (Path(curve(N["trig"].R(-30 + i * 20), (DX0, DY[i] + 22))), BLUE) for i in range(4)}
L.update({f"d{i}>panel": (Path(curve((DX1, DY[i] + 22), (PX0, 250 + i * 20))), CYAN) for i in range(4)})
L["panel>comb"] = (Path(curve((PX1, 250), N["comb"].L())), VIOLET)
L["comb>out"] = (Path(curve(N["comb"].B(), ((OX0 + OX1) / 2, OY[0]), "v")), GREEN)

APPEAR = {"trig": 0.2, "panel": 0.95, "comb": 1.6, "out": 1.8, "band": 2.0}
APPEAR.update({f"d{i}": 0.45 + 0.1 * i for i in range(4)})
KPIS = ["CWV pass ≥ 75%", "LCP < 2.5 s", "Tags < 250 ms", "A11y ≥ 90", "Health ≥ 90", "0 broken pages",
        "+5 keywords to top 3", "Net new ref. domains"]

STATUS_T = (6.0, 7.8)   # agents light up during the panel step (see --preview timings)
OUT_T = (10.6, 11.6)    # outputs light up during the deliver step
SKIP = mix(LINE, DIM, 0.4)


def under(c, t, state):
    act = state["act"]
    st = state["st"]
    section_label(c, DX0, 128, "Free data", a=window(t, 0.4, 0.8))
    section_label(c, OX0, 304, "Deliver", a=window(t, APPEAR["out"], APPEAR["out"] + 0.4))
    for i, (lab, ic) in enumerate(DATA):
        on = 1.0 if (st and st["st"].link in (f"trig>d{i}",) and st["phase"] == "travel") or act == f"d{i}" else 0.0
        chip(c, DX0, DY[i], DX1, DY[i] + 44, lab, ic, CYAN, window(t, APPEAR[f"d{i}"], APPEAR[f"d{i}"] + 0.4), on, 13)
    pa = window(t, APPEAR["panel"], APPEAR["panel"] + 0.5)
    if act == "panel":
        c.glow(PX0, PY0, PX1, PY1, AMBER, 0.7 * state["amt"])
    band(c, PX0, PY0, PX1, PY1, "Step 3 · run 10 AI agents", AMBER, pa)
    for i, (lab, col) in enumerate(AG):
        x = AX[i // 5]
        y = AY[i % 5]
        k = window(t, STATUS_T[0] + i * 0.15, STATUS_T[0] + i * 0.15 + 0.3)
        if t > STATUS_T[1] + 4:   # keep statuses through the outro
            k = 1.0
        status = ((col or SKIP), k)
        chip(c, x, y, x + 200, y + 44, lab, None, col or DIM,
             window(t, APPEAR["panel"] + 0.1 + i * 0.05, APPEAR["panel"] + 0.5 + i * 0.05), 0.0, 12.5, status)
    for i, (lab, ic) in enumerate(OUTS):
        on = window(t, OUT_T[0] + i * 0.3, OUT_T[0] + i * 0.3 + 0.25) if OUT_T[0] <= t < OUT_T[1] + 0.8 else 0.0
        chip(c, OX0, OY[i], OX1, OY[i] + 40, lab, ic, GREEN, window(t, APPEAR["out"] + i * 0.08, APPEAR["out"] + 0.4 + i * 0.08), on, 12.5)
    # legend + KPIs
    a = window(t, APPEAR["band"], APPEAR["band"] + 0.5)
    band(c, 40, 500, 1240, 626, "KPIs tracked every run", BLUE, a)
    x = 60
    for kpi in KPIS:
        w = c.pill(x, 538, kpi, BLUE, size=12.5, weight="demi", a=a, h=28)
        x += w + 10
    x = 60
    for lab, col in [("Pass", GREEN), ("Warn", AMBER), ("Fail", RED), ("Skipped this run", SKIP)]:
        c.circle(x + 7, 590, 7, fill=col, a=a)
        c.text(x + 20, 590, lab, 13, "demi", INK, anchor="lm", a=a)
        x += c.text_w(lab, 13, "demi") + 50


SC = [
    Scenario("Monday 06:00", "The weekly speed check runs itself on GitHub Actions", BLUE, [
        Step(None, "trig", 0, 1.0, "Run started", "Speed agents 1–5 and early-warning 10", BLUE),
        Step("trig>d0", "d0", 0.45, 1.1, "PageSpeed Insights", "6 revenue pages · mobile and desktop", CYAN,
             callout_xy=((DX0 + DX1) / 2, DY[0])),
        Step("d0>panel", "panel", 0.45, 2.3, "Agents report", "Status · KPI vs target · next action · owner", AMBER,
             side="bottom", callout_xy=((PX0 + PX1) / 2, PY1)),
        Step("panel>comb", "comb", 0.45, 1.4, "Claude summary", "Checkout LCP 3.4 s (+0.9 s) · tags 410 ms", VIOLET,
             callout_xy=(1080, 150)),
        Step("comb>out", "out", 0.45, 1.6, "Delivered", "Scorecard committed · Issue opened · Slack alerted", GREEN,
             side="bottom", callout_xy=(1100, OY[2] + 40)),
    ], label=""),
]

if __name__ == "__main__":
    run_scene(out=OUT, accent=BLUE, kicker="WEBSITE AUDIT AGENTS", title="Website speed & site health audit",
              sub="Trigger → free data → 10 agents → combine → deliver",
              right=[("10 agents", AMBER), ("GitHub Actions", BLUE), ("Read-only", GREEN)],
              nodes=N, links=L, appear=APPEAR, scenarios=SC, build_end=2.9, under=under,
              build_caption=("WORKFLOW", "Weekly speed check + monthly full audit, fully automated", BLUE),
              outro_caption=("READ-ONLY", "It reports and opens tickets · your team makes the fixes", GREEN))
