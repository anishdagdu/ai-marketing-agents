#!/bin/bash
# Installs the 16 HubSpot agents and the workflow skill into Claude Code.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.claude/agents ~/.claude/skills
cp "$DIR"/agents/*.md ~/.claude/agents/
cp -R "$DIR"/workflow/hubspot-growth-workflow ~/.claude/skills/
echo "Installed 16 agents + hubspot-growth-workflow. Start a new Claude Code session to use them."
