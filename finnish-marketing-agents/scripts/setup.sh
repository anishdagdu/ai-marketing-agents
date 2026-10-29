#!/usr/bin/env bash
# One-time setup: env file, output folders, agent links.
set -euo pipefail
cd "$(dirname "$0")/.."
[ -f .env ] || cp config/env.example .env
mkdir -p data/input data/output .claude/agents
for f in src/agents/*.md; do ln -sf "../../$f" ".claude/agents/$(basename "$f")"; done
echo "Setup done. Fill in .env if you use Apify/Ahrefs/Semrush."
