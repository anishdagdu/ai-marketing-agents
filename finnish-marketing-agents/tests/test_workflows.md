# Workflow tests (finnish-marketing-orchestrator)

| Test | Pass if |
|---|---|
| Gates | Stops after research, strategy, calendar and final summary; waits for approval |
| Routing | "Translate this ad" goes straight to finnish-ads-copywriter, no research run |
| Hand-off | `ads-briefs.md` from step 3 is the input for step 4 (file path passed) |
| Parallel | All four platforms produced in step 4 |
| QA loop | An over-limit line is fixed within 2 rounds or reported as open |
| Consistency | Same prices, dates and offer in calendar and ads |
| No publishing | Nothing is uploaded or posted |
| Output paths | All files under `data/output/<brand>/<date>/` |
