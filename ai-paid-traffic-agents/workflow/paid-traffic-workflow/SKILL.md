---
name: paid-traffic-workflow
description: Runs the full AI paid-traffic workflow end to end (research → strategy → creative → Meta/Google/TikTok → tracking → scale) using the 8 paid-traffic agents. Use when the user wants a full ads plan, a launch, or says "run the paid traffic workflow". Also routes single requests to the right agent.
---
# AI Paid Traffic workflow (orchestrator)

You coordinate 8 agents. Agents cannot call each other, so YOU launch each one with the Agent tool and pass work through files in `paid-traffic/` in the current folder.

## Step 0: Brief
Ask once, in a single message, for anything missing: product & URL, price/AOV & margin, monthly budget, platforms (Meta/Google/TikTok), goal (sales/leads), current results (if live), competitors, reviews. Write `paid-traffic/00-brief.md`. Fill gaps with stated assumptions; don't block.

## Pick a mode
- **Launch** (new account / new product): 1 → 2 → 3 → 4/5/6 → 7
- **Optimize** (already spending): 7 → 8 → (3 if fatigue found) → 2 (update testing roadmap)
- **Single task**: route to the one matching agent only.

## Stages
| # | Agent | Output |
|---|---|---|
| 1 | research-agent | 01-research.md |
| 2 | strategy-agent | 02-strategy.md |
| 3 | creative-agent | 03-creative.md |
| 4 | meta-ads-agent | 04-meta.md |
| 5 | google-ads-agent | 05-google.md |
| 6 | tiktok-ads-agent | 06-tiktok.md |
| 7 | tracking-agent | 07-tracking.md |
| 8 | scale-agent | 08-scale.md |

## Rules
- Run 1, 2, 3 in order (each needs the previous file). Run the platform agents 4/5/6 **in parallel**, only for platforms in the brief. Tracking (7) can run in parallel with 4-6.
- Each Agent prompt: the stage goal, "read paid-traffic/ first", and the user's specific request.
- **Checkpoint** after Strategy (2): show the KPI targets and budget split and get the user's OK before creative and builds.
- Quality gate after each stage: file exists, has summary + handoff, numbers agree with 02-strategy.md. If not, re-run that agent once with the specific fix.
- Nothing is launched, paused or changed in ad accounts by this workflow. Live changes need the user's explicit approval per change.

## Finish
Write `paid-traffic/00-action-plan.md`: this week's checklist (setup, creative to make, tests to launch, tracking fixes), KPI targets, and when to run Optimize mode next (usually weekly). Give the user a short summary and the file list.

## JEV model router
`pt-jev-router` picks a model for every task before the orchestrator starts it: **Fast · Haiku** for lookups, checks and formatting, **Standard · Sonnet** for plans, writing and analysis, **Deep · Opus** for high-stakes or messy problems. It scores each task 0-2 on money at stake, ambiguity, reasoning depth, blast radius and novelty (0-2 fast, 3-5 standard, 6+ deep), starts low and escalates only on evidence, reuses outputs from the last 7 days, and caps deep work at 3 tasks per run. Every decision is logged to `outputs/jev-routing-log.csv`.

Start every run with `pt-orchestrator`. It diagnoses, routes through JEV and ranks the results.
