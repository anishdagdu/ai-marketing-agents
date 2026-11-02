---
name: programmatic-growth-workflow
description: Runs the programmatic AI team end to end across CM360, DV360 and The Trade Desk (route → measure → plan → set up → buy → optimise → prove loop) using the pg-* agents and the JEV model router. Use when the user says "run the programmatic workflow", wants better DV360/TTD results, asks why CPA or reach changed, or wants a weekly programmatic check.
---

# Programmatic AI workflow (CM360 · DV360 · TTD) with JEV routing

```
          ┌───────────────────────────┐      ┌───────────────────────────┐
          │      pg-orchestrator      │ ───▶ │   pg-jev-router (JEV)     │
          │  finds the leak, briefs   │ ◀─── │ fast · standard · deep    │
          └─────────────┬─────────────┘      │ picks a model per task    │
                        ▼                    └───────────────────────────┘
 1 MEASURE FIRST   pg-floodlight-tracking · pg-verification · pg-cm360-trafficking
                        ▼
 2 PLAN            pg-media-planner · pg-audience-identity · pg-deals-supply
                        ▼
 3 BUY             pg-dv360-buyer · pg-ttd-buyer · pg-youtube-video · pg-ctv-audio-dooh · pg-retail-media
                        ▼
 4 OPTIMISE        pg-bidding-algorithms · pg-frequency-reach · pg-pacing-budget · pg-dynamic-creative
                        ▼
 5 PROVE           pg-attribution-dedup · pg-incrementality-lift · pg-clean-room-reporting ──▶ back to orchestrator (weekly)
```

## Steps
0. **Route** – the orchestrator lists the tasks and asks `pg-jev-router` for a tier per task. Start each agent with that `model`. Fast = haiku, standard = sonnet, deep = opus.
1. **Measure first** – `pg-floodlight-tracking`, `pg-verification` and `pg-cm360-trafficking` QA. If Floodlights are broken, CM360 and DSP conversions differ by more than 20%, or IVT is above 5%, stop and fix these first.
2. **Plan** – `pg-media-planner` sets goals and the DV360/TTD split; `pg-audience-identity` and `pg-deals-supply` pick who and where.
3. **Buy** – `pg-dv360-buyer` and `pg-ttd-buyer` build the structure **paused**; channel specialists handle YouTube, CTV/audio/DOOH and retail data.
4. **Optimise** – `pg-bidding-algorithms`, `pg-frequency-reach`, `pg-pacing-budget` and `pg-dynamic-creative`. Anything moving more than 10% of spend is routed to deep by JEV.
5. **Prove** – `pg-attribution-dedup` sets the source of truth, `pg-incrementality-lift` designs lift tests, `pg-clean-room-reporting` writes the weekly readout with JEV's cost summary. The orchestrator turns it into next week's ranked actions. Schedule with the `schedule` skill if the user asks.

## JEV efficiency rules
- Start low, escalate on evidence (low confidence or conflicting data → one tier up).
- Split a task into cheap and expensive parts before upgrading it.
- Reuse outputs from the last 7 days instead of rerunning.
- Batch fast-tier QA checks; cap deep tasks at 3 per weekly run.
- Log every decision to `outputs/jev-routing-log.csv`.

## Guardrails (apply to every agent)
- Every write in CM360, DV360 or TTD needs explicit approval in chat. Show the full list of changes first.
- Never launch, unpause or change budgets. New items are built paused or as drafts.
- Never accept deal terms, enter credentials or payment details, or delete data.
- Name created items with the prefix `AI · ` and tag them `ai-workflow`.
- Save outputs in `outputs/` so later steps and weekly runs can read them.

## Single requests
- "conversions don't match" → `pg-floodlight-tracking` + `pg-attribution-dedup`
- "CPA went up" → `pg-bidding-algorithms` + `pg-verification`
- "we're underspending" → `pg-pacing-budget`
- "same people see our ads too often" → `pg-frequency-reach`
- "plan next quarter" → `pg-media-planner`
- "is programmatic actually working" → `pg-incrementality-lift`
- "why is the AI bill high" → `pg-jev-router`
