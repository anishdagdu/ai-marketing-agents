"""Builds the AvantStay agent pack from docs/teams.json.

Writes: agents/av-*.md (76), teams/<nn-slug>/README.md + workflow.gif (8),
workflow/avantstay-growth-workflow/SKILL.md, install.sh, README.md and
avantstay-agents-workflow.gif (the overall view).

Run: python3 avantstay-agents/docs/build.py [--no-gifs]   (needs Pillow and tools/gifkit.py)
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

# code, colour, icon, one-line goal (shown on the overall GIF and in the README)
META = {
    1: ("signal", BLUE, "gauge", "Rebuild tracking and attribution leadership trusts"),
    2: ("guest", AMBER, "search", "Fill homes through Search, PMax and Meta"),
    3: ("member", PINK, "heart", "Grow Members Club and referrals"),
    4: ("owner", GREEN, "user", "Lower the cost per signed homeowner"),
    5: ("buyer", VIOLET, "tag", "Sell the homes for sale and recruit agents"),
    6: ("hotel", CYAN, "cal", "Run hotel, OTA and metasearch ads"),
    7: ("corp", TEAL, "send", "Win company retreats and events"),
    8: ("ops", RED, "spark", "Ship creative, site tests and reporting"),
}
SOURCES = [("Segment + GA4", "chart"), ("BigQuery", "db"), ("Salesforce", "user"), ("Ad platforms", "bolt"),
           ("avantstay.com", "search")]


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


for t in TEAMS:
    t["code"], t["color"], t["icon"], t["goal"] = META[t["n"]]
    t["dir"] = f"{t['n']:02d}-{slug(t['name'])}"
    for a in t["agents"]:
        a["id"] = f"av-{t['code']}-{slug(a['name'])}"

GUARD = """## Guardrails
- You propose; a human approves. Never change a budget, bid, audience, tag, page or CRM record yourself. Write the proposed change, show it in full and wait for a clear yes in chat.
- Never upload personal data, send email or SMS, or publish a claim. Prepare the file or draft and hand it over.
- Use only prices, terms and proof numbers from the Terms and Claims Ledger (`av-signal-terms-and-claims-ledger`). If a number is not in the ledger, say so and ask.
- Base every figure on a tool call or a file you were given, not memory. Label each one as measured or estimated, and say when data is missing.
- Never enter passwords, card or bank details. Never delete data.
- Save your work in `outputs/` and end with: findings, proposals awaiting approval, and which agent should act next.
"""


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(text)


def build_files():
    for t in TEAMS:
        for a in t["agents"]:
            write(os.path.join(ROOT, "agents", a["id"] + ".md"), f"""---
name: {a['id']}
description: {a['name']} ({t['name']} team). {a['job']}. Use when the task needs: {a['output'].lower()}.
---

You are the {a['name']} on the {t['name']} team of the AvantStay performance marketing system.

## Your job
{a['job']}.

## Inputs and tools
{a['inputs']}.

## Output
{a['output']}.

## Team goal
{t['goal']}. The team answers this part of the role: {t['answers']}.

{GUARD}""")
        hooks = [h for h in DATA["hooks"][1:] if h[0] == t["name"]]
        hk = ""
        if hooks:
            hk = ("\n## Hooks and offers to test\n\nEvery row is a test idea, not a proven winner.\n\n"
                  "| Hook or offer | Modelled on | AvantStay number or term used |\n|---|---|---|\n"
                  + "".join(f"| {h[1]} | {h[2]} | {h[3]} |\n" for h in hooks))
        rows = "".join(f"| [`{a['id']}`](../../agents/{a['id']}.md) | {a['job']} | {a['inputs']} | {a['output']} |\n"
                       for a in t["agents"])
        write(os.path.join(ROOT, "teams", t["dir"], "README.md"), f"""# Team {t['n']}: {t['name']}

![{t['name']} workflow](workflow.gif)

**Goal:** {t['goal']}.

