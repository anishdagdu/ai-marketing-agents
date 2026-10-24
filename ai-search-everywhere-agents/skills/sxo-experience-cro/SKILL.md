---
name: sxo-experience-cro
description: Search Experience Optimisation - check each landing page is the right page type for its keyword, serves each searcher persona, loads fast and converts, then build a CRO test backlog. Use for landing page conversion, intent mismatch, bounce rate, page speed or A/B tests on organic and AI traffic.
---
# SXO Experience & CRO (layer 5 of 5)

Shared rules: see `search-everywhere-workflow`.

Core idea: a page can score 95 on technical SEO and still fail because it's the **wrong page type** for the keyword.

## Inputs
Top landing pages + their main keyword (from SEO), conversion goal, analytics if available.

## Steps (per page)
1. **SERP backwards analysis**: search the keyword, classify the top 10 results by page type (product, category, comparison, listicle, guide, tool, local, video). Dominant type > 60% = strong consensus, 40-60% mixed, < 40% fragmented. Note SERP features, PAA, ad copy themes, AI Overview.
2. **Page-type match**:
   | Your page | SERP wants | Severity |
   |---|---|---|
   | Blog post | Product pages | Critical - build a product/category page |
   | Blog post | Comparison | High - restructure with a comparison table |
   | Product | Informational | High - add an educational section |
   | Landing page | Tool/calculator | High - add an interactive tool |
   | Service page | Local pack | Medium - add location signals |
3. **User stories** (3-5) from PAA, ads and related searches: "As a [persona], I want [goal], because [driver], but I'm blocked by [barrier]."
4. **Persona scoring**: 4-6 personas, each scored /25 on Relevance, Clarity (answer found in 10 s?), Trust, Action (clear next step). Fix the weakest persona first.
5. **Experience checks**: Core Web Vitals, mobile layout, one primary CTA above the fold with specific wording, trust (reviews, guarantees, returns, security), friction (form fields, popups, checkout steps).
6. **Test backlog**: hypothesis · change · metric · ICE score. One test per page at a time; set the sample size before starting.
7. **Measure AI traffic** separately: referrers chatgpt.com, perplexity.ai, gemini.google.com, copilot.microsoft.com, claude.ai.

## Score (0-100) - SXO gap score
Page type 15 · content depth 15 · UX/CTA 15 · schema 15 · media 15 · authority/trust 15 · freshness 10.
Report it next to the SEO score: high SEO + low SXO = technically fine but the wrong page.

## Output -> `findings/sxo.md`
Per page: SERP landscape · match verdict · user stories · persona cards · fixes · test backlog · limitations.
