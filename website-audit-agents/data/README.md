# Data exports (optional)

Agents 1-7 and 10 work with no files here. Agents 8 and 9 need ranking and backlink data. Drop these CSV exports in this folder (file names are set in `config.json`):

| File | Where to export it (free) | Used by |
|---|---|---|
| `ahrefs_organic_keywords.csv` | Ahrefs Webmaster Tools → Site Explorer → Organic keywords → Export | Agent 8 |
| `gsc_queries.csv` | Google Search Console → Performance → Queries → Export (fallback for agent 8) | Agent 8 |
| `ahrefs_referring_domains.csv` | Ahrefs Webmaster Tools → Site Explorer → Referring domains → Export | Agent 9 |
| `ahrefs_site_audit.csv` | Ahrefs Webmaster Tools → Site Audit → Page explorer → Export (optional, replaces the built-in crawler) | Agent 6 |

If you have paid Ahrefs API access, set the `AHREFS_API_TOKEN` secret instead and skip the CSVs.
