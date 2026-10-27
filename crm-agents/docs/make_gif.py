"""Renders crm-agents-architecture.gif: the CRM Agents architecture, animated.

Story: the system assembles stage by stage, a churning player is won back
(with uplift measured against control), an at-risk player's promotion is
vetoed by the RG Guardian, then everything flows on a summary card.

Run from anywhere: python3 crm-agents/docs/make_gif.py  (needs Pillow)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from gifkit import *  # noqa: E402,F403

W, H = 1280, 720
OUT = os.path.join(HERE, "..", "crm-agents-architecture.gif")

# ------------------------------------------------------------------ layout
DATA = [("Gaming platform", "db"), ("Retail loyalty card", "tag"), ("App & web events", "spark"),
        ("Payments", "chart"), ("RG limits", "shield")]
CHIP_Y = [150 + i * 60 for i in range(5)]
CHIP_X0, CHIP_X1 = 40, 205

N = {
    "n1": Node("n1", 245, 150, 465, 262, "Player 360", "One profile per player", BLUE, "user", "AGENT 1",
               lines=["Identity merge", "Micro-segments"]),
    "n2": Node("n2", 245, 300, 465, 430, "Predictive Scoring", "Churn · LTV · next best action", BLUE, "gauge",
               "AGENT 2"),
    "n3": Node("n3", 505, 150, 725, 262, "Journey Orchestrator", "Goal in plain words → journey", VIOLET,
               "route", "AGENT 3", lines=["Win-back, shop → app", "Draft until approved"]),
    "n4": Node("n4", 505, 300, 725, 412, "Real-Time Trigger", "Event → send in seconds", VIOLET, "bolt",
               "AGENT 4", lines=["Jackpot, win, limit hit"]),
    "n8": Node("n8", 765, 150, 985, 290, "RG Guardian", "Highest priority", RED, "shield", "AGENT 8",
               tag="VETO", lines=["Scores risk live", "Can stop any message", "Escalates to player care"]),
    "n9": Node("n9", 765, 320, 985, 432, "Contact Policy", "Caps · quiet hours", AMBER, "filter", "AGENT 9",
               lines=["Max 3 promos a week", "Best uplift wins"]),
    "n7": Node("n7", 1025, 150, 1240, 262, "Personalisation", "Game, hook and copy", GREEN, "spark", "AGENT 7",
               lines=["Finnish · Swedish · English"]),
    "n5": Node("n5", 262, 506, 562, 590, "Uplift & Control", "Lift vs a held-out group", TEAL, "chart",
               "AGENT 5"),
    "n6": Node("n6", 592, 506, 892, 590, "Self-Optimising Test", "Bandits on uplift, never spend", TEAL,
               "flask", "AGENT 6"),
    "n10": Node("n10", 922, 506, 1222, 590, "Insights & Calendar", "Weekly summary · Q&A", TEAL, "cal",
                "AGENT 10"),
}
CH = dict(x0=1025, y0=300, x1=1240, y1=432)
CHANNELS = [("Email", "mail"), ("Push", "send"), ("SMS", "doc"), ("In-app", "user"), ("Web", "search")]
CH_POS = []
for i, _ in enumerate(CHANNELS):
    col, row = i % 3, i // 3
    CH_POS.append((CH["x0"] + 12 + col * 67, CH["y0"] + 48 + row * 40))
BAND = (245, 488, 1240, 606)


def chip_R(i):
    return (CHIP_X1, CHIP_Y[i] + 21)


def build_links():
    L = {}
    for i in range(5):
        L[f"d{i}>n1"] = (Path(curve(chip_R(i), N["n1"].L(-36 + i * 18))), CYAN)
    L["n1>n2"] = (Path(curve(N["n1"].B(), N["n2"].T(), "v")), BLUE)
    L["n2>n3"] = (Path(curve(N["n2"].R(-30), N["n3"].L(20))), VIOLET)
    L["n2>n4"] = (Path(curve(N["n2"].R(10), N["n4"].L(0))), VIOLET)
    L["n3>n8"] = (Path(curve(N["n3"].R(0), N["n8"].L(-30))), RED)
    L["n4>n8"] = (Path(curve(N["n4"].R(0), N["n8"].L(30))), RED)
    L["n8>n9"] = (Path(curve(N["n8"].B(), N["n9"].T(), "v")), AMBER)
    L["n9>n7"] = (Path(curve(N["n9"].R(0), N["n7"].L(25))), GREEN)
    L["n7>ch"] = (Path(curve(N["n7"].B(), ((CH["x0"] + CH["x1"]) / 2, CH["y0"]), "v")), GREEN)
    L["ch>n10"] = (Path(curve(((CH["x0"] + CH["x1"]) / 2, CH["y1"]), N["n10"].T(60), "v")), TEAL)
    loop = poly((BAND[0], 547), (150, 547), (150, CHIP_Y[-1] + 48), n=30)
    L["loop"] = (Path(loop), TEAL)
    return L


LINKS = build_links()

# when each element appears (seconds)
APPEAR = {f"d{i}": 0.15 + 0.09 * i for i in range(5)}
APPEAR.update(n1=0.7, n2=0.85, n3=1.05, n4=1.15, n8=1.35, n9=1.5, n7=1.65, ch=1.8, band=1.95,
              n5=2.05, n6=2.15, n10=2.25)
BUILD_END = 3.0


def link_ends(name):
    if name == "loop":
        return "n5", "d4"
    a, b = name.split(">")
    return a, b


def link_start(name):
    a, b = link_ends(name)
    return max(APPEAR.get(a, 0), APPEAR.get(b, 0)) + 0.15


# ------------------------------------------------------------------ custom pieces
def draw_chip(c, i, appear, active=0.0):
    if appear <= 0.01:
        return
    e = ease_out(appear)
    a = e
    y = CHIP_Y[i] + (1 - e) * 10
    name, ic = DATA[i]
    col = RED if name == "RG limits" else CYAN
    if active > 0.01:
        c.glow(CHIP_X0, y, CHIP_X1, y + 42, col, strength=0.8 * active, spread=12)
    c.rect(CHIP_X0, y, CHIP_X1, y + 42, r=10, fill=mix(CARD, mix(WHITE, col, 0.08), active),
           outline=mix(LINE, col, 0.3 + 0.7 * active), width=1.4, a=a)
    c.circle(CHIP_X0 + 21, y + 21, 13, fill=mix(WHITE, col, 0.14), a=a)
    icon(c, ic, CHIP_X0 + 21, y + 21, col, size=12, a=a)
    c.text(CHIP_X0 + 40, y + 21, name, 13, "demi", INK, anchor="lm", a=a)


def draw_channels(c, appear, lit=None, lit_amt=0.0, lit_color=GREEN):
    if appear <= 0.01:
        return
    e = ease_out(appear)
    a = e
    dy = (1 - e) * 12
    c.rect(CH["x0"], CH["y0"] + dy, CH["x1"], CH["y1"] + dy, r=14, fill=CARD, outline=LINE, width=1.2, a=a)
    c.rect(CH["x0"] + 1, CH["y0"] + 1 + dy, CH["x0"] + 5, CH["y1"] - 1 + dy, r=2, fill=GREEN, a=a)
    c.text(CH["x0"] + 16, CH["y0"] + 14 + dy, "Channels", 16.5, "bold", INK, a=a)
    for i, (name, ic) in enumerate(CHANNELS):
        x, y = CH_POS[i]
        y += dy
        on = lit_amt if lit == i else 0.0
        col = lit_color
        c.rect(x, y, x + 62, y + 30, r=8, fill=mix(BG, col, 0.9 * on), outline=mix(LINE, col, on), width=1.4, a=a)
        icon(c, ic, x + 12, y + 15, mix(MUTED, WHITE, on), size=10, a=a)
        c.text(x + 22, y + 15, name, 11.5, "demi", mix(INK, WHITE, on), anchor="lm", a=a)


def draw_band(c, appear):
    if appear <= 0.01:
        return
    a = ease_out(appear)
    x0, y0, x1, y1 = BAND
    c.rect(x0, y0, x1, y1, r=16, fill=mix(BG, TEAL, 0.06), outline=mix(BG, TEAL, 0.45), width=1.2, a=a)
    section_label(c, x0 + 16, y0 + 3, "Learning loop · measures what CRM adds", TEAL, a=a)


def churn_meter(c, value, a=1.0, hot=False):
    n = N["n2"]
    x0, x1, y = n.x0 + 16, n.x1 - 16, n.y1 - 34
    c.text(x0, y - 4, "Churn risk", 12.5, "demi", MUTED, a=a)
    c.text(x1, y - 4, f"{value:.2f}", 13, "bold", RED if hot else INK, anchor="ra", a=a)
    c.rect(x0, y + 14, x1, y + 21, r=3, fill=BG2, a=a)
    col = mix(GREEN, RED, clamp((value - 0.3) / 0.45))
    c.rect(x0, y + 14, x0 + (x1 - x0) * value, y + 21, r=3, fill=col, a=a)


def badge(c, x, y, kind, color, appear):
    if appear <= 0.01:
        return
    r = 13 * back_out(appear)
    c.circle(x, y, r, fill=color)
    icon(c, kind, x, y, WHITE, size=11)


# ------------------------------------------------------------------ scenario extras
def s1_score(c, u):
    churn_meter(c, 0.30 + 0.45 * ease_in_out(window(u, 0.05, 0.7)), hot=u > 0.5)


def s1_rg_ok(c, u):
    badge(c, N["n8"].x1 - 18, N["n8"].y1 - 18, "check", GREEN, window(u, 0.1, 0.4))


def s1_learn(c, u):
    k = ease_out(window(u, 0.0, 0.5))
    for key, w0 in (("n5", 0.0), ("n6", 0.3), ("n10", 0.6)):
        n = N[key]
        c.glow(n.x0, n.y0, n.x1, n.y1, TEAL, 0.8 * window(u, w0, w0 + 0.2))
    callout(c, N["n5"].cx, N["n5"].y0, "Uplift vs control", f"+{4.2 * k:.1f} pts reactivation · 14 days", TEAL,
            appear=window(u, 0.0, 0.2))
    callout(c, N["n6"].cx, N["n6"].y0, "Bandit winner", "Evening push beats email", TEAL,
            appear=window(u, 0.3, 0.5))
    callout(c, N["n10"].cx - 30, N["n10"].y0, "Weekly summary", "Suggest: make it always-on", TEAL,
            appear=window(u, 0.6, 0.8))


def s2_score(c, u):
    churn_meter(c, 0.30)
    n = N["n2"]
    c.pill(n.x0 + 16, n.y1 - 62, "RG score 0.72 · high", RED, size=11.5, weight="bold", solid=True, a=window(u, 0.1, 0.5))


def s2_veto(c, u):
    n = N["n8"]
    stamp(c, n.cx + 40, n.cy + 18, "VETO", RED, window(u, 0.05, 0.3))
    c.pill(n.x0 + 10, n.y1 + 8, "→ Player care team notified", RED, size=11.5, weight="bold", solid=True, a=window(u, 0.45, 0.7))


SCENARIOS = [
    Scenario("Scenario 1", "A regular Lotto player starts to churn", BLUE, [
        Step("d0>n1", "n1", 0.45, 0.85, "Player 360", "Weekly Lotto player · digital · low risk", BLUE),
        Step("n1>n2", "n2", 0.35, 1.25, "Churn risk jumps", "0.30 → 0.75 after 3 missed draws", RED,
             extra=s1_score, side="bottom", callout_xy=(355, 430)),
        Step("n2>n3", "n3", 0.4, 0.85, "Win-back journey", "Push today · 10% held back as control", VIOLET),
        Step("n3>n8", "n8", 0.4, 0.9, "RG check passed", "Low risk → promotion allowed", GREEN, extra=s1_rg_ok),
        Step("n8>n9", "n9", 0.35, 0.75, "Contact policy", "1 of 3 promos this week → send", AMBER,
             side="bottom", callout_xy=(875, 432)),
        Step("n9>n7", "n7", 0.4, 0.85, "Personalised hook", "Lotto · €8M on Saturday (in Finnish)", GREEN,
             callout_xy=(1120, 150)),
        Step("n7>ch", "ch", 0.35, 0.6, "Sent", "Push · 18:30, the player's best time", GREEN,
             side="bottom", callout_xy=(1110, 432)),
        Step("ch>n10", "n10", 0.45, 1.9, extra=s1_learn),
    ]),
    Scenario("Scenario 2", "A different player shows risky play", RED, [
        Step("d4>n1", "n1", 0.45, 0.7, "New signals", "Limit raised · 45% of play after midnight", RED, token=AMBER),
        Step("n1>n2", "n2", 0.35, 0.95, "High value, high risk", "Next best action → care, never an offer", RED,
             extra=s2_score, side="bottom", callout_xy=(355, 430), token=AMBER),
        Step("n2>n4", "n4", 0.4, 0.7, "Jackpot alert queued", "Eurojackpot €70M · push", VIOLET,
             side="bottom", callout_xy=(615, 412), token=AMBER),
        Step("n4>n8", "n8", 0.4, 1.7, "Promotion blocked", "Swapped for: “Set a weekly limit”", RED,
             extra=s2_veto, token=AMBER),
        Step("n8>n9", "n9", 0.35, 0.6, "Care message", "Doesn't count towards the cap", TEAL,
             side="bottom", callout_xy=(875, 432), token=TEAL, label="+"),
        Step("n9>n7", "n7", 0.35, 0.4, token=TEAL, label="+"),
        Step("n7>ch", "ch", 0.35, 0.9, "Delivered in-app", "Limit tools · no offer · logged for audit", TEAL,
             side="bottom", callout_xy=(1110, 432), token=TEAL, label="+"),
    ]),
]


# ------------------------------------------------------------------ frame
def frame(base, t, tl, story_t0, outro_t0):
    c = Canvas(W, H, base)
    st = Story.state_at(tl, t - story_t0) if story_t0 <= t < outro_t0 else None
    flow_all = t < story_t0 or t >= outro_t0
    cur_link = st["st"].link if st else None
    act_node = st["st"].node if st and st["phase"] == "dwell" else None
    act_amt = ease_out(min(1, st.get("age", 0) / 0.25)) if act_node else 0.0

    for name, (path, col) in LINKS.items():
        g = ease_out(window(t, link_start(name), link_start(name) + 0.45))
        flow = t if (flow_all or name == cur_link) else None
        draw_link(c, path, col, grow=g, flow_t=flow, dash=(6, 5) if name == "loop" else None)
    c.text(142, 520, "feeds back", 12, "bold", TEAL, anchor="rm",
           a=window(t, APPEAR["band"] + 0.5, APPEAR["band"] + 0.9))

    for x, lab, key in [(40, "Data", "d0"), (245, "Understand", "n1"), (505, "Decide", "n3"),
                        (765, "Protect", "n8"), (1025, "Deliver", "n7")]:
        section_label(c, x, 126, lab, a=window(t, APPEAR[key] - 0.1, APPEAR[key] + 0.3))

    draw_band(c, window(t, APPEAR["band"], APPEAR["band"] + 0.5))
    for i in range(5):
        on = 1.0 if (st and st["st"].link == f"d{i}>n1" and st["phase"] == "travel") else 0.0
        draw_chip(c, i, window(t, APPEAR[f"d{i}"], APPEAR[f"d{i}"] + 0.45), active=on)
    for k, n in N.items():
        draw_node(c, n, appear=window(t, APPEAR[k], APPEAR[k] + 0.45), active=act_amt if act_node == k else 0.0)

    has_meter = st and st["phase"] == "dwell" and st["st"].extra in (s1_score, s2_score)
    if not has_meter:
        churn_meter(c, 0.30, a=window(t, APPEAR["n2"] + 0.3, APPEAR["n2"] + 0.7))

    lit, lit_amt, lit_col = None, 0.0, GREEN
    if st and st["st"].node == "ch" and st["phase"] == "dwell":
        first = st["sc"] is SCENARIOS[0]
        lit, lit_amt, lit_col = (1 if first else 3), act_amt, (GREEN if first else TEAL)
    draw_channels(c, window(t, APPEAR["ch"], APPEAR["ch"] + 0.45), lit, lit_amt, lit_col)

    if st:
        s, sc = st["st"], st["sc"]
        tok_col, label = s.token or sc.color, s.label or sc.label
        if st["phase"] == "travel":
            draw_token(c, LINKS[s.link][0].at(st["u"]), tok_col, label)
        else:
            if s.extra:
                s.extra(c, st["u"])
            if s.title:
                n = N.get(s.node)
                ax, ay = s.callout_xy or (n.cx, n.y0)
                callout(c, ax, ay, s.title, s.body, s.color, appear=window(st["age"], 0.05, 0.35), side=s.side)
        caption_bar(c, 650, sc.name.upper(), sc.caption, sc.color)
    elif t < story_t0:
        caption_bar(c, 650, "ARCHITECTURE",
                    "One shared data layer · 10 agents · the RG Guardian can veto any message",
                    BLUE, appear=window(t, 2.3, 2.7))
    else:
        caption_bar(c, 650, "GOVERNANCE",
                    "People approve journeys and RG thresholds · every decision is logged and explainable", GREEN)
    return c.finish()


def main():
    base = background(W, H, BLUE)
    hc = Canvas(W, H, base)
    header(hc, "CRM AGENTS", "AI CRM architecture",
           "Player 360 → scoring → journeys → RG Guardian → delivery → uplift",
           BLUE, right=[("10 agents", BLUE), ("5 skills", VIOLET), ("1 workflow", GREEN)])
    base = hc.img

    story = Story(W, H, LINKS)
    tl, story_len = story.timeline(SCENARIOS)
    story_t0 = BUILD_END
    outro_t0 = story_t0 + story_len
    end_t = outro_t0 + 1.6

    if len(sys.argv) > 2 and sys.argv[1] == "--preview":  # --preview DIR t1 t2 ... (seconds)
        for ts in sys.argv[3:]:
            frame(base, float(ts), tl, story_t0, outro_t0).save(os.path.join(sys.argv[2], f"p_{ts}.png"))
        print(f"story {story_t0:.2f}-{outro_t0:.2f}s, end {end_t:.2f}s")
        return

    frames, durs = [], []
    dt = 1 / story.fps
    t = 0.0
    while t < end_t:
        frames.append(frame(base, t, tl, story_t0, outro_t0))
        durs.append(int(round(dt * 1000)))
        t += dt
    durs[-1] = 3200  # hold the last frame
    size = save_gif(frames, durs, OUT)
    print(f"{len(frames)} frames, {size / 1e6:.2f} MB -> {os.path.normpath(OUT)}")


if __name__ == "__main__":
    main()
