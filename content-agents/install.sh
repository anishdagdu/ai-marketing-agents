#!/bin/bash
# Installs the 5 content agents into Claude Code.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.claude/agents
cp "$DIR"/agents/*.md ~/.claude/agents/
echo "Installed 5 content agents. Copy config.yaml into your project, fill it in, then start a new Claude Code session."
