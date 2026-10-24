---
name: seo-audit-plan
description: Foundational SEO audit and plan - technical health, on-page, content and high-intent keyword clusters, returned as a 0-100 SEO score. Use when the user asks for SEO, rankings, keywords, crawl/index issues or Core Web Vitals.
---
# SEO Audit & Plan (layer 1 of 5)

Shared rules for all 5 layers are in `search-everywhere-workflow` (output folder, severity scale, finding format, security). Follow them.

## Inputs
Site URL, business type, market, top 3 competitors. Optional: Search Console / GA4 / PageSpeed exports.

## Crawl limits
Max 50 pages (sitemap + homepage links first), respect robots.txt, 1 s between requests, 30 s timeout, max 3 redirect hops.

## Steps
1. **Business type**: SaaS, e-commerce, local, publisher, agency or other. It changes which checks matter.
2. **Technical** (fetch robots.txt, sitemap.xml, key templates):
   - Indexability: noindex, canonicals, status codes, redirect chains, orphan pages.
   - Rendering: is main content in the raw HTML or JS-only? (JS-only = Critical for AI layers too.)
   - Security headers: HTTPS, HSTS, CSP, X-Content-Type-Options, Referrer-Policy.
   - Mobile viewport, hreflang (if multi-region), URL structure.
3. **Performance**: LCP < 2.5 s, INP < 200 ms, CLS < 0.1. Use field data (CrUX / PageSpeed) if provided; otherwise label as "lab estimate".
4. **On-page**: titles, meta descriptions (flag templated ones), one H1, heading order, internal links to money pages, image alt text and size.
5. **Content**: thin pages (< 300 words where depth is expected), duplicates, E-E-A-T basics (author, dates, sources).
6. **Keyword clusters**: group by intent (transactional > commercial > informational > navigational). Map each cluster to one pillar page + supporting pages. Flag cannibalisation (two pages for one cluster) and gaps competitors cover.
7. **Change history**: before blaming a traffic drop on anything, check the Google Search Status Dashboard for updates in that window. A date overlap is a hypothesis, not proof.

## Score (0-100)
| Category | Weight |
|---|---|
| Technical | 25% |
| Content quality | 25% |
| On-page | 20% |
| Performance (CWV) | 15% |
| Schema | 10% |
| Images | 5% |

## Output -> `findings/seo.md`
- Score + category sub-scores
- Findings table (severity · issue · pages · fix)
- Keyword cluster map -> page mapping
- **Hand-off**: question keywords -> AEO; rendering / robots issues -> AIO; top landing pages -> SXO.
