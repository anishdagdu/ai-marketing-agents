#!/usr/bin/env bash
# Installs the AI UGC Ad agents into a Claude Code project.
# Usage: bash install.sh [target-project-dir]   (default: current directory)
set -euo pipefail

SRC="$(cd "$(dirname "$0")" && pwd)"
DEST="${1:-$PWD}"

mkdir -p "$DEST/.claude/agents" "$DEST/.claude/skills"
cp "$SRC"/agents/*.md "$DEST/.claude/agents/"
cp -R "$SRC/workflow/ugc-campaign" "$DEST/.claude/skills/"
echo "Installed 4 agents and the /ugc-campaign workflow into $DEST/.claude"

# The 19 Higgsfield skills (prompt styles + browser automation) are not included.
# They come from https://github.com/AKCodez/higgsfield-claude-skills
if [ ! -d "$DEST/.claude/skills/ugc-video-auto" ]; then
  read -r -p "Download the 19 Higgsfield skills from AKCodez/higgsfield-claude-skills now? [y/N] " ok
  if [[ "$ok" =~ ^[Yy]$ ]]; then
    tmp="$(mktemp -d)"
    git clone -q --depth 1 https://github.com/AKCodez/higgsfield-claude-skills "$tmp/hf"
    for d in "$tmp"/hf/*/; do cp -R "$d" "$DEST/.claude/skills/"; done
    rm -rf "$tmp"
    echo "Installed Higgsfield skills."
  else
    echo "Skipped. Install them later from https://github.com/AKCodez/higgsfield-claude-skills"
  fi
fi

if command -v claude >/dev/null && ! claude mcp list 2>/dev/null | grep -q playwright; then
  echo "For generation on Higgsfield, add Playwright:  claude mcp add playwright npx @playwright/mcp@latest"
fi
echo "Done. In Claude Code run:  /ugc-campaign <product, audience, platform, number of ads>"
