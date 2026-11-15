"""Builds the Carry1st agent pack from docs/teams.json.

Writes: agents/c1-*.md (139), teams/<nn-slug>/README.md + workflow.gif (12),
workflow/carry1st-growth-workflow/SKILL.md, install.sh, README.md and
carry1st-agents-workflow.gif (the overall view).

Run: python3 carry1st-agents/docs/build.py [--no-gifs]   (needs Pillow and tools/gifkit.py)
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from gifkit import *  # noqa: E402,F403

DATA = json.load(open(os.path.join(HERE, "teams.json")))
TEAMS = DATA["teams"]
NT = len(TEAMS)

INDIGO, ORANGE, LIME, SLATE = (79, 70, 229), (234, 88, 12), (101, 163, 13), (71, 85, 105)

# code, colour, icon
META = {
    1: ("command", BLUE, "route"),
    2: ("measure", TEAL, "gauge"),
    3: ("intel", VIOLET, "search"),
    4: ("creative", PINK, "video"),
    5: ("google", AMBER, "bolt"),
    6: ("meta", INDIGO, "user"),
    7: ("tiktok", RED, "spark"),
    8: ("crm", CYAN, "mail"),
    9: ("shop", GREEN, "tag"),
    10: ("discover", LIME, "filter"),
    11: ("community", ORANGE, "heart"),
    12: ("b2b", SLATE, "send"),
}
SOURCES = [("Shop orders + payments", "tag"), ("MMP + app events", "chart"), ("Google, Meta, TikTok", "bolt"),
           ("CRM + WhatsApp", "mail"), ("Market + community", "search")]


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


for t in TEAMS:
    t["code"], t["color"], t["icon"] = META[t["n"]]
    t["goal"] = t["mission"]
    t["dir"] = f"{t['n']:02d}-{slug(t['name'])}"
    for a in t["agents"]:
        a["id"] = f"c1-{t['code']}-{slug(a['name'])}"

GUARD = """## Guardrails
- You propose; a human approves. Never change a budget, bid, audience, price, offer, page or customer record yourself. Write the proposed change, show it in full and wait for a clear yes in chat.
- Paid media is Google, Meta and TikTok only. Only the platform writer agents (`c1-google-google-writer`, `c1-meta-meta-writer`, `c1-tiktok-tiktok-writer`) prepare ad account changes, and only after Growth Command approves them.
- Never send a message, upload personal data or publish anything. Prepare the draft or file and hand it over. Marketing sends need a valid consent record.
- Use the blended view from the Measurement team for every CAC, payback and repeat-rate figure. Label each number as measured or estimated, and say when data is missing.
- Base every figure on a tool call or a file you were given, not memory. Never enter passwords, card or bank details. Never delete data.
- Save your work in `outputs/` and end with: findings, proposals awaiting approval, and which agent should act next.
"""

NOTE = ("> **Independent project.** This pack is a candidate's own design. It is not affiliated with, endorsed by or built "
        "for Carry1st, and it has not been run on Carry1st's accounts. Company facts were read from public pages on "
        "14 November 2026 and may have changed. Workflows and KPIs are a recommended design with no performance data "
        "behind them.")


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(text)


def build_files():
    for t in TEAMS:
        for a in t["agents"]:
            write(os.path.join(ROOT, "agents", a["id"] + ".md"), f"""---
name: {a['id']}
description: {a['name']} ({t['name']} team). {a['job']}. Use when the task needs: {a['output']}.
---

You are the {a['name']} on the {t['name']} team of the Carry1st growth engine.

## Your job
{a['job']}.

## Inputs and tools
{a['inputs']}.

## Output
{a['output']}.

## Team goal
{t['goal']}. The team works most closely with: {t['works_with']}.

{GUARD}""")
        rows = "".join(f"| [`{a['id']}`](../../agents/{a['id']}.md) | {a['job']} | {a['inputs']} | {a['output']} |\n"
                       for a in t["agents"])
        wf = "".join(f"| {w['name']} | {w['trigger']} | {w['inputs']} | {w['handoffs']} | {w['output']} | {w['gate']} |\n"
                     for w in t["workflows"])
        kp = "".join(f"- {k.strip()[0].upper() + k.strip()[1:]}\n" for k in t["kpis"].split(";"))
        write(os.path.join(ROOT, "teams", t["dir"], "README.md"), f"""# Team {t['n']}: {t['name']}

