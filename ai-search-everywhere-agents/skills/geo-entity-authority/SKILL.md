---
name: geo-entity-authority
description: Generative Engine Optimisation - get cited and recommended by ChatGPT, Perplexity, Gemini, Claude, Copilot and Google AI Overviews through citable content, E-E-A-T, off-site authority and platform-specific tactics. Use for AI search visibility, AI citations or "why doesn't ChatGPT mention us".
---
# GEO Entity & Authority (layer 3 of 5)

Shared rules: see `search-everywhere-workflow`.

## Inputs
Brand, category, competitors, 10-30 buyer prompts ("best X for Y", "X vs Y", "is X worth it", "X alternatives"). Brand facts from AIO.

## Steps
1. **Prompt benchmark**: run each prompt in each engine 3 times (answers vary). Record: mentioned? rank in answer? cited URL? sentiment? competitors named? If you can't query an engine, give the user the prompt sheet and mark that cell "not checked".
   Share of voice = brand mentions / all brand mentions in the answer set.
2. **Cited sources**: list every domain the engines cite. These are the off-site targets.
3. **Citable content**: run `python3 scripts/citability_scorer.py <url>` (bundled in this skill folder) on key pages. Fix blocks < 60 by adding:
   - Original stats and data with sources, expert quotes, named entities (the 2023 GEO paper found these lift visibility the most; keyword stuffing doesn't).
   - "Our data shows..." / case studies with numbers.
4. **E-E-A-T** (score each 0-25): Experience (first-hand, case studies), Expertise (named author, credentials, Person schema), Authority (about page, media mentions, `sameAs`), Trust (HTTPS, contact, policies, sources, update dates).
5. **Platform tactics** (engines overlap little - optimise each):
   - Google AI Overviews: rank in top 10 first; question headings, direct answers, tables.
   - ChatGPT: entity clarity (Wikipedia/Wikidata, `sameAs`), factual attributed statements, OAI-SearchBot allowed.
   - Perplexity: community proof (Reddit, Quora, forums), fresh dated content, PerplexityBot allowed.
   - Gemini / Copilot: Google / Bing index health, YouTube (Gemini), Bing Webmaster + IndexNow (Copilot).
6. **Off-site plan**: get onto cited listicles and review sites, genuine community answers, YouTube explainers/reviews, digital PR. Never fake reviews or astroturf.

## Score (0-100)
Citability 30 · E-E-A-T 25 · share of voice 25 · platform readiness 20.

## Output -> `findings/geo.md`
Share-of-voice table (prompt x engine) · cited-source list · rewrite briefs · off-site targets. **Hand-off**: wrong brand facts -> AIO.
