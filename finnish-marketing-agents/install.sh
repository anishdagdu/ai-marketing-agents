#!/bin/bash
# Installs the 3 Finnish marketing agents into Claude Code.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.claude/agents
cp "$DIR"/src/agents/*.md ~/.claude/agents/
echo "Installed 3 agents (finnish-marketing-orchestrator, finnish-content-calendar, finnish-ads-copywriter). Start a new Claude Code session to use them."
