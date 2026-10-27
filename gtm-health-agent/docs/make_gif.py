"""Renders gtm-agent-workflow.gif: the weekly GTM Health Agent audit, animated.

Story: the 8-step loop assembles, then one Monday run finds a deleted purchase
trigger, scores it P0, explains the cause and ships the fix list.

Run: python3 gtm-health-agent/docs/make_gif.py  (needs Pillow)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from gifkit import *  # noqa: E402,F403

OUT = os.path.join(HERE, "..", "gtm-agent-workflow.gif")
XS = [40, 350, 660, 970]
W1 = 270
R1, R2 = (150, 262), (300, 412)


def nd(key, col, row, title, sub, color, ic, num, lines):
    y0, y1 = (R1, R2)[row]
    return Node(key, XS[col], y0, XS[col] + W1, y1, title, sub, color, ic, num, lines=lines)


N = {
    "n1": nd("n1", 0, 0, "Trigger", "Every Monday · 8 AM", BLUE, "clock", "STEP 1", ["Scheduled task", "Read-only run"]),
    "n2": nd("n2", 1, 0, "Connect", "GTM MCP connector", BLUE, "route", "STEP 2", ["Find accounts", "List containers"]),
    "n3": nd("n3", 2, 0, "Collect", "Live version + workspaces", VIOLET, "db", "STEP 3", ["Tags · triggers · variables", "User permissions"]),
    "n4": nd("n4", 3, 0, "Audit", "30+ checks", RED, "search", "STEP 4", ["Won't-fire causes", "Consent v2 · PII leaks"]),
    "n5": nd("n5", 3, 1, "Score", "Severity + health 0–100", RED, "gauge", "STEP 5", ["P0 to P3 per issue", "Score per container"]),
    "n6": nd("n6", 2, 1, "Diagnose", "Likely cause + exact fix", AMBER, "spark", "STEP 6", ["Recent publish? who?", "dataLayer change?"]),
    "n7": nd("n7", 1, 1, "Compare", "Week over week", TEAL, "chart", "STEP 7", ["NEW · STILL OPEN · FIXED", "Weeks open"]),
    "n8": nd("n8", 0, 1, "Report", "Ship it to the team", GREEN, "doc", "STEP 8", ["Top 5 actions + owner", "Full issue table"]),
}
L = {
    "n1>n2": (Path(curve(N["n1"].R(), N["n2"].L())), BLUE),
    "n2>n3": (Path(curve(N["n2"].R(), N["n3"].L())), VIOLET),
    "n3>n4": (Path(curve(N["n3"].R(), N["n4"].L())), RED),
    "n4>n5": (Path(curve(N["n4"].B(), N["n5"].T(), "v")), RED),
    "n5>n6": (Path(curve(N["n5"].L(), N["n6"].R())), AMBER),
    "n6>n7": (Path(curve(N["n6"].L(), N["n7"].R())), TEAL),
    "n7>n8": (Path(curve(N["n7"].L(), N["n8"].R())), GREEN),
    "n8>n1": (Path(curve(N["n8"].T(-60), N["n1"].B(-60), "v")), BLUE),
}
APPEAR = dict(n1=0.2, n2=0.4, n3=0.6, n4=0.8, n5=1.0, n6=1.2, n7=1.4, n8=1.6, band=1.9)

SEV = [("P0", "Revenue data lost now", RED), ("P1", "Data wrong / at risk", AMBER),
       ("P2", "Will cause bugs", (202, 138, 4)), ("P3", "Housekeeping", DIM)]
BX0, BY0, BX1, BY1 = 40, 456, 1240, 626
COUNTS = {"P0": 1, "P1": 2, "P2": 4, "P3": 3}
SCORE = 100 - (25 * 1 + 10 * 2 + 3 * 4 + 1 * 3)  # 40


def severity_panel(c, t, counts_k, score_k):
    a = window(t, APPEAR["band"], APPEAR["band"] + 0.5)
    band(c, BX0, BY0, BX1, BY1, "Severity · health score = 100 − (25×P0 + 10×P1 + 3×P2 + 1×P3)", RED, a)
    if a <= 0.01:
        return
    for i, (p, desc, col) in enumerate(SEV):
        x0 = BX0 + 16 + i * 205
        y0 = BY0 + 40
        c.rect(x0, y0, x0 + 190, y0 + 108, r=12, fill=WHITE, outline=mix(LINE, col, 0.5), width=1.4, a=a)
        c.pill(x0 + 14, y0 + 14, p, col, size=12, weight="bold", solid=True, h=24, a=a)
        n = int(round(COUNTS[p] * counts_k))
        c.text(x0 + 176, y0 + 10, str(n) if counts_k > 0 else "–", 30, "bold", col if n else DIM, anchor="ra", a=a)
        c.text(x0 + 14, y0 + 56, desc, 13, "demi", INK, a=a)
        c.text(x0 + 14, y0 + 78, "issues this week", 12, "medium", MUTED, a=a)
    # gauge
    gx, gy, r = 1080, BY0 + 112, 62
    pts = [(gx + r * math.cos(math.pi + i * math.pi / 40), gy + r * math.sin(math.pi + i * math.pi / 40)) for i in range(41)]
    c.line(pts, BG2, 12, a)
    val = 100 - (100 - SCORE) * score_k
    col = mix(RED, GREEN, clamp((val - 40) / 50))
    m = max(2, int(40 * val / 100))
    c.line(pts[:m + 1], col, 12, a)
    c.text(gx, gy - 14, f"{int(round(val))}", 30, "bold", INK, anchor="mm", a=a)
    c.text(gx, gy + 12, "web-prod health", 12, "demi", MUTED, anchor="mm", a=a)


SC = [
    Scenario("Monday 8:00", "The weekly audit runs on its own and changes nothing in GTM", BLUE, [
        Step(None, "n1", 0, 1.0, "Run started", "Scheduled task · read-only GTM tools", BLUE),
        Step("n1>n2", "n2", 0.45, 0.9, "Connected", "3 accounts · 7 containers found", BLUE),
        Step("n2>n3", "n3", 0.45, 0.9, "Live version pulled", "212 tags · 148 triggers · 96 variables", VIOLET),
        Step("n3>n4", "n4", 0.45, 1.3, "Issues found", "Purchase trigger deleted · Meta tag paused", RED),
        Step("n4>n5", "n5", 0.4, 1.4, "Scored", "1 × P0 → revenue data lost now", RED, side="bottom",
             callout_xy=(XS[3] + 135, R2[1] - 4)),
        Step("n5>n6", "n6", 0.45, 1.2, "Root cause", "Publish v87 on Friday 17:42 removed the trigger", AMBER, side="bottom", callout_xy=(XS[2] + 135, R2[1] - 4)),
        Step("n6>n7", "n7", 0.45, 1.0, "Week over week", "2 NEW · 4 STILL OPEN · 3 FIXED", TEAL,
             side="bottom", callout_xy=(XS[1] + 135, R2[1] - 4)),
        Step("n7>n8", "n8", 0.45, 1.3, "Report shipped", "Top 5 actions with owners · verify in Preview", GREEN, side="bottom", callout_xy=(XS[0] + 150, R2[1] - 4)),
    ], label=""),
]


def under(c, t, state):
    # counts fill during the Audit step, the gauge drops during the Score step (times from --preview)
    severity_panel(c, t, ease_out(window(t, 7.05, 8.0)), ease_in_out(window(t, 8.75, 9.9)))
    c.text(N["n1"].x0 + 86, (R1[1] + R2[0]) / 2, "next Monday", 12, "bold", BLUE, anchor="lm",
           a=window(t, APPEAR["n8"] + 0.5, APPEAR["n8"] + 0.9))


if __name__ == "__main__":
    run_scene(out=OUT, accent=BLUE, kicker="GTM HEALTH AGENT", title="Weekly Google Tag Manager audit",
              sub="Trigger → connect → collect → audit → score → diagnose → compare → report",
              right=[("1 weekly agent", BLUE), ("30+ checks", RED), ("Read-only", GREEN)],
              nodes=N, links=L, appear=APPEAR, scenarios=SC, build_end=2.8, under=under,
              build_caption=("LOOP", "Eight steps every Monday · flags tags that won't fire and explains why", BLUE),
              outro_caption=("READ-ONLY", "It never creates, edits or publishes in GTM · a human makes every change", GREEN),
              dash_links=("n8>n1",))
