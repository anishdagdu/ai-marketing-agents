"""Renders content-agents-workflow.gif: the Content Agents, animated.

Story: config feeds website and competitor sentiment research, you review the
insights, the planner writes the calendar, you approve, and the publisher does
a dry run before scheduling posts in Postiz.

Run: python3 content-agents/docs/make_gif.py  (needs Pillow)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from gifkit import *  # noqa: E402,F403

OUT = os.path.join(HERE, "..", "content-agents-workflow.gif")
XS = [40, 347, 654, 961]
WD = 279
R1, R2 = (150, 270), (318, 438)

N = {
    "cfg": Node("cfg", XS[0], 234, XS[0] + WD, 354, "Config", "config.yaml", DIM, "doc", "INPUT",
                lines=["Brand · pages · competitors", "Posts per week · key dates"]),
    "web": Node("web", XS[1], R1[0], XS[1] + WD, R1[1], "Website sentiment", "website-sentiment-analyst", BLUE,
                "heart", "AGENT 1", lines=["Promise vs what customers say", "Score −1 to +1"]),
    "comp": Node("comp", XS[1], R2[0], XS[1] + WD, R2[1], "Competitor sentiment", "competitor-sentiment-analyst",
                 VIOLET, "search", "AGENT 2", lines=["Loves, complaints, positioning", "Topics nobody covers"]),
    "cp1": Node("cp1", XS[2], 234, XS[2] + WD, 354, "Checkpoint 1", "You review the insights", RED, "user",
                "YOU REVIEW", lines=["Orchestrator stops here", "Nothing planned yet"]),
    "cal": Node("cal", XS[3], R1[0], XS[3] + WD, R1[1], "Calendar planner", "content-calendar-planner", PINK,
                "cal", "AGENT 3", lines=["Weekly themes · post copy", "Visual brief per post"]),
    "pub": Node("pub", XS[3], R2[0], XS[3] + WD, R2[1], "Postiz publisher", "postiz-publisher", GREEN, "send",
                "AGENT 4", tag="DRY RUN", lines=["Matches posts to channels", "Schedules after your OK"]),
}
L = {
    "cfg>web": (Path(curve(N["cfg"].R(-20), N["web"].L())), BLUE),
    "cfg>comp": (Path(curve(N["cfg"].R(20), N["comp"].L())), VIOLET),
    "web>cp1": (Path(curve(N["web"].R(), N["cp1"].L(-20))), RED),
    "comp>cp1": (Path(curve(N["comp"].R(), N["cp1"].L(20))), RED),
    "cp1>cal": (Path(curve(N["cp1"].R(-20), N["cal"].L())), PINK),
    "cal>pub": (Path(curve(N["cal"].B(), N["pub"].T(), "v")), GREEN),
    "pub>out": (Path(curve(N["pub"].B(), (N["pub"].cx, 510), "v")), GREEN),
}
APPEAR = dict(cfg=0.2, web=0.45, comp=0.55, cp1=0.85, cal=1.1, pub=1.35, out=1.6, band=1.6)
CH = [("LinkedIn", BLUE), ("Instagram", PINK), ("Facebook", BLUE), ("X", INK), ("TikTok", INK), ("Threads", DIM)]
OUT_T = (13.1, 14.2)


def under(c, t, state):
    a = window(t, APPEAR["web"], APPEAR["web"] + 0.4)
    c.text(XS[1] + 4, R1[1] + 24, "run at the same time", 12.5, "bold", DIM, a=a)
    a = window(t, APPEAR["band"], APPEAR["band"] + 0.5)
    band(c, 40, 510, 1240, 626, "Scheduled in Postiz · checkpoint 2: you approve before anything posts", GREEN, a)
    x = 60
    for i, (name, col) in enumerate(CH):
        on = window(t, OUT_T[0] + i * 0.15, OUT_T[0] + i * 0.15 + 0.25) if OUT_T[0] <= t < OUT_T[1] + 1 else 0.0
        w = c.text_w(name, 13.5, "bold") + 28
        c.rect(x, 548, x + w, 584, r=10, fill=mix(WHITE, col, 0.85 * on), outline=mix(LINE, col, 0.4 + 0.6 * on),
               width=1.4, a=a)
        c.text(x + w / 2, 566, name, 13.5, "bold", mix(INK, WHITE, on), anchor="mm", a=a)
        x += w + 12
    c.text(1220, 566, "16 posts · 4 weeks", 15, "bold", INK, anchor="rm", a=a)


def pill_below(node, text, color):
    def fn(c, u):
        n = N[node]
        c.pill(n.x0 + 14, n.y1 + 8, text, color, size=12, weight="bold", solid=True, h=24, a=window(u, 0.45, 0.7))
    return fn


SC = [
    Scenario("4 weeks", "Content calendar for a specialty coffee brand", PINK, [
        Step(None, "cfg", 0, 1.0, "Config", "3 competitors · 4 posts a week · launch on 12 Nov", DIM),
        Step("cfg>web", "web", 0.45, 1.2, "Your sentiment +0.42", "Site says “smooth” · reviews say “too bitter”", BLUE),
        Step("cfg>comp", "comp", 0.5, 1.2, "Content gap", "No competitor posts brewing guides", VIOLET,
             side="bottom"),
        Step("comp>cp1", "cp1", 0.45, 1.4, "Checkpoint 1", "You review the insights before planning", RED,
             extra=pill_below("cp1", "Insights approved", GREEN), side="bottom"),
        Step("cp1>cal", "cal", 0.45, 1.3, "Calendar ready", "16 posts · weekly themes · copy + visual briefs", PINK),
        Step("cal>pub", "pub", 0.45, 1.4, "Dry run passed", "16 posts matched to 4 channels · no errors", GREEN,
             side="bottom", callout_xy=(1100, R2[1])),
        Step("pub>out", "pub", 0.4, 1.8, "Scheduled", "You approved · posts queued in Postiz", GREEN,
             callout_xy=(760, 510)),
    ], label=""),
]

if __name__ == "__main__":
    run_scene(out=OUT, accent=PINK, kicker="CONTENT AGENTS", title="Social content from real sentiment research",
              sub="Config → website + competitor sentiment → you review → calendar → you approve → Postiz",
              right=[("5 agents", PINK), ("2 checkpoints", RED), ("Postiz", GREEN)],
              nodes=N, links=L, appear=APPEAR, scenarios=SC, build_end=2.8, under=under,
              build_caption=("WORKFLOW", "The content orchestrator runs it all and stops at two checkpoints", PINK),
              outro_caption=("EVIDENCE ONLY", "No invented stats, reviews or quotes · nothing scheduled until you say yes", GREEN))
