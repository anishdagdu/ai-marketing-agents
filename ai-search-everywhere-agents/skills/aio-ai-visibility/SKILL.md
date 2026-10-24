---
name: aio-ai-visibility
description: AI Optimisation - make sure AI models can reach the site and know the brand accurately, via AI-crawler access, server rendering, llms.txt, entity schema and presence on the sources models learn from. Use for llms.txt, AI crawlers, brand facts in AI, Wikipedia/Wikidata or wrong AI answers.
---
# AIO AI Visibility (layer 4 of 5)

Shared rules: see `search-everywhere-workflow`.

## Inputs
Brand name, site URL, official brand facts (founded, HQ, founders, products, pricing, USP).

## Steps
1. **Crawler access**: read robots.txt and test a fetch with each user agent if possible (CDN/WAF rules like Cloudflare's AI-bot block can override robots.txt).
   - Critical: GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-SearchBot, PerplexityBot, Googlebot, Bingbot.
   - Secondary: Google-Extended, Applebot-Extended, CCBot, Meta-ExternalAgent, Amazonbot.
   - Note the trade-off: training bots (GPTBot, Google-Extended, CCBot) vs search/retrieval bots (OAI-SearchBot, ChatGPT-User, PerplexityBot). Blocking search bots removes you from live answers; let the user decide on training bots.
   - Score: start 100, -15 per critical bot blocked, -5 per secondary, -10 if robots.txt has no Sitemap line.
2. **Rendering**: fetch raw HTML without JS. If the main content or the JSON-LD only appears after JS runs = Critical (AI crawlers mostly don't run JS).
3. **llms.txt**: check `/llms.txt` and `/llms-full.txt`. Score 0 absent · 30 malformed · 50 minimal · 70 covers main sections · 90+ with llms-full.txt. Draft one if missing (H1 brand, one-line summary in a quote, H2 sections of markdown links). It's an emerging standard; low effort, uncertain payoff.
4. **Brand fact audit**: ask each engine "What is <brand>?", "Who founded...", "How much does... cost", "Is <brand> legit?". List each wrong or missing fact and where it probably came from.
5. **Entity graph**: Organization (or LocalBusiness) JSON-LD with `logo`, `foundingDate`, `founder`, `sameAs` to 5+ profiles. Keep facts identical on Wikidata/Wikipedia (only if notable), LinkedIn, Crunchbase, Google Business Profile, G2/Trustpilot, YouTube, marketplaces.
6. **Brand authority** (points): Wikipedia/Wikidata 30 · industry/review sites and press 25 · Reddit 20 · YouTube 15 · LinkedIn 10. (Third-party research reports YouTube mentions correlate strongly with AI citations; backlinks less so. Treat as directional.)

## Score (0-100)
Crawler access 30 · rendering 25 · entity schema + consistency 20 · brand authority 15 · llms.txt 10.

## Output -> `findings/aio.md`
Crawler table · robots.txt suggestion · llms.txt draft · brand-fact error list with the source to fix · Organization JSON-LD.
Training-data inclusion can't be guaranteed; this raises the odds and fixes live retrieval.
