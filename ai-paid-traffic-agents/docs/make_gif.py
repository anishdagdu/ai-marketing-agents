"""Renders ai-paid-traffic-workflow.gif: the 8 paid-traffic agents, animated.

Story: a launch brief goes through research and strategy (you approve), then
creative, the platform agents in parallel, tracking and scaling; the weekly
Optimize loop feeds results back into the strategy.

Run: python3 ai-paid-traffic-agents/docs/make_gif.py  (needs Pillow)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from gifkit import *  # noqa: E402,F403

OUT = os.path.join(HERE, "..", "ai-paid-traffic-workflow.gif")
XS = [40, 347, 654, 961]
WD = 279
R1, R2 = (150, 270), (330, 450)
PX = [654, 853, 1052]
PW = 188

N = {
    "brief": Node("brief", XS[0], R1[0], XS[0] + WD, R1[1], "Brief", "Product · margin · budget · goal", DIM, "doc",
                  "STEP 0", lines=["Platforms you use", "00-brief.md"]),
    "res": Node("res", XS[1], R1[0], XS[1] + WD, R1[1], "Research", "research-agent", BLUE, "search", "AGENT 1",
                lines=["Avatar · reviews · competitors", "Offer audit · keywords"]),
    "str": Node("str", XS[2], R1[0], XS[2] + WD, R1[1], "Strategy", "strategy-agent", RED, "chart", "AGENT 2",
                tag="YOU APPROVE", lines=["KPI targets · budget split", "Funnel · 4-week test plan"]),
    "cre": Node("cre", XS[3], R1[0], XS[3] + WD, R1[1], "Creative", "creative-agent", PINK, "spark", "AGENT 3",
                lines=["Hooks · ad copy · UGC scripts", "Static + video briefs"]),
    "meta": Node("meta", PX[0], R2[0], PX[0] + PW, R2[1], "Meta", "meta-ads-agent", BLUE, "user", "AGENT 4",
                 lines=["Advantage+", "Retargeting"]),
    "goog": Node("goog", PX[1], R2[0], PX[1] + PW, R2[1], "Google", "google-ads-agent", GREEN, "search", "AGENT 5",
                 lines=["Search · PMax", "Negatives"]),
    "tik": Node("tik", PX[2], R2[0], PX[2] + PW, R2[1], "TikTok", "tiktok-ads-agent", INK, "video", "AGENT 6",
                lines=["Spark Ads", "TikTok Shop"]),
    "trk": Node("trk", XS[1], R2[0], XS[1] + WD, R2[1], "Tracking", "tracking-agent", AMBER, "tag", "AGENT 7",
                lines=["Pixel / CAPI · UTMs", "Conversion audit"]),
    "scl": Node("scl", XS[0], R2[0], XS[0] + WD, R2[1], "Scale", "scale-agent", VIOLET, "gauge", "AGENT 8",
                lines=["ROAS diagnosis · fatigue", "Scaling rules · weekly report"]),
}
L = {
    "brief>res": (Path(curve(N["brief"].R(), N["res"].L())), BLUE),
    "res>str": (Path(curve(N["res"].R(), N["str"].L())), RED),
    "str>cre": (Path(curve(N["str"].R(), N["cre"].L())), PINK),
    "cre>meta": (Path(curve(N["cre"].B(-90), N["meta"].T(), "v")), BLUE),
    "cre>goog": (Path(curve(N["cre"].B(-20), N["goog"].T(), "v")), GREEN),
    "cre>tik": (Path(curve(N["cre"].B(60), N["tik"].T(), "v")), INK),
    "meta>trk": (Path(curve(N["meta"].L(), N["trk"].R())), AMBER),
    "trk>scl": (Path(curve(N["trk"].L(), N["scl"].R())), VIOLET),
    "scl>str": (Path(curve(N["scl"].T(60), N["str"].B(-60), "v", 0.6)), VIOLET),
}
APPEAR = dict(brief=0.2, res=0.4, str=0.6, cre=0.8, meta=1.0, goog=1.08, tik=1.16, trk=1.4, scl=1.6, band=1.9)


def under(c, t, state):
    a = window(t, APPEAR["meta"], APPEAR["meta"] + 0.4)
    c.text(PX[0] + 4, R2[1] + 14, "Agents 4–6 run in parallel, only for the platforms you use", 12.5, "bold", DIM, a=a)
    a = window(t, APPEAR["band"], APPEAR["band"] + 0.5)
    band(c, 40, 500, 1240, 626, "Three modes", BLUE, a)
    for i, (m, d, col) in enumerate([("Launch", "1 → 2 → 3 → 4/5/6 + 7 · new account or product", BLUE),
                                     ("Optimize", "7 → 8 → 3 → 2 · already spending, run weekly", VIOLET),
                                     ("Single task", "“Write hooks” → straight to the creative agent", PINK)]):
        x = 60 + i * 400
        c.pill(x, 540, m, col, size=13, weight="bold", solid=True, h=26, a=a)
        c.text(x, 586, d, 13.5, "demi", INK, a=a)


def approved(c, u):
    n = N["str"]
    c.pill(n.x0 + 14, n.y1 + 8, "You approved the plan", GREEN, size=12, weight="bold", solid=True, h=24,
           a=window(u, 0.45, 0.7))


def parallel(c, u):
    for k, w0 in (("meta", 0.0), ("goog", 0.15), ("tik", 0.3)):
        n = N[k]
        c.glow(n.x0, n.y0, n.x1, n.y1, n.color, 0.75 * window(u, w0, w0 + 0.2))


SC = [
    Scenario("Launch", "New skincare brand · $15k a month · Meta, Google and TikTok", BLUE, [
        Step(None, "brief", 0, 1.0, "Brief", "Margin 68% · goal: first-time buyers", DIM),
        Step("brief>res", "res", 0.45, 1.1, "Research", "120 reviews mined · 14 competitor ads", BLUE),
        Step("res>str", "str", 0.45, 1.5, "Strategy", "Target CPA $32 · 60/30/10 split", RED, extra=approved),
        Step("str>cre", "cre", 0.45, 1.1, "Creative", "20 hooks · 6 UGC scripts · 8 static briefs", PINK),
        Step("cre>goog", "goog", 0.5, 1.4, "Platform builds", "Advantage+ · PMax + Search · Spark Ads", GREEN,
             extra=parallel, side="bottom"),
        Step("meta>trk", "trk", 0.5, 1.1, "Tracking", "Pixel + CAPI deduped · UTMs on every ad", AMBER, side="bottom"),
        Step("trk>scl", "scl", 0.45, 1.2, "Week 2 readout", "ROAS 2.4 · two hooks fatigued", VIOLET, side="bottom",
             callout_xy=(190, R2[1])),
        Step("scl>str", "str", 0.6, 1.2, "Optimize loop", "Refresh creative · update the test plan", VIOLET),
    ], label=""),
]

if __name__ == "__main__":
    run_scene(out=OUT, accent=BLUE, kicker="AI PAID TRAFFIC", title="Paid ads end to end: 8 agents, one workflow",
              sub="Research → strategy (you approve) → creative → Meta / Google / TikTok → tracking → scale",
              right=[("8 agents", BLUE), ("1 workflow", PINK), ("You approve spend", RED)],
              nodes=N, links=L, appear=APPEAR, scenarios=SC, build_end=2.8, under=under,
              build_caption=("WORKFLOW", "Every agent reads the earlier files, so nothing is asked twice", BLUE),
              outro_caption=("AI RECOMMENDS", "The agents never launch, pause or change budgets · you make every spend call", GREEN),
              dash_links=("scl>str",))
