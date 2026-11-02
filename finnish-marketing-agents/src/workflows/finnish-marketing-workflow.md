# Workflow: Finnish marketing (end to end)

Run by `finnish-marketing-orchestrator`. Each gate waits for the user.

| # | Step | Agent | Input | Output (in `data/output/<brand>/<date>/`) | Gate |
|---|---|---|---|---|---|
| 0 | Brief | orchestrator | `prompts/templates/brief.md` | `brief.md` | — |
| 1 | Research: website, competitor sentiment, Meta Ad Library | finnish-content-calendar | brief | `research.md` | Gate 1 |
| 2 | Strategy: pillars, channel mix, organic vs paid | finnish-content-calendar | research | `strategy.md` | Gate 2 |
| 3 | Calendar (fi + en) and paid briefs | finnish-content-calendar | strategy | `calendar.csv`, `ads-briefs.md` | Gate 3 |
| 4 | Ad copy: Google, Meta, LinkedIn, Snapchat (parallel) | finnish-ads-copywriter | ads-briefs | `ads/<platform>.md` (+ CSV) | — |
| 5 | Translation & QA: fi⇄en, char limits, compliance, consistency | finnish-ads-copywriter + `src/utils/char_count.py` | ads, calendar | `qa-report.md` | — |
| 6 | Approval | user | summary | — | Gate 4 |
| 7 | Measure: results → new briefs (monthly loop to step 1/3/4) | orchestrator | exports in `data/input/` | `results-<date>.md` | — |

Failure handling: if QA fails, send the fix list back to the agent (max 2 rounds), then report open items.

## JEV model router
`finnish-jev-router` picks a model for every task before the orchestrator starts it: **Fast · Haiku** for lookups, checks and formatting, **Standard · Sonnet** for plans, writing and analysis, **Deep · Opus** for high-stakes or messy problems. It scores each task 0-2 on money at stake, ambiguity, reasoning depth, blast radius and novelty (0-2 fast, 3-5 standard, 6+ deep), starts low and escalates only on evidence, reuses outputs from the last 7 days, and caps deep work at 3 tasks per run. Every decision is logged to `outputs/jev-routing-log.csv`.
