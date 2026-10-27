"""Renders ai-ugc-agents-workflow.gif: the AI UGC ad agents, animated.

Story: a product brief becomes an ad matrix and prompts; compliance catches a
health claim and sends it back; once READY you approve the credits, and the
operator generates the videos on Higgsfield.

Run: python3 ai-ugc-ad-agents/docs/make_gif.py  (needs Pillow)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from gifkit import *  # noqa: E402,F403

OUT = os.path.join(HERE, "..", "ai-ugc-agents-workflow.gif")
R1, R2 = (150, 284), (338, 472)

N = {
    "brief": Node("brief", 40, R1[0], 280, R1[1], "Brief", "Product · audience · platform", DIM, "doc", "INPUT",
                  lines=["Facts from the product page", "Number of ads"]),
    "dir": Node("dir", 320, R1[0], 620, R1[1], "UGC director", "ugc-director", VIOLET, "video", "AGENT 1",
                tag="plan.md", lines=["Creators: age, look, setting", "Hook × angle × format · scripts"]),
    "pe": Node("pe", 660, R1[0], 940, R1[1], "Prompt engineer", "prompt-engineer", BLUE, "spark", "AGENT 2",
               tag="prompts.md", lines=["Soul 2.0 image prompt", "Seedance 2.0 video prompt"]),
    "cc": Node("cc", 980, R1[0], 1240, R1[1], "Compliance check", "ad-compliance-checker", AMBER, "shield",
               "AGENT 3", lines=["Health & result claims", "Under-21s, look-alikes"]),
    "ap": Node("ap", 980, R2[0], 1240, R2[1], "You approve", "Credit cost + screenshot", RED, "user", "GATE",
               lines=["No Generate without your OK", "Or a credit cap you set"]),
    "op": Node("op", 600, R2[0], 940, R2[1], "Higgsfield operator", "higgsfield-operator", GREEN, "send",
               "AGENT 4", lines=["Drives higgsfield.ai in a browser", "One ad at a time"]),
    "out": Node("out", 40, R2[0], 560, R2[1], "Ad videos", "Ready for Meta, TikTok and Reels", GREEN, "video",
                "OUTPUT", lines=["Image → 15-second video per ad", "Label realistic AI people as AI"]),
}
L = {
    "brief>dir": (Path(curve(N["brief"].R(), N["dir"].L())), VIOLET),
    "dir>pe": (Path(curve(N["dir"].R(), N["pe"].L())), BLUE),
    "pe>cc": (Path(curve(N["pe"].R(-12), N["cc"].L(-12))), AMBER),
    "cc>pe": (Path(curve(N["cc"].L(26), N["pe"].R(26))), RED),
    "cc>ap": (Path(curve(N["cc"].B(), N["ap"].T(), "v")), RED),
    "ap>op": (Path(curve(N["ap"].L(), N["op"].R())), GREEN),
    "op>out": (Path(curve(N["op"].L(), N["out"].R())), GREEN),
}
APPEAR = dict(brief=0.2, dir=0.45, pe=0.7, cc=0.95, ap=1.2, op=1.45, out=1.7, band=1.95)


def stamp_on(node, text, color):
    def fn(c, u):
        n = N[node]
        stamp(c, n.x1 - 70, n.y1 - 26, text, color, window(u, 0.1, 0.35))
    return fn


def thumbs(c, u):
    n = N["out"]
    for i in range(5):
        k = window(u, 0.1 + i * 0.12, 0.3 + i * 0.12)
        if k <= 0:
            continue
        x = n.x1 - 230 + i * 44
        y = n.y0 + 14
        c.rect(x, y, x + 36, y + 58, r=7, fill=mix(WHITE, GREEN, 0.18), outline=GREEN, width=1.4, a=k)
        c.circle(x + 18, y + 22, 7, fill=mix(WHITE, GREEN, 0.5), a=k)
        c.rect(x + 7, y + 34, x + 29, y + 50, r=5, fill=mix(WHITE, GREEN, 0.5), a=k)


def under(c, t, state):
    c.text(960, 300, "fails → fix (max 2 rounds)", 12, "bold", RED, anchor="mm",
           a=window(t, APPEAR["cc"] + 0.5, APPEAR["cc"] + 0.9))
    a = window(t, APPEAR["band"], APPEAR["band"] + 0.5)
    band(c, 40, 508, 1240, 626, "Run it in Claude Code", BLUE, a)
    if a > 0:
        c.rect(60, 548, 700, 600, r=10, fill=INK, a=a)
        c.text(80, 574, "/ugc-campaign  vitamin C serum, women 25–40, TikTok, 5 ads", 15, "demi", WHITE, anchor="lm", a=a)
        c.text(730, 560, "Nothing generated before compliance says READY", 14, "demi", INK, a=a)
        c.text(730, 584, "Never types passwords · adult (21+) creators only", 14, "demi", INK, a=a)


SC = [
    Scenario("Campaign", "Vitamin C serum · women 25–40 · TikTok · 5 ads", VIOLET, [
        Step(None, "brief", 0, 1.0, "Brief in", "Only claims from the product page", DIM),
        Step("brief>dir", "dir", 0.45, 1.2, "Ad matrix", "5 creators × hooks × angles · 15-second scripts", VIOLET),
        Step("dir>pe", "pe", 0.45, 1.1, "Prompts written", "One image + one video prompt per ad", BLUE),
        Step("pe>cc", "cc", 0.45, 1.5, "1 ad fails", "“Clears acne in 7 days” is a health claim", RED,
             extra=stamp_on("cc", "FIX", RED)),
        Step("cc>pe", "pe", 0.45, 1.0, "Rewritten", "“Brighter-looking skin” · no promised result", BLUE),
        Step("pe>cc", "cc", 0.45, 1.2, "All 5 pass", "Meta and TikTok ad policy checked", GREEN,
             extra=stamp_on("cc", "READY", GREEN)),
        Step("cc>ap", "ap", 0.45, 1.3, "Your OK", "5 ads · about 40 credits · screenshot shown", RED,
             side="bottom", callout_xy=(1110, R2[1])),
        Step("ap>op", "op", 0.45, 1.1, "Generating", "Soul 2.0 image → Seedance 2.0 video", GREEN, side="bottom"),
        Step("op>out", "out", 0.45, 1.6, "5 ad videos", "Saved with screenshots and a resume file", GREEN,
             extra=thumbs, side="bottom", callout_xy=(170, R2[1])),
    ], label=""),
]

if __name__ == "__main__":
    run_scene(out=OUT, accent=VIOLET, kicker="AI UGC AD AGENTS", title="AI creator video ads on Higgsfield",
              sub="Brief → creators, hooks and scripts → prompts → compliance → you approve → generate",
              right=[("4 agents", VIOLET), ("1 workflow", BLUE), ("You approve credits", RED)],
              nodes=N, links=L, appear=APPEAR, scenarios=SC, build_end=2.8, under=under,
              build_caption=("WORKFLOW", "Four agents take a brief to finished AI UGC videos", VIOLET),
              outro_caption=("GUARDRAILS", "No Generate click without your OK · no invented product claims", GREEN),
              dash_links=("cc>pe",))
