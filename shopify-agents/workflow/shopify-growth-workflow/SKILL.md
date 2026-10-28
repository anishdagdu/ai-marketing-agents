---
name: shopify-growth-workflow
description: Runs the Shopify AI team end to end (store health → conversion → traffic → retention → profit loop) using the sh-* agents. Use when the user says "run the Shopify workflow", wants more Shopify revenue, asks what is wrong with their store, or wants a weekly store check.
---

# Shopify AI growth workflow

```
            ┌───────────────────────────┐
            │     sh-orchestrator       │  finds the biggest revenue leak,
            │  (routes + ranks actions) │  briefs the right agents
            └─────────────┬─────────────┘
                          ▼
 1 FIX THE STORE      sh-store-setup · sh-debugger · sh-catalog · sh-inventory
                          ▼
 2 CONVERT            sh-conversion · sh-support · sh-shipping-returns
                          ▼
 3 BRING TRAFFIC      sh-seo · sh-content-social · sh-paid-ads
                          ▼
 4 BRING THEM BACK    sh-email-sms · sh-retention-reviews
                          ▼
 5 MEASURE + PROFIT   sh-analytics-tracking · sh-profit-pricing ──▶ back to orchestrator (weekly)
```

## Steps
1. **Fix the store** – run `sh-store-setup` and `sh-debugger`. If checkout, tracking or key pages are broken, stop and fix those first: more traffic into a broken store wastes money. Then `sh-catalog` and `sh-inventory`.
2. **Convert** – run `sh-conversion` on the top product and collection pages. Use `sh-support` and `sh-shipping-returns` to remove the objections customers raise most.
3. **Bring traffic** – `sh-seo` and `sh-content-social` for organic, `sh-paid-ads` for paid. Paid only scales on products with stock and a margin above break-even.
4. **Bring them back** – `sh-email-sms` builds the core flows as drafts. `sh-retention-reviews` finds the best entry products and review angles.
5. **Measure and protect profit** – `sh-analytics-tracking` writes the weekly readout and `sh-profit-pricing` checks margin. The orchestrator turns both into next week's ranked actions. Schedule this with the `schedule` skill if the user asks.

## Guardrails (apply to every agent)
- Every write needs explicit user approval in chat. Show the full list of changes first.
- Content, discounts, campaigns and theme edits are drafts or on a duplicate theme. The user publishes, sends and changes budgets.
- Never enter credentials or payment details, never delete data.
- Name created assets with the prefix `AI · ` and tag them `ai-workflow`.
- Save outputs in `outputs/` so later steps and weekly runs can read them.

## Single requests
- "something is broken" → `sh-debugger`
- "visitors don't buy" → `sh-conversion`
- "ads are expensive" → `sh-paid-ads` + `sh-profit-pricing`
- "more organic traffic" → `sh-seo` / `sh-content-social`
- "set up abandoned cart" → `sh-email-sms`
- "what should I restock" → `sh-inventory`
- "how did last week go" → `sh-analytics-tracking`
