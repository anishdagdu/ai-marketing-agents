# Search Everywhere: SEO · AEO · GEO · AIO · SXO

Source: LinkedIn post by "AI for E-Commerce" (Blue Elephant Media NY). Its claim: most businesses only work on SEO, but the biggest advantage is in the other four layers.

## How the five layers stack

| Layer | Question it answers | Where the user is | Main levers | How to measure |
|---|---|---|---|---|
| **SEO** | Can search engines find, crawl and rank us? | Google / Bing results | Keyword clusters by intent, technical health (crawl, index, Core Web Vitals, canonicals), internal links, backlinks | Rankings, organic clicks, indexed pages (Search Console) |
| **AEO** | Are we *the* answer? | Featured snippets, People Also Ask, voice assistants, AI Overviews | Question-led headings, 40–60 word direct answers, FAQ/HowTo/Product schema, tables and lists | Snippet ownership, PAA presence, AI Overview citations |
| **GEO** | Do AI chatbots cite or recommend us? | ChatGPT, Perplexity, Gemini, Claude, Copilot | Entity-rich content, original stats and data, quotes from experts, E-E-A-T (author bios, credentials, reviews), clear brand facts | Share of voice across a fixed prompt set, citation count, sentiment |
| **AIO** | Does AI "know" our brand correctly? | Model training data + live retrieval | Consistent brand facts across the web (Wikipedia/Wikidata, Crunchbase, LinkedIn, G2/Trustpilot, Reddit, press), `llms.txt`, allowing AI crawlers in robots.txt, Organization schema with `sameAs` | Accuracy of AI answers about the brand, mention rate, wrong-fact count |
| **SXO** | Once they land, do they convert? | Your site | Page speed (LCP < 2.5s, INP < 200ms, CLS < 0.1), clear CTAs, matching search intent, trust signals, ongoing A/B tests | Conversion rate, bounce/engagement, revenue per visit |

## Key research findings

- **AI search is growing fast but doesn't replace Google.** Google still sends most referral traffic; AI assistants send less but higher-intent visits. Treat them as extra channels, not a swap.
- **AI answers pull from pages that already rank.** AI Overviews and Perplexity mostly cite pages in the top organic results, so SEO stays the base layer.
- **Citations favour concrete content.** The 2023 GEO paper (Aggarwal et al., Princeton/IIT Delhi) found adding statistics, quotations and cited sources raised visibility in generative answers by up to ~40%. Keyword stuffing did not help.
- **Off-site mentions matter more for AI than for Google.** Chatbots lean on Reddit, review sites, Wikipedia, YouTube and "best X" listicles. Brand mentions (even without links) shape what AI says.
- **Schema is a shared foundation.** Organization, Product, FAQPage, HowTo, Review and Article markup help AEO, GEO and AIO at once.
- **Crawler access is a hard gate.** If robots.txt or a CDN blocks GPTBot, OAI-SearchBot, PerplexityBot, ClaudeBot or Google-Extended, those engines can't use your pages.
- **Content that needs JavaScript to render** is often missed by AI crawlers. Server-render key content.
- **SXO closes the loop.** More visibility is wasted if the landing page is slow or doesn't match the query intent.

## Caveats

- "AEO", "GEO" and "AIO" overlap and the terms aren't standardised; vendors define them differently.
- AI answers vary by run, model and location. Measure with a fixed prompt set run repeatedly, not a single check.
- Nobody can guarantee inclusion in model training data; AIO is about raising the odds.
