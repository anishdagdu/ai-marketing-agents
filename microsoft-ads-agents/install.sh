#!/bin/bash
# Installs the 8 Microsoft Ads agents, the JEV model router and the workflow skill into Claude Code.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.claude/agents ~/.claude/skills
cp "$DIR"/agents/*.md ~/.claude/agents/
cp -R "$DIR"/workflow/microsoft-ads-workflow ~/.claude/skills/
echo "Installed 8 agents + JEV router + microsoft-ads-workflow. Start a new Claude Code session to use them."
