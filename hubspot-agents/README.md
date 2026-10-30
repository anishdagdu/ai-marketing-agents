# HubSpot Agents: An AI Team for Your Whole HubSpot

![HubSpot agents workflow](hubspot-agents-workflow.gif)

Fifteen Claude Code agents and one workflow skill that run HubSpot end to end: CRM setup, data hygiene, lead capture, scoring, sales pipeline, SEO and AI search, social, ads, email, automation, help desk, reporting and revenue. They connect HubSpot with **Shopify** (orders and customers), **Stripe** (payments, MRR, churn) and **Slack** (alerts and weekly summaries). An orchestrator finds the biggest funnel leak each week and sends the right specialists after it.

> **AI recommends. You approve.** Nothing changes without your OK in chat. Emails, pages, workflows and sequences are saved as **drafts** or turned off. The agents never change ad budgets, never send emails, never post to Slack without a yes, never refund or charge in Stripe and never delete records.

## How it works

| Stage | Agent | What it does |
|---|---|---|
| Lead | [`hs-orchestrator`](agents/hs-orchestrator.md) | Finds the biggest funnel leak, briefs the right agents, returns one ranked action list |
| 1 Fix the CRM | [`hs-crm-setup`](agents/hs-crm-setup.md) | Objects, properties, lifecycle stages, pipelines, custom objects |
| | [`hs-data-hygiene`](agents/hs-data-hygiene.md) | Duplicates, missing fields, orphaned deals, timeline gaps |
| | [`hs-integrations`](agents/hs-integrations.md) | Shopify, Stripe and Slack sync, marketplace apps |
| 2 Convert | [`hs-forms-landing-pages`](agents/hs-forms-landing-pages.md) | Forms, pop-ups, landing pages |
| | [`hs-lead-scoring`](agents/hs-lead-scoring.md) | Segments, fit and engagement scores, MQL/SQL handoff |
| | [`hs-sales-pipeline`](agents/hs-sales-pipeline.md) | Deal pipelines, forecasting, sequences, meetings, templates |
| 3 Bring traffic | [`hs-seo-aeo`](agents/hs-seo-aeo.md) | SEO recommendations, topic clusters, AI-search visibility |
| | [`hs-social`](agents/hs-social.md) | Social calendar, publishing and reporting |
| | [`hs-ads`](agents/hs-ads.md) | Google, Meta, LinkedIn audience sync and ad ROI |
| 4 Bring them back | [`hs-email-marketing`](agents/hs-email-marketing.md) | Campaigns, personalization, A/B tests |
| | [`hs-workflows`](agents/hs-workflows.md) | Nurture, routing, Shopify and Stripe-triggered flows |
| | [`hs-service-helpdesk`](agents/hs-service-helpdesk.md) | Help desk, tickets, knowledge base, chatbots |
| 5 Measure revenue | [`hs-reporting-attribution`](agents/hs-reporting-attribution.md) | Dashboards, attribution, weekly readout |
| | [`hs-revenue-stripe`](agents/hs-revenue-stripe.md) | MRR, churn, failed payments, LTV, upsell segments |

The [`hubspot-growth-workflow`](workflow/hubspot-growth-workflow/SKILL.md) skill runs the stages in order. It stops at stage 1 if CRM data or integrations are broken, because bad data makes every later step wrong.

**Works with the rest of this repo:** `hs-ads` hands platform builds to [AI Paid Traffic](../ai-paid-traffic-agents/), `hs-seo-aeo` to [AI Search Everywhere](../ai-search-everywhere-agents/), `hs-social` to [Content Agents](../content-agents/), `hs-integrations` to [Shopify Agents](../shopify-agents/) and `hs-reporting-attribution` to the [GTM Health Agent](../gtm-health-agent/).

**Guardrails in every agent**
- Show the full list of changes before any write, send or Slack post
- Drafts or turned-off workflows for anything new; you publish, send and turn on
- Name everything created with the prefix `AI · ` and tag it `ai-workflow`
- Every number comes from a tool call, never from memory

## Requirements

- [Claude Code](https://claude.com/claude-code)
- The **HubSpot MCP connector**, signed in to your portal
- Optional: **Shopify** connector, **Stripe** connector (read only), **Slack** connector, Windsor.ai, Ahrefs or Semrush

## Install

```bash
./install.sh
```

Then, in a new Claude Code session, say **"run the HubSpot workflow"**. Or ask one agent directly, for example "use hs-sales-pipeline, which deals are stuck?" or "use hs-integrations, Shopify orders aren't showing in HubSpot".

## Files

- `agents/`: the 15 agent definitions
- `workflow/hubspot-growth-workflow/SKILL.md`: the orchestrator skill
- `hubspot-agents-workflow.gif`: workflow infographic
- `docs/make_gif.py`: regenerates the GIF (needs Pillow and `tools/gifkit.py`)
