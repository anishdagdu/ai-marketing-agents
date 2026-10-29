---
name: amazon-ads-workflow
description: Runs the Amazon Ads AI team end to end (unit economics → keywords and competitors → listing gate → account build → weekly harvest, bid, budget and report loop) using the amz-* agents. Use when the user says "run the Amazon Ads workflow", is launching Amazon PPC, or wants a weekly Amazon Ads optimization.
---

# Amazon Ads AI workflow

```
 SETUP (once per launch)                     OPTIMIZE (every Monday)
 ───────────────────────                     ───────────────────────
 01 amz-product-research   (profit math)     09 amz-search-term-harvest ┐ parallel
 02 amz-keyword-research  ┐ parallel         10 amz-bid-optimizer       ┘
 03 amz-competitor-intel  ┘                  11 amz-budget-pacing
 04 amz-listing-readiness  ── GATE ──        12 amz-reporting
 05 amz-account-architect                          │
 06 amz-sponsored-products ┐                       ▼
 07 amz-sponsored-brands   │ parallel        you approve → upload bulk CSV
 08 amz-display-dsp        ┘                 → wait 7 days → repeat 09–12
          ▼
 you approve → upload bulk CSVs
```

## Modes
**Setup** – run 01, then 02 and 03 in parallel, then 04. If 04 says "Fix first", stop and show the fixes: ads only amplify a weak listing. Then 05, then 06/07/08 in parallel. Present the bulk files and launch checklist for approval.

**Optimize (weekly)** – needs fresh Search Term, Targeting, Placement and Business reports in `data/inputs/`. Run 09 and 10 in parallel, then 11, then 12. Schedule with the `schedule` skill if the user asks.

**Report** – 12 only.

## Guardrails (apply to every agent)
- Agents never upload or change anything in Amazon. They write bulk-ready CSVs; the user approves and uploads.
- Profit first: break-even ACoS and target TACoS from step 01 decide everything.
- Respect data thresholds (10+ clicks, 7+ days, settled attribution) and log every change in `outputs/optimization/change-log.csv`.

## Single requests
- "ACoS is too high" → `amz-bid-optimizer` then `amz-search-term-harvest`
- "running out of budget" / Prime Day → `amz-budget-pacing`
- "which keywords?" → `amz-keyword-research`
- "weekly report" → `amz-reporting`