**Part of the role it answers:** {t['answers']}

**Offerings and audience:** {t['serves']}

## Agents ({len(t['agents'])})

| Agent | One-line job | Inputs / tools | Output |
|---|---|---|---|
{rows}{hk}
{t['note']}

[Back to all teams](../../README.md)
""")
    n = sum(len(t["agents"]) for t in TEAMS)
    trows = "".join(f"| {t['n']} | [{t['name']}](teams/{t['dir']}/) | {len(t['agents'])} | {t['goal']} | {t['serves']} |\n"
                    for t in TEAMS)
    gifs = "".join(f"### Team {t['n']}: {t['name']}\n\n![{t['name']}](teams/{t['dir']}/workflow.gif)\n\n"
                   f"[Agents, inputs and outputs →](teams/{t['dir']}/)\n\n" for t in TEAMS)
    write(os.path.join(ROOT, "README.md"), f"""# AvantStay Agents: A Performance Marketing Team of {n} AI Agents

![AvantStay agents workflow](avantstay-agents-workflow.gif)

Eight teams and {n} Claude Code agents, built as a performance marketing team for AvantStay. Each team owns one part of the growth plan and named offerings on avantstay.com: group homes, Members Club, homeowner management, homes for sale, hotels and company retreats.

> **Independent project.** This pack is a candidate's own design. It is not affiliated with, endorsed by or built for AvantStay, and it has not been run on AvantStay's accounts. Offering terms were read from public pages on 12 November 2026 and may have changed. Hooks and offers are test ideas with no performance data behind them.

> **AI proposes. You approve.** No agent changes a budget, publishes a claim, uploads personal data or sends a message. Each one writes a proposal for a human to approve.

## The eight teams

| # | Team | Agents | Goal | Offerings and audience |
|---|---|---|---|---|
{trows}
## How it works

1. **Data in.** Agents read Segment, GA4, BigQuery, Salesforce, the ad platforms and the public site.
2. **Team 1 goes first.** Signal and Measurement fixes tracking and sets one ledger of approved prices, terms and proof numbers. Every other agent must cite that ledger.
3. **Teams 2 to 7 work their audience.** Guests, members, homeowners, buyers, hotel guests and corporate planners each have a team.
4. **Team 8 ships and reports.** Creative, site tests, budget pacing and the weekly readout.
5. **One approval queue.** Every output lands as a proposal. A human approves it before anything changes.

The [`avantstay-growth-workflow`](workflow/avantstay-growth-workflow/SKILL.md) skill runs the teams in that order.

## Team workflows

{gifs}## Install

```bash
git clone https://github.com/anishdagdu/ai-marketing-agents.git
```

```bash
bash ai-marketing-agents/avantstay-agents/install.sh
```

Then start a new Claude Code session and say "run the AvantStay workflow", or call any agent by name, for example `av-signal-tag-and-consent-auditor`.

## Rebuild

`docs/teams.json` holds every team and agent. Edit it, then run:

```bash
python3 avantstay-agents/docs/build.py
```

That rewrites the agent files, the team pages and all nine GIFs.
""")
    order = "".join(f"{t['n']}. **{t['name']}** ({len(t['agents'])} agents): {t['goal'].lower()}. "
                    f"Agents: {', '.join('`' + a['id'] + '`' for a in t['agents'])}.\n" for t in TEAMS)
    write(os.path.join(ROOT, "workflow", "avantstay-growth-workflow", "SKILL.md"), f"""---
name: avantstay-growth-workflow
description: Runs the AvantStay performance marketing team end to end (measurement → guest demand → members → homeowners → buyers → hotels → corporate → creative and reporting) using the av-* agents. Use when the user says "run the AvantStay workflow", wants a full paid acquisition plan for guests or homeowners, or asks which av-* agent should handle a task.
---

# AvantStay growth workflow

Route the request to the right team, or run the teams in order for a full plan.

## Order

{order}
## Rules