![{t['name']} workflow](workflow.gif)

**Goal:** {t['goal']}.

**Works with:** {t['works_with']}

## Agents ({len(t['agents'])})

| Agent | One-line job | Inputs / tools | Output |
|---|---|---|---|
{rows}
## Workflows

| Workflow | Trigger | Inputs | Hand-offs | Output | Human gate |
|---|---|---|---|---|---|
{wf}
## KPIs

{kp}
[Back to all teams](../../README.md)
""")
    n = sum(len(t["agents"]) for t in TEAMS)
    trows = "".join(f"| {t['n']} | [{t['name']}](teams/{t['dir']}/) | {len(t['agents'])} | {t['goal']} | {t['works_with']} |\n"
                    for t in TEAMS)
    gifs = "".join(f"### Team {t['n']}: {t['name']}\n\n![{t['name']}](teams/{t['dir']}/workflow.gif)\n\n"
                   f"[Agents, workflows and KPIs →](teams/{t['dir']}/)\n\n" for t in TEAMS)
    write(os.path.join(ROOT, "README.md"), f"""# Carry1st Agents: One Growth Engine of {n} AI Agents

![Carry1st agents workflow](carry1st-agents-workflow.gif)

Twelve teams and {n} Claude Code agents, built as one growth engine for Carry1st: the Carry1st Shop (game top-ups and vouchers), Pay1st payments, Flow1st distribution and Publishing. Paid media is Google, Meta and TikTok only. The engine is organised around one event: a player's first, second and third purchase on the Shop.

{NOTE}

> **AI proposes. You approve.** No agent changes a budget, price or offer, sends a message, uploads personal data or publishes anything. Each one writes a proposal for a human to approve.

## The twelve teams

| # | Team | Agents | Goal | Works with |
|---|---|---|---|---|
{trows}
## How it works

1. **Data in.** Agents read Shop orders and payments, app and attribution data, the three ad platforms, CRM and WhatsApp, and market and community signals.
2. **Growth Command leads.** Team 1 keeps the beat calendar, the budget plan, the change ledger and the consent record. Every write proposal goes through it.
3. **Measurement sets the numbers.** Team 2 publishes one blended view of CAC, payback and repeat purchase. Every other agent cites it.
4. **Intelligence and Creative supply the rest.** Team 3 feeds insights; Team 4 turns them into creative for every channel.
5. **Three platform teams, one writer each.** Google, Meta and TikTok each have exactly one agent that prepares account changes, so two agents never change the same budget.
6. **Owned growth runs alongside.** Lifecycle, Shop, Discovery, Creators and B2B work the same beats as the paid teams.
7. **One approval queue.** Every output lands as a proposal. A human approves it before anything changes.

The [`carry1st-growth-workflow`](workflow/carry1st-growth-workflow/SKILL.md) skill runs the teams in that order.

**North-star metric:** the share of new Shop buyers who reach a third purchase, with blended first-purchase CAC and payback as the cost side. This is a hypothesis to check on real cohorts.

**Run it lean.** {n} is a count of defined roles, not of agents to run at once. Brief one to four agents per request; the full research behind the design is in [the report](../reports/Carry1st%20AI%20growth%20engine%20teams.md).

## Team workflows

{gifs}## Install

```bash
git clone https://github.com/anishdagdu/ai-marketing-agents.git
```

```bash
bash ai-marketing-agents/carry1st-agents/install.sh
```

Then start a new Claude Code session and say "run the Carry1st workflow", or call any agent by name, for example `c1-command-budget-allocator`.

## Rebuild

`docs/teams.json` holds every team, agent, workflow and KPI. Edit it, then run:

```bash
python3 carry1st-agents/docs/build.py
```

