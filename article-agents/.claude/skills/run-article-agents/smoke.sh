#!/bin/bash
# Smoke test for the article-agents pack.
# 1) validates every agent's frontmatter, 2) checks the workflow skill wires all 6
# agents and their numbered outputs together, 3) runs install.sh into a throwaway
# HOME and checks what landed. Never touches your real ~/.claude.
# Usage (from article-agents/): bash .claude/skills/run-article-agents/smoke.sh
set -u
UNIT="$(cd "$(dirname "$0")/../../.." && pwd)"
cd "$UNIT"
fail=0
ok()  { printf '  ok   %s\n' "$1"; }
bad() { printf '  FAIL %s\n' "$1"; fail=1; }

EXPECTED="ar-topic-strategist ar-researcher ar-outline-architect ar-writer ar-editor ar-seo-publisher"
SKILL=workflow/article-creation-workflow/SKILL.md

fm() { awk -v k="$2" 'NR==1&&$0!="---"{exit} NR>1&&$0=="---"{exit} NR>1{ if (index($0,k": ")==1){sub(k": ",""); print; exit} }' "$1"; }

echo "== agents"
n=$(ls agents/*.md 2>/dev/null | wc -l | tr -d ' ')
[ "$n" = 6 ] && ok "6 agent files" || bad "expected 6 agent files, found $n"
for a in $EXPECTED; do
  f="agents/$a.md"; before=$fail; fail=0
  [ -f "$f" ] || { bad "$f missing"; continue; }
  name=$(fm "$f" name); desc=$(fm "$f" description); model=$(fm "$f" model)
  [ "$name" = "$a" ] || bad "$f: name '$name' != filename"
  [ ${#desc} -ge 60 ] || bad "$f: description too short (${#desc} chars)"
  echo "$desc" | grep -qi "use when" || bad "$f: description has no 'Use when' trigger"
  case "$model" in opus|sonnet|haiku|inherit) ;; *) bad "$f: model '$model' invalid";; esac
  grep -q "outputs/articles/<slug>/" "$f" || bad "$f: no outputs/articles/<slug>/ path"
  [ $fail = 0 ] && ok "$a"
  [ $before = 1 ] && fail=1
done

echo "== workflow skill"
[ -f "$SKILL" ] && ok "$SKILL exists" || bad "$SKILL missing"
[ "$(fm "$SKILL" name)" = article-creation-workflow ] && ok "skill name matches dir" || bad "skill name mismatch"
for a in $EXPECTED; do grep -q "\`$a\`" "$SKILL" || bad "skill never invokes $a"; done
for o in 01-brief 02-research 03-outline 04-draft 05-edit-report 05-final 06-seo; do
  grep -rqs "$o.md" agents/ || bad "no agent writes $o.md"
  grep -qs "$o.md" "$SKILL" || bad "skill never mentions $o.md"
done
# each step N's agent must read what step N-1 wrote
grep -q "01-brief.md" agents/ar-researcher.md        || bad "researcher doesn't read the brief"
grep -q "02-research.md" agents/ar-outline-architect.md || bad "outline doesn't read research"
grep -q "03-outline.md" agents/ar-writer.md          || bad "writer doesn't read the outline"
grep -q "04-draft.md" agents/ar-editor.md            || bad "editor doesn't read the draft"
grep -q "05-final.md" agents/ar-seo-publisher.md     || bad "publisher doesn't read 05-final"
[ $fail = 0 ] && ok "handoff chain 01→06 intact"

echo "== install (sandboxed HOME)"
bash -n install.sh && ok "install.sh syntax" || bad "install.sh syntax"
TMPH=$(mktemp -d)
if out=$(HOME="$TMPH" bash install.sh 2>&1); then ok "install.sh ran: $out"; else bad "install.sh failed: $out"; fi
got=$(ls "$TMPH/.claude/agents" 2>/dev/null | wc -l | tr -d ' ')
[ "$got" = 6 ] && ok "6 agents installed" || bad "installed $got agents"
[ -f "$TMPH/.claude/skills/article-creation-workflow/SKILL.md" ] && ok "workflow skill installed" || bad "workflow skill not installed"
# re-running must be idempotent (cp -R into an existing dir nests it otherwise)
HOME="$TMPH" bash install.sh >/dev/null 2>&1
[ ! -d "$TMPH/.claude/skills/article-creation-workflow/article-creation-workflow" ] && ok "re-install is idempotent" || bad "re-install nested the skill dir"
rm -rf "$TMPH"

echo
[ $fail = 0 ] && echo "SMOKE PASS" || echo "SMOKE FAIL"
exit $fail
