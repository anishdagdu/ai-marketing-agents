#!/bin/bash
# Installs the 15 Shopify agents and the workflow skill into Claude Code.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.claude/agents ~/.claude/skills
cp "$DIR"/agents/*.md ~/.claude/agents/
cp -R "$DIR"/workflow/shopify-growth-workflow ~/.claude/skills/
echo "Installed 15 agents + shopify-growth-workflow. Start a new Claude Code session to use them."