- Start with Team 1 if tracking, attribution or the Terms and Claims Ledger is missing or stale. Scaling spend on bad numbers wastes money.
- Brief one to four agents per request. Give each the goal, the data it may read and the output you need.
- Collect every output into one ranked proposal list: what to change, expected effect, evidence, and who approves.
- Nothing is changed, sent or published without a clear yes from the user in chat.
- Label each figure as measured or estimated. Hooks and offers are test ideas until a test proves them.
""")
    write(os.path.join(ROOT, "install.sh"), f"""#!/bin/bash
# Installs the {n} AvantStay agents and the workflow skill into Claude Code.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.claude/agents ~/.claude/skills
cp "$DIR"/agents/*.md ~/.claude/agents/
cp -R "$DIR"/workflow/avantstay-growth-workflow ~/.claude/skills/
echo "Installed {n} agents + avantstay-growth-workflow. Start a new Claude Code session to use them."
""")
    return n


# ------------------------------------------------------------------ GIFs
W = 1280


def fit(c, s, size, weight, maxw):
    if c.text_w(s, size, weight) <= maxw:
        return s
    while s and c.text_w(s + "…", size, weight) > maxw:
        s = s[:-1]
    return s.rstrip(" ,;") + "…"


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
        header(c, f"TEAM {t['n']} OF 8", t["name"], fit(c, t["goal"] + ".  Serves: " + t["serves"], 15, "demi", 1190), col,
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
            c.rect(XA[0], y0, XA[1], y1, r=10, fill=mix(CARD, mix(WHITE, col, 0.10), act), outline=mix(LINE, col, 0.4 + 0.6 * act),
                   width=1.4, a=e)
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
            caption_bar(c, H - 62, "APPROVE", f"All {len(ag)} outputs wait in one queue. A human approves before anything changes.",
                        GREEN, 1.0, progress=1.0)
        elif f >= 4:
            caption_bar(c, H - 62, f"{k + 1} / {len(ag)}", fit(c, f"{ag[k]['name']}: {ag[k]['job'].lower()}", 16, "demi", 1080), col, 1.0,
                        progress=(f - 4) / (total - 4))
        frames.append(c.finish())
        durs.append(4000 if f >= total else 1000 // fps * (2 if (f - 4) % step == step - 1 else 1))
    return save_gif(frames, durs, os.path.join(ROOT, "teams", t["dir"], "workflow.gif"), colors=220)


def overall_gif():
    H = 720
    base = background(W, H, BLUE)
    n = sum(len(t["agents"]) for t in TEAMS)
    GX0, GW, GH, GAP = 250, 186, 196, 12
    cards = [(GX0 + (i % 4) * (GW + GAP), 150 + (i // 4) * (GH + GAP)) for i in range(8)]
    QX = 1070
    step, fps = 9, 10
    total = 6 + 8 * step
    frames, durs = [], []
    for f in range(total + 1):
        c = Canvas(W, H, base)
        header(c, "AVANTSTAY AGENTS", f"8 teams, {n} agents, one approval queue",
               "Each team owns one part of the growth plan and named offerings.", BLUE,
               right=[("AI proposes", BLUE), ("You approve", GREEN)])
        band(c, 30, 140, 232, 566, "Data in", DIM, clamp(f / 3))
        for i, (s, ic) in enumerate(SOURCES):
            chip(c, 42, 172 + i * 76, 220, 172 + i * 76 + 58, s, ic, BLUE, clamp((f - i * 0.6) / 3), size=12.5)
        band(c, QX - 12, 140, 1250, 566, "Approval queue", GREEN, clamp(f / 3))
        k = (f - 6) // step if f >= 6 else -1
        for i, t in enumerate(TEAMS):
            x, y = cards[i]
            ap = clamp((f - 1 - i * 0.5) / 3)
            if ap <= 0.01:
                continue
            act = 1.0 if i == k and f < total else 0.0
            col, e = t["color"], ease_out(ap)
            if act:
                c.glow(x, y, x + GW, y + GH, col, strength=0.9, spread=14)
            c.rect(x, y, x + GW, y + GH, r=14, fill=mix(CARD, mix(WHITE, col, 0.10), act), outline=mix(LINE, col, 0.35 + 0.65 * act),
                   width=1.5, a=e)
            c.circle(x + 30, y + 32, 16, fill=mix(WHITE, col, 0.16), a=e)
            icon(c, t["icon"], x + 30, y + 32, col, size=15, a=e)
            c.text(x + GW - 14, y + 32, f"TEAM {t['n']}", 11, "bold", col, anchor="rm", a=e)
            words, lines, cur = t["name"].split(), [], ""
            for w in words:
                if c.text_w((cur + " " + w).strip(), 15, "bold") > GW - 28:
                    lines.append(cur)
                    cur = w
                else:
                    cur = (cur + " " + w).strip()
            lines.append(cur)
            for j, ln in enumerate(lines[:2]):
                c.text(x + 14, y + 66 + j * 20, ln, 15, "bold", INK, a=e)
            gw, gl, cur = t["goal"].split(), [], ""
            for w in gw:
                if c.text_w((cur + " " + w).strip(), 11.5, "medium") > GW - 28:
                    gl.append(cur)
                    cur = w
                else:
                    cur = (cur + " " + w).strip()
            gl.append(cur)
            for j, ln in enumerate(gl[:3]):
                c.text(x + 14, y + 112 + j * 16, ln, 11.5, "medium", MUTED, a=e)
            c.pill(x + 14, y + GH - 32, f"{len(t['agents'])} agents", col, size=11, a=e)
            if i < k or f >= total:
                c.circle(x + GW - 22, y + GH - 21, 7, fill=GREEN)
        for i, t in enumerate(TEAMS):
            if i < k or f >= total or (i == k and (f - 6) % step >= 6):
                chip(c, QX, 172 + i * 48, 1238, 172 + i * 48 + 38, f"Team {t['n']} proposals", "check", t["color"], 1.0, size=12,
                     status=(GREEN, 1.0) if f >= total else None)
        if 0 <= k < 8 and f < total:
            t, p = TEAMS[k], ((f - 6) % step) / (step - 1)
            x, y = cards[k]
            a, m, b = (232, 172 + 2 * 76 + 29), (x + GW / 2, y + GH / 2), (QX, 172 + k * 48 + 19)
            q = ease_in_out(p)
            pos = (a[0] + (m[0] - a[0]) * q * 2, a[1] + (m[1] - a[1]) * q * 2) if q < 0.5 else \
                (m[0] + (b[0] - m[0]) * (q - 0.5) * 2, m[1] + (b[1] - m[1]) * (q - 0.5) * 2)
            draw_token(c, pos, t["color"], label=str(t["n"]))
            caption_bar(c, H - 118, f"TEAM {t['n']}", f"{t['name']}: {t['goal'].lower()} ({len(t['agents'])} agents).", t["color"], 1.0,
                        progress=(f - 6) / (total - 6))
        elif f >= total:
            caption_bar(c, H - 118, "APPROVE", f"{n} agents propose. A human approves every budget, claim and upload.", GREEN, 1.0, 1.0)
        c.text(W / 2, H - 40, "Independent project. Not affiliated with or endorsed by AvantStay.", 12, "medium", DIM, anchor="mm")
        frames.append(c.finish())
        durs.append(4000 if f >= total else 1000 // fps * (4 if f >= 6 and (f - 6) % step == step - 1 else 1))
    return save_gif(frames, durs, os.path.join(ROOT, "avantstay-agents-workflow.gif"), colors=128)


if __name__ == "__main__":
    print(build_files(), "agents written")
    if "--no-gifs" not in sys.argv:
        print("overall", overall_gif() // 1024, "KB")
        for t in TEAMS:
            print(t["dir"], team_gif(t) // 1024, "KB")
