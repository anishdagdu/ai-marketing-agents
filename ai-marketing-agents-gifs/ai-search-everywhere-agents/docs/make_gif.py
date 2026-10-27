"""Renders ai-search-workflow.gif: AI Search Everywhere (SEO, AIO, AEO, GEO, SXO), animated.

Story: a site audit moves through the four stages and seven agents, sets ranking
targets, then the Monday report loops results back into stage 1.

Run: python3 ai-search-everywhere-agents/docs/make_gif.py  (needs Pillow)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from gifkit import *  # noqa: E402,F403

OUT = os.path.join(HERE, "ai-search-workflow.gif")
A, B = (150, 262), (296, 408)
INPUTS = [("Your website", "search"), ("Search Console export", "chart"), ("Target keywords", "tag")]
IX0, IX1 = 40, 225
IY = [166 + i * 70 for i in range(3)]

N = {
    "seo": Node("seo", 260, A[0], 480, A[1], "SEO", "seo-agent", BLUE, "search", "STAGE 1",
                lines=["Technical + on-page", "Schema · internal links"]),
    "aio": Node("aio", 260, B[0], 480, B[1], "AIO", "aio-agent", CYAN, "spark", "STAGE 1",
                lines=["AI Overviews visibility", "Which answers cite you"]),
    "aeo": Node("aeo", 515, A[0], 735, A[1], "AEO", "aeo-agent", VIOLET, "doc", "STAGE 2",
                lines=["Answer-ready pages", "Citability score"]),
    "geo": Node("geo", 515, B[0], 735, B[1], "GEO", "geo-agent", PINK, "user", "STAGE 2",
                lines=["Entity authority", "Reviews · Wikidata · NAP"]),
    "sxo": Node("sxo", 770, 223, 990, 335, "SXO", "sxo-agent", AMBER, "speed", "STAGE 3",
                lines=["Search experience", "Speed · answer · CTA"]),
    "rank": Node("rank", 1025, A[0], 1240, A[1], "Rankings", "rankings-agent", GREEN, "chart", "STAGE 4",
                 lines=["Targets per keyword", "Roadmap to top 3"]),
    "week": Node("week", 1025, B[0], 1240, B[1], "Weekly report", "weekly-report-agent", TEAL, "cal", "MONDAYS",
                 lines=["One page", "Wins · drops · next 3"]),
}
L = {f"i{i}>seo": (Path(curve((IX1, IY[i] + 22), N["seo"].L(-30 + i * 30))), BLUE) for i in range(3)}
L.update({
    "seo>aio": (Path(curve(N["seo"].B(), N["aio"].T(), "v")), CYAN),
    "aio>aeo": (Path(curve(N["aio"].R(), N["aeo"].L())), VIOLET),
    "aeo>geo": (Path(curve(N["aeo"].B(), N["geo"].T(), "v")), PINK),
    "geo>sxo": (Path(curve(N["geo"].R(), N["sxo"].L(20))), AMBER),
    "sxo>rank": (Path(curve(N["sxo"].R(-20), N["rank"].L())), GREEN),
    "rank>week": (Path(curve(N["rank"].B(), N["week"].T(), "v")), TEAL),
    "week>seo": (Path(poly(N["week"].B(), (N["week"].cx, 440), (N["seo"].cx, 440), N["aio"].B(), n=30)), TEAL),
})
APPEAR = {f"i{i}": 0.15 + 0.1 * i for i in range(3)}
APPEAR.update(seo=0.6, aio=0.75, aeo=0.95, geo=1.1, sxo=1.3, rank=1.5, week=1.65, band=1.9)
ENGINES = [("Google", BLUE), ("AI Overviews", CYAN), ("ChatGPT", GREEN), ("Perplexity", TEAL), ("Gemini", VIOLET),
           ("Copilot", PINK)]


def under(c, t, state):
    st = state["st"]
    section_label(c, IX0, 128, "Inputs", a=window(t, 0.1, 0.4))
    for x, lab in ((260, "1 · SEO + AIO"), (515, "2 · AEO + GEO"), (770, "3 · SXO"), (1025, "4 · Rankings")):
        section_label(c, x, 128, lab, a=window(t, 0.5, 0.9))
    for i, (lab, ic) in enumerate(INPUTS):
        on = 1.0 if (st and st["st"].link == f"i{i}>seo" and st["phase"] == "travel") else 0.0
        chip(c, IX0, IY[i], IX1, IY[i] + 44, lab, ic, BLUE, window(t, APPEAR[f"i{i}"], APPEAR[f"i{i}"] + 0.4), on, 13)
    c.text(N["sxo"].cx, 452, "every Monday, results feed stage 1", 12, "bold", TEAL, anchor="mm",
           a=window(t, APPEAR["week"] + 0.5, APPEAR["week"] + 0.9))
    a = window(t, APPEAR["band"], APPEAR["band"] + 0.5)
    band(c, 40, 486, 1240, 626, "Visible everywhere people search", BLUE, a)
    x = 60
    for name, col in ENGINES:
        x += c.pill(x, 524, name, col, size=13, weight="bold", h=28, a=a) + 10
    c.pill(60, 572, "Top 5 in 2–3 months", GREEN, size=13, weight="bold", solid=True, h=28, a=a)
    c.pill(260, 572, "Top 3 in 6 months", GREEN, size=13, weight="bold", solid=True, h=28, a=a)
    c.text(450, 586, "8 Claude skills · 7 agents · runs in claude.ai or Claude Code", 14, "demi", INK, anchor="lm", a=a)


SC = [
    Scenario("Audit", "“Run the search everywhere workflow on example.com”", BLUE, [
        Step("i0>seo", "seo", 0.45, 1.1, "SEO audit", "42 pages · 9 technical fixes · schema gaps", BLUE),
        Step("seo>aio", "aio", 0.4, 1.1, "AI visibility", "Cited in 3 of 20 AI answers checked", CYAN, side="bottom"),
        Step("aio>aeo", "aeo", 0.45, 1.1, "Answer-ready", "FAQ citability score 41 → 78", VIOLET),
        Step("aeo>geo", "geo", 0.4, 1.1, "Entity authority", "Consistent NAP · reviews · Wikidata", PINK,
             side="bottom"),
        Step("geo>sxo", "sxo", 0.45, 1.1, "Search experience", "Answer above the fold · faster CTA", AMBER),
        Step("sxo>rank", "rank", 0.45, 1.2, "Ranking targets", "18 keywords · top 5 by month 3", GREEN,
             callout_xy=(1120, A[0])),
        Step("rank>week", "week", 0.4, 1.2, "Monday report", "+6 keywords in top 10 · 2 new AI citations", TEAL,
             side="bottom", callout_xy=(1100, B[1])),
        Step("week>seo", "aio", 0.7, 0.9, "Loop", "Next week starts from these results", TEAL, side="bottom"),
    ], label=""),
]

if __name__ == "__main__":
    run_scene(out=OUT, accent=BLUE, kicker="AI SEARCH EVERYWHERE", title="Rank on Google and in AI answers",
              sub="SEO + AIO → AEO + GEO → SXO → rankings → weekly report every Monday",
              right=[("7 agents", BLUE), ("8 skills", VIOLET), ("Weekly report", TEAL)],
              nodes=N, links=L, appear=APPEAR, scenarios=SC, build_end=2.8, under=under,
              build_caption=("WORKFLOW", "Four stages, seven agents, one page of results every Monday", BLUE),
              outro_caption=("EVIDENCE FIRST", "Every recommendation comes from your pages, your data or a live search", GREEN),
              dash_links=("week>seo",))
