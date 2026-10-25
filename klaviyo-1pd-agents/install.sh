#!/bin/bash
# Installs the 5 Klaviyo agents and the workflow skill into Claude Code.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.claude/agents ~/.claude/skills
cp "$DIR"/agents/*.md ~/.claude/agents/
cp -R "$DIR"/workflow/klaviyo-growth-workflow ~/.claude/skills/
echo "Installed 5 agents + klaviyo-growth-workflow. Start a new Claude Code session to use them."
