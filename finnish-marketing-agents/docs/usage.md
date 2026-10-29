# Usage

## Setup
```bash
scripts/setup.sh
```

## Full workflow
Fill in `prompts/templates/brief.md`, save a copy as `data/input/brief.md`, then in Claude Code say:
> Run the Finnish workflow with data/input/brief.md

or run `scripts/run.sh data/input/brief.md`.

## Single jobs
- "Use finnish-ads-copywriter: Google Search + PMax and Meta Sales for example.fi/joulu, 20 % off until 24.12."
- "Use finnish-ads-copywriter to translate this English ad set to Finnish: …"
- "Use finnish-content-calendar for example.fi, competitors A, B, C, December 2026."

## Check character limits
```bash
python3 src/utils/char_count.py data/output/<brand>/<date>/ads/google.md
```

## Troubleshooting
- Meta Ad Library won't load → paste ad links/screenshots, or add the Apify MCP in `.mcp.json`.
- Agent not found → run `scripts/setup.sh` to recreate the links in `.claude/agents/`.
- Excel shows broken ä/ö → open the CSV with UTF-8 import; separator is `;`.
