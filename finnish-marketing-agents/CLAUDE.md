# Finnish marketing AI agents

## Overview
AI team that produces Finnish (fi) marketing content with English (en) review copies:
1. Ad copy for every campaign type on Google Ads, Meta, LinkedIn and Snapchat.
2. Organic + paid content calendar based on the brand's website analysis, competitor sentiment and the Meta Ad Library.

## Goals
- Native Finnish copy (transcreated, never word-for-word), always within platform character limits.
- Every claim compliant with Finnish/EU rules (KKV, 30-day lowest price rule, alcohol, gambling, finance, health).
- A human approves at every gate. Nothing is published or uploaded automatically.

## Architecture
- `src/agents/` — agent definitions (linked into `.claude/agents/` so Claude Code loads them)
  - `finnish-marketing-orchestrator` → runs the workflow and routes requests
  - `finnish-content-calendar` → research, strategy, calendar
  - `finnish-ads-copywriter` → ad copy + en⇄fi translation
- `src/workflows/` — step-by-step workflow definitions
- `src/tools/` — which tools/MCPs each step uses
- `src/utils/` — helper scripts (e.g. `char_count.py` for limit checks)
- `src/types/` — output schemas (calendar columns, ad tables)
- `prompts/system/` — shared rules (Finnish language, compliance, platform specs)
- `prompts/templates/` — brief templates
- `data/input/` — briefs, exports, screenshots from the user
- `data/output/` — everything the agents produce
- `data/examples/` — reference examples of good output
- `docs/` — architecture and usage; `tests/` — test cases

## Conventions
- Finnish formats: `29,90 €`, `20 %`, `24.12.2026`, `klo 18.00`. Default tone `sinä`.
- Save outputs as `data/output/<brand>/<YYYY-MM-DD>/...`. CSV uses `;` separator and UTF-8.
- Check character limits with `python3 src/utils/char_count.py <file>` before presenting ad copy.
- Quote reviews/competitor copy only in short snippets (≤ 15 words) with source.
- Never invent statistics; mark estimates as estimates.
- Personal/local overrides go in `CLAUDE.local.md` (not committed).
