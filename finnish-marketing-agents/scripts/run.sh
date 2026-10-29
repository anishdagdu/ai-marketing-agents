#!/usr/bin/env bash
# Run the full workflow headless with Claude Code.
# Usage: scripts/run.sh data/input/brief.md
set -euo pipefail
cd "$(dirname "$0")/.."
BRIEF="${1:-data/input/brief.md}"
claude -p "Use the finnish-marketing-orchestrator agent to run the Finnish workflow with the brief in $BRIEF. Stop at each approval gate."
