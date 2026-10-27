# AI Website Audit Agents

Ten agents that audit and optimize any company website automatically, using two free tools: **Google PageSpeed Insights** and **Ahrefs Webmaster Tools**. GitHub Actions runs them on a schedule, Claude writes the executive summary, and the results arrive as a scorecard, a GitHub Issue and Slack alerts.

![Workflow](docs/workflow.gif)

## The 10 agents

| # | Agent | What it does | KPI / target | Owner | Data |
|---|---|---|---|---|---|
| 1 | Core Web Vitals baseline | Real-user speed (LCP, INP, CLS) on revenue pages | ≥ 75% pages passing | Engineering | PageSpeed |
| 2 | Conversion leakage | Flags revenue pages slow enough to lose buyers | LCP < 2.5s | Eng + Growth | PageSpeed |
| 3 | Speed fix backlog | Ranks fixes across pages by seconds saved → sprint tickets | < 1s savings left | Engineering | PageSpeed |
| 4 | Marketing tag bloat | Finds pixels, chat and heatmap scripts slowing pages | < 250ms blocking | Marketing Ops | PageSpeed |
| 5 | Accessibility & compliance | ADA/EAA risks: contrast, alt text, labels | Score ≥ 90 | Design + Eng | PageSpeed |
| 6 | Site health score | % of pages with no critical issue | ≥ 90 | SEO | Ahrefs export or built-in crawler |
| 7 | Crawl budget & link equity | Broken pages, redirect chains, duplicate titles, orphan pages | 0 critical | SEO + Eng | Built-in crawler |
| 8 | Striking-distance keywords | Keywords in positions 4–15, the quickest traffic wins | Move 5/month to top 3 | SEO + Content | Ahrefs or Search Console export |
| 9 | Backlink authority | New and lost referring domains, spam review | Net growth monthly | SEO + PR | Ahrefs export |
| 10 | Early-warning alerts | Regressions since the last run, noindex/404 on revenue pages → Slack | 0 open alerts | Marketing Ops | All of the above |

## Workflow

1. **Trigger:** GitHub Actions runs the speed check (agents 1–5 + 10) **every Monday** and the full audit (all 10) **on the 1st of each month**. You can also run it manually from the Actions tab.
2. **Data:** PageSpeed Insights API, Ahrefs Webmaster Tools CSV exports (or an Ahrefs API token), Search Console exports, and a built-in crawler.
3. **Agents:** each one returns a status (🟢 pass, 🟡 warn, 🔴 fail, ⚪ skipped), a KPI value against its target, findings, next actions and an owner.
4. **Combine:** `run.py` collects the results, compares them with the previous run, and asks Claude for a short summary for leadership.
5. **Deliver:** a markdown scorecard is committed to `reports/`, a GitHub Issue is opened with the action checklist, and Slack is alerted on regressions.

## Setup (about 10 minutes)

1. **Edit `config.json`:** set `site` and list your key `revenue_pages` (home, pricing, product, checkout).
2. **Add repo secrets** (Settings → Secrets and variables → Actions):

| Secret | Required? | Where to get it |
|---|---|---|
| `PAGESPEED_API_KEY` | **Yes** (without it Google returns 429 errors) | Free: Google Cloud Console → enable "PageSpeed Insights API" → Credentials → API key |
| `ANTHROPIC_API_KEY` | Optional, for the Claude summary | console.anthropic.com |
| `SLACK_WEBHOOK_URL` | Optional, for alerts | Slack → Incoming Webhooks |
| `AHREFS_API_TOKEN` | Optional, paid Ahrefs API | Otherwise use free CSV exports (next step) |

3. **For agents 8 and 9:** add free Ahrefs Webmaster Tools / Search Console exports to `data/`. See [data/README.md](data/README.md).
4. **Run it:** Actions → *Website audit agents* → *Run workflow*.

## Run locally

```bash
export PAGESPEED_API_KEY=...        # free
python run.py --mode weekly          # speed agents
python run.py --mode monthly         # full audit
```

No dependencies: the agents use only the Python standard library. Pillow is needed only to regenerate the GIF (`python docs/make_gif.py`).

## Files

```
run.py                  orchestrator + Claude summary + scorecard
config.json             your site + revenue pages
agents/speed_agents.py  agents 1-5 (PageSpeed Insights)
agents/search_agents.py agents 6-10 (Ahrefs / crawler / alerts)
agents/crawler.py       free built-in crawler
agents/common.py        shared helpers
data/                   optional CSV exports
reports/                scorecards + run history (written by the workflow)
docs/workflow.gif       infographic
```