That rewrites the agent files, the team pages and all {NT + 1} GIFs.
""")
    order = "".join(f"{t['n']}. **{t['name']}** ({len(t['agents'])} agents): {t['goal'][0].lower() + t['goal'][1:]}. "
                    f"Agents: {', '.join('`' + a['id'] + '`' for a in t['agents'])}.\n" for t in TEAMS)
    flows = "".join(f"- **{t['name']}:** " + "; ".join(f"{w['name']} ({w['trigger']})"
                                                      for w in t["workflows"]) + ".\n" for t in TEAMS)
    write(os.path.join(ROOT, "workflow", "carry1st-growth-workflow", "SKILL.md"), f"""---
name: carry1st-growth-workflow
description: Runs the Carry1st growth engine end to end (growth command → measurement → intelligence → creative → Google, Meta and TikTok → lifecycle → shop → discovery → creators → B2B) using the c1-* agents. Use when the user says "run the Carry1st workflow", wants a growth plan for the Carry1st Shop, Pay1st or Flow1st, or asks which c1-* agent should handle a task.
---

# Carry1st growth workflow

Route the request to the right team, or run the teams in order for a full plan.

## Order

{order}
## Workflows by team

{flows}
## Rules

- Start with Team 2 if tracking, the blended view or identity matching is missing or stale. Scaling spend on bad numbers wastes money.
- Paid media is Google, Meta and TikTok only. Each platform has one writer agent; every account change goes through Growth Command first.
- TikTok plans must pass `c1-tiktok-country-eligibility-guard` before any other TikTok work.
- Brief one to four agents per request. Give each the goal, the data it may read and the output you need.
- Collect every output into one ranked proposal list: what to change, expected effect, evidence, and who approves.
- Nothing is changed, sent or published without a clear yes from the user in chat.
- Label each figure as measured or estimated.
""")
    write(os.path.join(ROOT, "install.sh"), f"""#!/bin/bash
