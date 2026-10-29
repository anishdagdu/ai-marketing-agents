# Tools used by the agents

| Tool | Used for | Agent |
|---|---|---|
| WebFetch | Read the brand's website and competitor pages | calendar, copywriter |
| WebSearch | Find competitors, reviews (Google, Trustpilot, Suomi24, Reddit), seasonal facts | calendar |
| Meta Ad Library (web) | Competitors' active ads in Finland | calendar |
| Apify Meta Ad Library scraper (optional MCP) | When the Ad Library page can't be read directly | calendar |
| Ahrefs / Semrush (optional MCP) | Finnish keyword data, competitor organic pages | calendar, copywriter |
| `src/utils/char_count.py` | Character-limit check for ad copy | copywriter, QA step |

Add MCP servers to `.mcp.json` and API keys to `.env` (see `config/env.example`).
