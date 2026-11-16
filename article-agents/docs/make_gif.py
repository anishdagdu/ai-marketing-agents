"""Renders article-agents-workflow.gif: the 6 article agents, animated.

Story: a topic comes in, a token travels brief -> research -> outline (you approve) -> draft
-> edit. The editor scores it 72 and sends it back round the dashed revise loop; the rewrite
scores 88 and passes to SEO, which saves the article as a CMS draft for you to publish.

Run: python3 article-agents/docs/make_gif.py  (needs Pillow and tools/gifkit.py)
     python3 article-agents/docs/make_gif.py --preview DIR 2.5 8 14   (PNG stills + timeline)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from gifkit import *  # noqa: E402,F403

OUT = os.path.join(HERE, "..", "article-agents-workflow.gif")

CX = [262, 524, 786]          # card left edges (3 columns)
CW = 232
R1, R2, CH = 142, 324, 132    # row tops, card height
N = {
    "n1": Node("n1", CX[0], R1, CX[0] + CW, R1 + CH, "Topic strategist", "ar-topic-strategist", BLUE, "search", "1",
               lines=["Keyword, intent, SERP gap", "Writes the brief"]),
    "n2": Node("n2", CX[1], R1, CX[1] + CW, R1 + CH, "Researcher", "ar-researcher", VIOLET, "db", "2",
               lines=["Facts, stats, quotes", "Every claim sourced"]),
    "n3": Node("n3", CX[2], R1, CX[2] + CW, R1 + CH, "Outline architect", "ar-outline-architect", TEAL, "route", "3",
               lines=["H2/H3 plan, word budget", "Sources per section"]),
    "n4": Node("n4", CX[0], R2, CX[0] + CW, R2 + CH, "Writer", "ar-writer", AMBER, "doc", "4",
               lines=["Draft in your brand voice", "Inline [n] citations"]),
    "n5": Node("n5", CX[1], R2, CX[1] + CW, R2 + CH, "Editor", "ar-editor", PINK, "check", "5",
               tag="GATE 80", lines=["Fact-check, 100-pt score", "Under 80 goes back"]),
    "n6": Node("n6", CX[2], R2, CX[2] + CW, R2 + CH, "SEO & publisher", "ar-seo-publisher", CYAN, "speed", "6",
               tag="DRAFT", lines=["Meta, schema, links", "AI-answer ready"]),
}
INS = [("Topic or keyword", "search"), ("Brand voice", "user"), ("Ahrefs / Semrush", "chart")]
IY = [R1 + 30 + i * 44 for i in range(3)]
OX0, OX1 = 1058, 1240
OUTS = [("CMS draft", "doc"), ("article.html + .md", "tag"), ("Social + newsletter", "send")]
OY = [R2 + 4 + i * 46 for i in range(3)]
LOOP_Y = R2 + CH + 22

L = {
    "in>n1": (Path(curve((222, IY[1] + 18), N["n1"].L())), BLUE),
    "n1>n2": (Path(curve(N["n1"].R(), N["n2"].L())), VIOLET),
    "n2>n3": (Path(curve(N["n2"].R(), N["n3"].L())), TEAL),
    "n3>n4": (Path(poly(N["n3"].B(), (N["n3"].cx, R1 + CH + 24), (N["n4"].cx, R1 + CH + 24), N["n4"].T())), AMBER),
    "n4>n5": (Path(curve(N["n4"].R(), N["n5"].L())), PINK),
    "n5>n4": (Path(poly(N["n5"].B(), (N["n5"].cx, LOOP_Y), (N["n4"].cx, LOOP_Y), N["n4"].B())), RED),
    "n5>n6": (Path(curve(N["n5"].R(), N["n6"].L())), CYAN),
    "n6>out": (Path(curve(N["n6"].R(), (OX0, OY[1] + 20))), GREEN),
}

APPEAR = {"in": 0.2, "out": 2.0, "band": 2.3}
APPEAR.update({f"n{i + 1}": 0.5 + 0.2 * i for i in range(6)})
RULES = ["You approve topic + outline", "No invented facts or quotes", "Gaps marked [NEEDS SOURCE]",
         "Editor gate: score 80+", "CMS writes are drafts", "Never publishes live"]
WORKS = [("Ahrefs", BLUE), ("Semrush", AMBER), ("HubSpot", PINK), ("Wix", VIOLET), ("Humanizer", TEAL)]


def under(c, t, state):
    act = state["act"]
    section_label(c, 40, R1 + 6, "Inputs", a=window(t, 0.15, 0.5))
    for i, (lab, ic) in enumerate(INS):
        on = state["amt"] if act == "in" else 0.0
        chip(c, 40, IY[i], 222, IY[i] + 36, lab, ic, BLUE,
             window(t, APPEAR["in"] + i * 0.08, APPEAR["in"] + 0.4 + i * 0.08), on, 12.5)
    section_label(c, OX0, R2 - 18, "You publish", a=window(t, APPEAR["out"], APPEAR["out"] + 0.4))
    for i, (lab, ic) in enumerate(OUTS):
        on = state["amt"] if act == "out" else 0.0
        chip(c, OX0, OY[i], OX1, OY[i] + 38, lab, ic, GREEN,
             window(t, APPEAR["out"] + i * 0.08, APPEAR["out"] + 0.4 + i * 0.08), on, 12.5)
    a = window(t, 2.2, 2.6)
    looping = state["st"] is not None and state["st"]["st"].link == "n5>n4"
    col = RED if looping else mix(RED, DIM, 0.35)
    c.pill(N["n4"].cx + (N["n5"].cx - N["n4"].cx) / 2 - 78, LOOP_Y - 12, "REVISE · score under 80", col,
           size=11.5, weight="bold", a=a, h=24, solid=looping)
    a = window(t, APPEAR["band"], APPEAR["band"] + 0.5)
    band(c, 40, 512, 1240, 632, "Guardrails in every agent", BLUE, a)
    x = 60
    for r in RULES:
        x += c.pill(x, 540, r, BLUE, size=12.5, weight="demi", a=a, h=28) + 10
    c.text(60, 594, "Works with:", 13, "demi", INK, anchor="lm", a=a)
    x = 60 + c.text_w("Works with:", 13, "demi") + 12
    for lab, col in WORKS:
        x += c.pill(x, 580, lab, col, size=12.5, weight="demi", a=a, h=28) + 10


def stamp_at(node, text, color):
    n = N[node]
    return lambda c, u: stamp(c, n.x1 - 44, n.y0 + 70, text, color, appear=window(u, 0.15, 0.45))


def below(node, dx=0):
    return (N[node].cx + dx, N[node].y1)


SC = [
    Scenario("New article", "A topic goes in · six agents take it to a fact-checked CMS draft", BLUE, [
        Step(None, "in", 0, 1.0, "Topic in", "Email deliverability for Shopify stores", BLUE,
             side="bottom", callout_xy=(131, IY[2] + 36)),
        Step("in>n1", "n1", 0.45, 1.2, "Brief", "1.9K searches · how-to intent · gap: no 2026 data", BLUE,
             side="bottom", callout_xy=below("n1", 20)),
        Step("n1>n2", "n2", 0.4, 1.2, "Research", "14 sources · 9 primary · 2 gaps flagged", VIOLET,
             side="bottom", callout_xy=below("n2")),
        Step("n2>n3", "n3", 0.4, 1.4, "Outline", "7 sections · 1,800 words · you approve it", TEAL,
             side="bottom", callout_xy=below("n3", -30), extra=stamp_at("n3", "APPROVED", GREEN)),
        Step("n3>n4", "n4", 0.6, 1.2, "Draft", "1,840 words · 22 inline citations", AMBER,
             side="bottom", callout_xy=below("n4", 30)),
        Step("n4>n5", "n5", 0.4, 1.4, "Edit", "Score 72 · two stats don't match the source", RED,
             side="bottom", callout_xy=below("n5", 60), extra=stamp_at("n5", "REVISE", RED)),
        Step("n5>n4", "n4", 0.6, 1.1, "Rewrite", "Writer fixes all 6 items on the list", AMBER,
             side="bottom", callout_xy=below("n4", 30), token=RED),
        Step("n4>n5", "n5", 0.4, 1.3, "Edit again", "Score 88 · facts check out", GREEN,
             side="bottom", callout_xy=below("n5", 60), extra=stamp_at("n5", "PASS", GREEN)),
        Step("n5>n6", "n6", 0.4, 1.2, "SEO", "Meta, FAQ schema, 4 internal links", CYAN,
             side="bottom", callout_xy=below("n6", -30)),
        Step("n6>out", "out", 0.45, 1.6, "Your call", "Saved as a HubSpot draft · you publish", GREEN,
             side="bottom", callout_xy=(OX0 + 40, OY[2] + 38)),
    ], label="A"),
]

def save_gif_wide(frames, durations, path, colors=255):
    """Like gifkit.save_gif, but the shared palette also sees every accent colour.

    Six accents plus their tints don't fit in a palette sampled from 5 mostly-white frames:
    amber, teal and violet got merged into a muddy maroon. Sampling 12 frames and adding a
    swatch strip of each accent (solid and its light tints) keeps them true.
    """
    import gifkit
    from PIL import Image
    idx = sorted(set(int(i * (len(frames) - 1) / 11) for i in range(12)))
    w, h = frames[0].width, frames[0].height
    sw_h = 40
    strip = Image.new("RGB", (w, h * len(idx) + sw_h * 4))
    for i, k in enumerate(idx):
        strip.paste(frames[k], (0, i * h))
    accents = [BLUE, VIOLET, TEAL, AMBER, PINK, CYAN, GREEN, RED]
    cw = w // len(accents)
    for r, t in enumerate((0.0, 0.45, 0.75, 0.9)):
        for j, col in enumerate(accents):
            strip.paste(mix(col, WHITE, t), (j * cw, h * len(idx) + r * sw_h, (j + 1) * cw, h * len(idx) + (r + 1) * sw_h))
    pal = strip.quantize(colors=colors, method=Image.MEDIANCUT)
    q = [f.quantize(palette=pal, dither=Image.Dither.NONE) for f in frames]
    q[0].save(path, save_all=True, append_images=q[1:], duration=durations, loop=0, optimize=True, disposal=1)
    return os.path.getsize(path)


if __name__ == "__main__":
    import gifkit
    gifkit.save_gif = save_gif_wide  # run_scene looks save_gif up in gifkit's globals
    run_scene(out=OUT, accent=BLUE, kicker="ARTICLE AGENTS", title="An AI team that researches, writes and ships articles",
              sub="Topic → research → outline → draft → edit → SEO & CMS draft",
              right=[("6 agents", AMBER), ("Ahrefs · HubSpot · Wix", GREEN), ("You approve", BLUE)],
              nodes=N, links=L, appear=APPEAR, scenarios=SC, build_end=3.0, under=under,
              dash_links=("n5>n4",),
              build_caption=("WORKFLOW", "6 agents in one line, with an editor gate before anything ships", BLUE),
              outro_caption=("YOU APPROVE", "You sign off the outline · CMS writes are drafts · you publish", BLUE))
