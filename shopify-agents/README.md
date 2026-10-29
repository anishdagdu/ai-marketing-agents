# Shopify Agents: An AI Team That Runs Your Whole Store

![Shopify agents workflow](shopify-agents-workflow.gif)

Fifteen AI agents and one workflow skill. Together they look after the entire Shopify store: setup, debugging, catalog, inventory, conversion, organic and paid traffic, email and SMS, tracking, profit, support, shipping and retention. An orchestrator finds the biggest revenue leak each week and sends the right specialists after it.

> **AI recommends. You approve.** Nothing changes in your store without your OK in chat. New content, discounts, campaigns and theme edits are saved as **drafts** or on a duplicate theme. The agents never change ad budgets, never send emails, never enter payment details and never delete data.

## How it works

| Stage | Agent | What it does |
|---|---|---|
| Lead | [`sh-orchestrator`](agents/sh-orchestrator.md) | Finds the biggest revenue leak, briefs the right agents, returns one ranked action list |
| 1 Fix the store | [`sh-store-setup`](agents/sh-store-setup.md) | Settings, theme, policies, markets, payments, apps and sales channels checklist |
| | [`sh-debugger`](agents/sh-debugger.md) | Broken pages, checkout errors, app conflicts, sudden number drops: root cause and fix |
| | [`sh-catalog`](agents/sh-catalog.md) | Titles, descriptions, images, variants, collections and feed quality |
| | [`sh-inventory`](agents/sh-inventory.md) | Stockout and overstock risk, restock plan |
| 2 Convert | [`sh-conversion`](agents/sh-conversion.md) | Product pages, cart, checkout, upsells, speed and trust |
| | [`sh-support`](agents/sh-support.md) | Repeated questions, FAQs, reply templates, chatbot answers |
| | [`sh-shipping-returns`](agents/sh-shipping-returns.md) | Shipping cost, free-shipping threshold, return reasons, chargebacks |
| 3 Bring traffic | [`sh-seo`](agents/sh-seo.md) | Technical SEO, keywords, AI-search visibility |
| | [`sh-content-social`](agents/sh-content-social.md) | Blog and organic social calendar |
| | [`sh-paid-ads`](agents/sh-paid-ads.md) | Meta, Google and TikTok ROAS, wasted spend, creative tests, scaling |
| 4 Bring them back | [`sh-email-sms`](agents/sh-email-sms.md) | Klaviyo flows, campaigns and list growth |
| | [`sh-retention-reviews`](agents/sh-retention-reviews.md) | Cohorts, LTV, loyalty, reviews into marketing |
| 5 Measure + profit | [`sh-analytics-tracking`](agents/sh-analytics-tracking.md) | GA4, pixel and CAPI, UTMs, weekly readout |
| | [`sh-profit-pricing`](agents/sh-profit-pricing.md) | Margin per SKU, break-even ROAS, promos and pricing |

The [`shopify-growth-workflow`](workflow/shopify-growth-workflow/SKILL.md) skill runs the stages in order. It stops at stage 1 if checkout, tracking or key pages are broken, because sending traffic to a broken store wastes money.

**Works with the rest of this repo:** `sh-paid-ads` hands platform builds to [AI Paid Traffic](../ai-paid-traffic-agents/), `sh-seo` to [AI Search Everywhere](../ai-search-everywhere-agents/), `sh-content-social` to [Content Agents](../content-agents/), `sh-email-sms` to [Klaviyo 1PD Agents](../klaviyo-1pd-agents/) and `sh-analytics-tracking` to the [GTM Health Agent](../gtm-health-agent/).

**Guardrails in every agent**
- Show the full list of changes before any write
- Drafts or a duplicate theme for anything new; you publish, send and change budgets
- Name everything created with the prefix `AI · ` and tag it `ai-workflow`, so it's easy to audit or roll back
- Every number comes from a tool call, never from memory

## Requirements

- [Claude Code](https://claude.com/claude-code)
- The **Shopify MCP connector**, signed in to your store
- Optional, for the matching agents: Klaviyo connector, Windsor.ai (ads, GA4, Search Console), Ahrefs or Semrush

## Install

```bash
./install.sh
```

Then, in a new Claude Code session, say **"run the Shopify workflow"**. Or ask one agent directly, for example "use sh-debugger, checkout is failing" or "use sh-orchestrator, why is revenue flat?".

## Files

- `agents/`: the 15 agent definitions
- `workflow/shopify-growth-workflow/SKILL.md`: the orchestrator skill
- `shopify-agents-workflow.gif`: workflow infographic
- `docs/make_gif.py`: regenerates the GIF (needs Pillow)
