# Amazon Ads Agents: An AI Team for Amazon PPC

![Amazon Ads agents workflow](amazon-ads-agents-workflow.gif)

Twelve Claude Code agents and one workflow skill that set up and optimize Amazon Ads: Sponsored Products, Sponsored Brands, Sponsored Display and DSP. Setup runs once per launch; the optimize loop runs every Monday.

> **AI recommends. You approve.** The agents never upload or change anything in Amazon Ads. They write bulk-sheet-ready CSVs and a change log; you review and upload.

## How it works

| Stage | Agent | What it does |
|---|---|---|
| Setup | [`amz-product-research`](agents/amz-product-research.md) | Break-even ACoS, target ACoS, max CPC; tiers ASINs into Hero, Support, Hold |
| | [`amz-keyword-research`](agents/amz-keyword-research.md) | Keyword clusters by intent, relevance scores, starter negatives |
| | [`amz-competitor-intel`](agents/amz-competitor-intel.md) | Competitor ASINs to attack or avoid, brand defense |
| | [`amz-listing-readiness`](agents/amz-listing-readiness.md) | Retail readiness score /100; **gate**: fix the listing before spending |
| Build | [`amz-account-architect`](agents/amz-account-architect.md) | Portfolios, campaign structure, naming, budget split |
| | [`amz-sponsored-products`](agents/amz-sponsored-products.md) | SP bulk CSV with bids, bidding strategy, placements |
| | [`amz-sponsored-brands`](agents/amz-sponsored-brands.md) | Headline and video ads plus creative briefs |
| | [`amz-display-dsp`](agents/amz-display-dsp.md) | Retargeting, audiences, contextual; DSP plan above $10k/month |
| Optimize (weekly) | [`amz-search-term-harvest`](agents/amz-search-term-harvest.md) | Winning search terms → Exact; wasted terms → negatives |
| | [`amz-bid-optimizer`](agents/amz-bid-optimizer.md) | Target-ACoS bids and placement modifier shifts |
| | [`amz-budget-pacing`](agents/amz-budget-pacing.md) | Out-of-budget fixes, dayparting, Prime Day and BFCM ramps |
| | [`amz-reporting`](agents/amz-reporting.md) | ACoS, TACoS, ROAS, organic rank and next actions |

The [`amazon-ads-workflow`](workflow/amazon-ads-workflow/SKILL.md) skill runs the stages in order and stops at the listing gate if the product page isn't ready.

**Works with the rest of this repo:** the [Shopify Agents](../shopify-agents/) profit agent shares break-even math, [AI Search Everywhere](../ai-search-everywhere-agents/) keyword research seeds Amazon keywords, and [AI Paid Traffic](../ai-paid-traffic-agents/) creative briefs feed Sponsored Brands video.

**Guardrails in every agent**
- Bulk-ready CSVs only; you approve and upload
- Profit first: every decision is checked against break-even ACoS and target TACoS
- No decisions on thin data (10+ clicks, 7+ days, settled attribution); no entity changed twice in 7 days
- Every change logged in `outputs/optimization/change-log.csv`

## Requirements

- [Claude Code](https://claude.com/claude-code)
- Amazon Ads report exports (bulk sheet, Search Term, Targeting, Placement) and the Seller/Vendor Central Business Report
- Optional: Windsor.ai for automatic Amazon Ads and Seller Central data

## Install

```bash
./install.sh
```

Then, in a new Claude Code session, say **"run the Amazon Ads workflow"**. Or ask one agent directly, for example "use amz-bid-optimizer, ACoS is 45%".

## Files

- `agents/`: the 12 agent definitions
- `workflow/amazon-ads-workflow/SKILL.md`: the orchestrator skill
- `amazon-ads-agents-workflow.gif`: workflow infographic
- `docs/make_gif.py`: regenerates the GIF (needs Pillow)