# Installs the {n} Carry1st agents and the workflow skill into Claude Code.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.claude/agents ~/.claude/skills
cp "$DIR"/agents/*.md ~/.claude/agents/
cp -R "$DIR"/workflow/carry1st-growth-workflow ~/.claude/skills/
echo "Installed {n} agents + carry1st-growth-workflow. Start a new Claude Code session to use them."
""")
    os.chmod(os.path.join(ROOT, "install.sh"), 0o755)
    return n


# ------------------------------------------------------------------ GIFs
W = 1280


def fit(c, s, size, weight, maxw):
    if c.text_w(s, size, weight) <= maxw:
        return s
    while s and c.text_w(s + "…", size, weight) > maxw:
        s = s[:-1]
    return s.rstrip(" ,;") + "…"


def wrap(c, s, size, weight, maxw):
    lines, cur = [], ""
    for w in s.split():
        if cur and c.text_w(cur + " " + w, size, weight) > maxw:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    lines.append(cur)
    return lines


def team_gif(t):
    ag, col = t["agents"], t["color"]
    RH, Y0 = 46, 168
    H = Y0 + len(ag) * RH + 78
    base = background(W, H, col)
    XI, XA, XO = (40, 350), (400, 890), (940, 1240)
    step, fps = 5, 10
    total = 4 + len(ag) * step
    frames, durs = [], []
    for f in range(total + 1):
        c = Canvas(W, H, base)
        header(c, f"TEAM {t['n']} OF {NT}", t["name"],
               fit(c, t["goal"] + ".  Works with: " + t["works_with"], 15, "demi", 1190), col,
               right=[(f"{len(ag)} agents", col)])
        for x, lab in ((XI[0], "Inputs and tools"), (XA[0], "Agent and one-line job"), (XO[0], "Output")):
            section_label(c, x + 4, 140, lab, DIM)
        for i, a in enumerate(ag):
            p = (f - 4 - i * step) / step  # 0..1 while this row is the active one
            if p < 0:
                continue
            ap = clamp(p * 2.5)
            act = 1.0 if 0 <= p < 1 and f < total else 0.0
            y0 = Y0 + i * RH
            y1 = y0 + RH - 8
            ym = (y0 + y1) / 2
            chip(c, XI[0], y0, XI[1], y1, fit(c, a["inputs"], 12.5, "demi", 280), None, col, ap, act * 0.6, 12.5)
            e = ease_out(ap)
            if act:
                c.glow(XA[0], y0, XA[1], y1, col, strength=0.8, spread=12)
            c.rect(XA[0], y0, XA[1], y1, r=10, fill=mix(CARD, mix(WHITE, col, 0.10), act),
                   outline=mix(LINE, col, 0.4 + 0.6 * act), width=1.4, a=e)
            c.rect(XA[0], y0, XA[0] + 5, y1, r=2, fill=col, a=e)
            c.text(XA[0] + 16, ym - 8, a["name"], 13.5, "bold", INK, anchor="lm", a=e)
            c.text(XA[0] + 16, ym + 9, fit(c, a["job"], 11.5, "medium", 460), 11.5, "medium", MUTED, anchor="lm", a=e)
            done = (WHITE, 0) if p < 1 and f < total else (GREEN, 1.0)
            chip(c, XO[0], y0, XO[1], y1, fit(c, a["output"], 12.5, "demi", 262), None, col, clamp((p - 0.3) * 2.5),
                 act * 0.6, 12.5, status=done if done[1] else None)
            for (xa, xb), lo in (((XI[1], XA[0]), 0.0), ((XA[1], XO[0]), 0.3)):
                g = clamp((p - lo) * 3)
                if g > 0:
                    c.line([(xa + 6, ym), (xa + 6 + (xb - xa - 14) * g, ym)], mix(LINE, col, 0.6), width=2, a=0.9)
                    if g >= 1:
                        c.arrowhead((xb - 6, ym), (xb - 20, ym), mix(LINE, col, 0.6), size=7)
            if act:
                draw_token(c, (XI[1] + (XO[0] - XI[1]) * ease_in_out(clamp(p * 1.25)), ym), col, label=str(i + 1))
        k = min(len(ag) - 1, max(0, (f - 4) // step))
        if f >= total:
            caption_bar(c, H - 62, "APPROVE",
                        f"All {len(ag)} outputs wait in one queue. A human approves before anything changes.",
                        GREEN, 1.0, progress=1.0)
        elif f >= 4:
            caption_bar(c, H - 62, f"{k + 1} / {len(ag)}",
                        fit(c, f"{ag[k]['name']}: {ag[k]['job'][0].lower() + ag[k]['job'][1:]}", 16, "demi", 1080), col, 1.0,
                        progress=(f - 4) / (total - 4))
        frames.append(c.finish())
        durs.append(4000 if f >= total else 1000 // fps * (2 if (f - 4) % step == step - 1 else 1))
    return save_gif(frames, durs, os.path.join(ROOT, "teams", t["dir"], "workflow.gif"), colors=220)


def overall_gif():
    H = 810
    base = background(W, H, BLUE)
    n = sum(len(t["agents"]) for t in TEAMS)
    GX0, GW, GH, GAP = 250, 186, 160, 12
    cards = [(GX0 + (i % 4) * (GW + GAP), 150 + (i // 4) * (GH + GAP)) for i in range(NT)]
    BY1 = 150 + 3 * GH + 2 * GAP + 12
    QX, QS = 1070, 40
    step, fps = 8, 10
    total = 6 + NT * step
    frames, durs = [], []
    for f in range(total + 1):
        c = Canvas(W, H, base)
        header(c, "CARRY1ST AGENTS", f"{NT} teams, {n} agents, one growth engine",
               "Built around the first, second and third purchase on the Carry1st Shop. Ads on Google, Meta and TikTok.",
               BLUE, right=[("AI proposes", BLUE), ("You approve", GREEN)])
        band(c, 30, 140, 232, BY1, "Data in", DIM, clamp(f / 3))
        for i, (s, ic) in enumerate(SOURCES):
            chip(c, 42, 176 + i * 92, 220, 176 + i * 92 + 62, s, ic, BLUE, clamp((f - i * 0.6) / 3), size=11.5)
        band(c, QX - 12, 140, 1250, BY1, "Approval queue", GREEN, clamp(f / 3))
        k = (f - 6) // step if f >= 6 else -1
        for i, t in enumerate(TEAMS):
            x, y = cards[i]
            ap = clamp((f - 1 - i * 0.35) / 3)
            if ap <= 0.01:
                continue
            act = 1.0 if i == k and f < total else 0.0
            col, e = t["color"], ease_out(ap)
            if act:
                c.glow(x, y, x + GW, y + GH, col, strength=0.9, spread=14)
            c.rect(x, y, x + GW, y + GH, r=14, fill=mix(CARD, mix(WHITE, col, 0.10), act),
                   outline=mix(LINE, col, 0.35 + 0.65 * act), width=1.5, a=e)
            c.circle(x + 26, y + 26, 14, fill=mix(WHITE, col, 0.16), a=e)
            icon(c, t["icon"], x + 26, y + 26, col, size=13, a=e)
            c.text(x + GW - 14, y + 26, f"TEAM {t['n']}", 11, "bold", col, anchor="rm", a=e)
            for j, ln in enumerate(wrap(c, t["name"], 14, "bold", GW - 26)[:2]):
                c.text(x + 14, y + 48 + j * 18, ln, 14, "bold", INK, a=e)
            gl = wrap(c, t["goal"], 11, "medium", GW - 26)
            if len(gl) > 2:
                gl = [gl[0], fit(c, " ".join(gl[1:]), 11, "medium", GW - 26)]
            for j, ln in enumerate(gl):
                c.text(x + 14, y + 92 + j * 15, ln, 11, "medium", MUTED, a=e)
            c.pill(x + 14, y + GH - 30, f"{len(t['agents'])} agents", col, size=10.5, a=e)
            if i < k or f >= total:
                c.circle(x + GW - 22, y + GH - 19, 7, fill=GREEN)
        for i, t in enumerate(TEAMS):
            if i < k or f >= total or (i == k and (f - 6) % step >= 5):
                chip(c, QX, 174 + i * QS, 1238, 174 + i * QS + 32, f"Team {t['n']} proposals", "check", t["color"], 1.0,
                     size=11.5, status=(GREEN, 1.0) if f >= total else None)
        if 0 <= k < NT and f < total:
            t, p = TEAMS[k], ((f - 6) % step) / (step - 1)
            x, y = cards[k]
            a, m, b = (232, 176 + 2 * 92 + 31), (x + GW / 2, y + GH / 2), (QX, 174 + k * QS + 16)
            q = ease_in_out(p)
            pos = (a[0] + (m[0] - a[0]) * q * 2, a[1] + (m[1] - a[1]) * q * 2) if q < 0.5 else \
                (m[0] + (b[0] - m[0]) * (q - 0.5) * 2, m[1] + (b[1] - m[1]) * (q - 0.5) * 2)
            draw_token(c, pos, t["color"], label=str(t["n"]))
            caption_bar(c, H - 118, f"TEAM {t['n']}",
                        fit(c, f"{t['name']}: {t['goal'][0].lower() + t['goal'][1:]} ({len(t['agents'])} agents).", 16,
                            "demi", 1080), t["color"], 1.0, progress=(f - 6) / (total - 6))
        elif f >= total:
            caption_bar(c, H - 118, "APPROVE", f"{n} agents propose. A human approves every budget, price, send and post.",
                        GREEN, 1.0, 1.0)
        c.text(W / 2, H - 40, "Independent project. Not affiliated with or endorsed by Carry1st.", 12, "medium", DIM,
               anchor="mm")
        frames.append(c.finish())
        durs.append(4000 if f >= total else 1000 // fps * (4 if f >= 6 and (f - 6) % step == step - 1 else 1))
    return save_gif(frames, durs, os.path.join(ROOT, "carry1st-agents-workflow.gif"), colors=128)


if __name__ == "__main__":
    print(build_files(), "agents written")
    if "--no-gifs" not in sys.argv:
        print("overall", overall_gif() // 1024, "KB")
        for t in TEAMS:
            print(t["dir"], team_gif(t) // 1024, "KB")
