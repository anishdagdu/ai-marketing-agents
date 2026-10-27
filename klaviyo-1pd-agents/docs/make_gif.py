"""Renders klaviyo-agents-workflow.gif: the Klaviyo 1PD agents, animated.

Story: first-party signals feed five agents; one run audits the data, proposes
segments (you approve), drafts flows and campaigns (you send), then the weekly
loop measures results and routes a fix back.

Run: python3 klaviyo-1pd-agents/docs/make_gif.py  (needs Pillow)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from gifkit import *  # noqa: E402,F403

OUT = os.path.join(HERE, "..", "klaviyo-agents-workflow.gif")

SIG = [("Product views", "search"), ("Cart adds", "tag"), ("Placed Order", "check"),
       ("Email & SMS engagement", "mail"), ("Consent status", "shield")]
SX0, SX1 = 40, 250
SY = [168 + i * 56 for i in range(5)]

N = {
    "n1": Node("n1", 290, 150, 600, 284, "Data foundation", "kl-data-foundation", BLUE, "db", "AGENT 1",
               tag="READ-ONLY", lines=["Audit events, catalog, consent", "Readiness score + setup plan"]),
    "n2": Node("n2", 630, 150, 940, 284, "Segment architect", "kl-segment-architect", VIOLET, "user", "AGENT 2",
               tag="ON APPROVAL", lines=["RFM, intent, VIP, at-risk", "Ad seed + exclusion audiences"]),
    "n3": Node("n3", 970, 150, 1240, 284, "Flow builder", "kl-flow-builder", GREEN, "route", "AGENT 3",
               tag="DRAFTS", lines=["Welcome, cart, browse", "Post-buy, win-back, sunset"]),
    "n5": Node("n5", 630, 330, 940, 464, "Performance analyst", "kl-performance-analyst", PINK, "chart",
               "AGENT 5", tag="WEEKLY", lines=["Revenue per recipient", "Routes each fix to an agent"]),
    "n4": Node("n4", 970, 330, 1240, 464, "Campaign strategist", "kl-campaign-strategist", AMBER, "cal",
               "AGENT 4", tag="YOU SEND", lines=["4-week calendar per segment", "Personalised copy + A/B"]),
}
L = {f"s{i}>n1": (Path(curve((SX1, SY[i] + 21), N["n1"].L(-40 + i * 20))), CYAN) for i in range(5)}
L.update({
    "n1>n2": (Path(curve(N["n1"].R(), N["n2"].L())), VIOLET),
    "n2>n3": (Path(curve(N["n2"].R(), N["n3"].L())), GREEN),
    "n3>n4": (Path(curve(N["n3"].B(), N["n4"].T(), "v")), AMBER),
    "n4>n5": (Path(curve(N["n4"].L(), N["n5"].R())), PINK),
    "n5>n2": (Path(curve(N["n5"].T(-60), N["n2"].B(-60), "v")), VIOLET),
    "n5>n1": (Path(curve(N["n5"].L(), N["n1"].B(40), "h", 0.7)), BLUE),
})
APPEAR = {f"s{i}": 0.15 + 0.08 * i for i in range(5)}
APPEAR.update(n1=0.7, n2=0.95, n3=1.2, n4=1.45, n5=1.7, band=1.95)
GUARD = ["Every write needs your OK", "Flows saved as drafts", "Never sends campaigns",
         "Consented profiles only", "Never deletes or suppresses", "Assets labelled “AI ·”"]


def under(c, t, state):
    st = state["st"]
    section_label(c, SX0, 128, "Your Klaviyo data", a=window(t, 0.05, 0.4))
    section_label(c, 290, 128, "Five agents · one workflow", a=window(t, 0.6, 0.9))
    for i, (lab, ic) in enumerate(SIG):
        on = 1.0 if (st and st["st"].link == f"s{i}>n1" and st["phase"] == "travel") else 0.0
        chip(c, SX0, SY[i], SX1, SY[i] + 42, lab, ic, CYAN, window(t, APPEAR[f"s{i}"], APPEAR[f"s{i}"] + 0.4), on, 12.5)
    # guardrails band
    a = window(t, APPEAR["band"], APPEAR["band"] + 0.5)
    band(c, 40, 500, 1240, 626, "AI recommends · you approve", GREEN, a)
    for i, g in enumerate(GUARD):
        x = 60 + (i % 3) * 400
        y = 540 + (i // 3) * 40
        c.circle(x + 10, y + 10, 10, fill=GREEN, a=a)
        icon(c, "check", x + 10, y + 10, WHITE, size=9, a=a)
        c.text(x + 28, y + 10, g, 14, "demi", INK, anchor="lm", a=a)


def approve(text, color=GREEN):
    def fn(c, u):
        k = window(u, 0.45, 0.7)
        if k > 0:
            c.pill(N["n2"].x0 + 14, N["n2"].y1 + 8, text, color, size=12, weight="bold", solid=True, h=24, a=k)
    return fn


def drafts(node, text, color):
    def fn(c, u):
        n = N[node]
        c.pill(n.x0 + 14, n.y1 + 8, text, color, size=12, weight="bold", solid=True, h=24, a=window(u, 0.4, 0.65))
    return fn


SC = [
    Scenario("This week", "Grow repeat revenue from first-party data", VIOLET, [
        Step("s2>n1", "n1", 0.5, 1.2, "Readiness 82/100", "Placed Order, product views and consent all firing", BLUE),
        Step("n1>n2", "n2", 0.45, 1.5, "6 segments proposed", "VIP · at-risk · hot browsers · cart abandoners …", VIOLET,
             extra=approve("You approved all 6 · created in Klaviyo")),
        Step("n2>n3", "n3", 0.45, 1.3, "3 flows drafted", "Abandoned checkout · win-back · post-purchase", GREEN,
             extra=drafts("n3", "Saved as drafts · you switch on", GREEN)),
        Step("n3>n4", "n4", 0.45, 1.3, "4-week calendar", "One segment per send · subject-line A/B test", AMBER,
             side="bottom", extra=drafts("n4", "Drafts · you press send", AMBER)),
        Step("n4>n5", "n5", 0.45, 1.3, "Monday readout", "Revenue per recipient +18% · spam 0.03%", PINK, side="bottom"),
        Step("n5>n1", "n1", 0.55, 1.2, "Fix routed", "Unengaged 180-day profiles grew → sunset flow", BLUE),
    ], label=""),
]

if __name__ == "__main__":
    run_scene(out=OUT, accent=VIOLET, kicker="KLAVIYO 1PD AGENTS", title="Email & SMS from first-party data",
              sub="Data audit → segments → flows → campaigns → weekly performance loop",
              right=[("5 agents", VIOLET), ("1 workflow", GREEN), ("Drafts only", AMBER)],
              nodes=N, links=L, appear=APPEAR, scenarios=SC, build_end=2.8, under=under,
              build_caption=("WORKFLOW", "Five agents turn site behaviour, orders and consent into revenue", VIOLET),
              outro_caption=("SAFE BY DEFAULT", "Nothing is created without your OK · campaigns are never sent for you", GREEN),
              dash_links=("n5>n2", "n5>n1"))
