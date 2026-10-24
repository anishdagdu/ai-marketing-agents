---
name: aeo-answer-optimizer
description: Answer Engine Optimisation - make pages the direct answer for featured snippets, People Also Ask, voice and Google AI Overviews, using answer-first blocks and currently supported schema. Use for snippets, FAQs, question-based content or AI Overviews.
---
# AEO Answer Optimizer (layer 2 of 5)

Shared rules: see `search-everywhere-workflow`.

## Inputs
Keyword clusters from SEO. Optional: PAA questions, support tickets, reviews, site search logs.

## Steps
1. **Collect questions**: People Also Ask, related searches, "how / what / why / best / vs / cost" variants, customer FAQs and tickets. Note which SERP feature each query shows (paragraph, list, table, video snippet, AI Overview).
2. **Answer blocks**: question as H2/H3, then a direct answer in the first 40-60 words ("X is ..." definition style), then detail. For AI citation, keep each full section self-contained at roughly 130-170 words with few pronouns and named entities.
   - Lists for steps, tables for comparisons, numbers with units and sources.
3. **Run the citability scorer** on each target page:
   `python3 scripts/citability_scorer.py <url>` (bundled in this skill folder) (needs `requests`, `beautifulsoup4`, `lxml`). It scores each block on answer quality, self-containment, readability, stats density and uniqueness. Rewrite blocks scoring < 60.
4. **Schema (current Google rules)**:
   - Use: Organization, WebSite, BreadcrumbList, Article (author as Person, `dateModified`), Product + Offer + AggregateRating, LocalBusiness, `speakable` for voice.
   - **HowTo**: Google removed HowTo rich results (Sept 2023). Keep step content on the page; don't expect a rich result.
   - **FAQPage**: rich results only for well-known government and health sites since Aug 2023. Q&A markup can still help machines read the page, but don't promise SERP display.
   - JSON-LD only, in the server HTML (not injected by JS), and only for content visible on the page.
5. **Validate**: tell the user to test with Google Rich Results Test and validator.schema.org.

## Score (0-100)
Question coverage 25 · answer-block quality (avg citability score) 35 · snippet-format match 20 · valid schema 20.

## Output -> `findings/aeo.md`
Per page: questions · rewritten answer blocks · JSON-LD · target feature. **Hand-off**: entity and authority gaps -> GEO.
