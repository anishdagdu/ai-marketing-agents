---
name: crm-agents-workflow
description: Runs the CRM Agents workflow end to end (Player 360 → scoring → journeys and triggers → RG Guardian → contact policy → personalisation → uplift, tests and weekly insights) using the crm-* agents. Use when the user says "run the CRM workflow", wants to win back churning players, move shop players to the app, or asks where to start with CRM.
---

# CRM Agents workflow

```
 DATA (gaming · retail card · app/web · payments · RG limits)
        │
 ┌──────▼─────────┐   ┌──────────────────┐
 │1 crm-player-360│──▶│2 crm-predictive- │
 │  (profiles)    │   │  scoring (NBA)   │
 └────────────────┘   └───┬──────────┬───┘
                ┌─────────▼──┐   ┌───▼───────────┐
                │3 journey-  │──▶│4 realtime-    │
                │ orchestrator│  │  trigger      │
                └─────┬──────┘   └──────┬────────┘
              ┌───────▼─────────────────▼───────┐
              │ 8 crm-rg-guardian  (VETO)        │ ← highest priority
              └───────────────┬─────────────────┘
              ┌───────────────▼─────────────────┐
              │ 9 crm-contact-policy (caps)      │
              └───────────────┬─────────────────┘
              ┌───────────────▼─────────────────┐
              │ 7 crm-personalisation (fi/sv/en) │
              └───────────────┬─────────────────┘
     ┌────────────────────────┼────────────────────────┐
 5 crm-uplift-analyst   6 crm-test-optimiser   10 crm-insights-calendar
     └──────────── learning loop back to DATA ─────────┘
```

## Steps
1. **Player 360:** run `crm-player-360`. If the RG-limit data is missing, **stop**. Nothing can be sent safely without it.
2. **Scoring:** run `crm-predictive-scoring`. Show the players per next best action.
3. **Plan:** run `crm-insights-calendar` for the calendar. Then run `crm-journey-orchestrator` for the user's goal and `crm-realtime-trigger` for any triggers. Show the drafts and **wait for approval**.
4. **Gatekeepers:** run `crm-rg-guardian` on the audience. Then run `crm-contact-policy` on what's left. Always in this order.
5. **Copy:** run `crm-personalisation` for the approved steps. Then run `crm-rg-guardian` again on the final messages.
6. **Hand-off:** export the final send list, copy and specs to `outputs/handoff/` for your CRM or ESP platform. The agents don't send.
7. **Learn:** after 14 days run `crm-uplift-analyst` and `crm-test-optimiser`. Every Monday run `crm-insights-calendar` for the weekly summary. Use the `schedule` skill if the user wants this automatic.

## Guardrails (every agent)
- **The RG Guardian can veto anything.** No other agent, test or revenue target can override it.
- Players at risk get care messages, never promotions. Target: 0% of at-risk players sent a promotion.
- People approve new journeys, triggers and any change to RG thresholds or caps.
- Every journey has a random control group. Results are reported as incremental uplift with confidence intervals.
- Every decision is logged with a reason in `outputs/` (Finnish gambling regulation and GDPR).
- No personal data in chat. Counts and segment names only.

## Single requests
- "who is about to churn" → step 2
- "build a shop-to-app journey" → step 3
- "is this campaign safe to send" → step 4
- "write the push copy" → step 5
- "did the win-back work" → step 7 (uplift)
- "weekly CRM report" or "why did Keno drop" → `crm-insights-calendar`
