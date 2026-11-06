#!/bin/bash
# Installs the 14 Apple Ads agents (incl. the JEV model router) and the workflow skill into Claude Code.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.claude/agents ~/.claude/skills
cp "$DIR"/agents/*.md ~/.claude/agents/
cp -R "$DIR"/workflow/apple-ads-workflow ~/.claude/skills/
echo "Installed 14 agents + apple-ads-workflow. Start a new Claude Code session to use them."
