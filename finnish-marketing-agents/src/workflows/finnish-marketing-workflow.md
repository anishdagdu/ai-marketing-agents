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
