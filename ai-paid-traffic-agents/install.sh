#!/bin/bash
# Installs the 10 agents and the workflow skill into Claude Code.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.claude/agents ~/.claude/skills
cp "$DIR"/agents/*.md ~/.claude/agents/
cp -R "$DIR"/workflow/paid-traffic-workflow ~/.claude/skills/
echo "Installed 10 agents + paid-traffic-workflow. Start a new Claude Code session to use them."
