#!/usr/bin/env python3
"""Check ad copy against character limits.

Reads a Markdown file and checks every table row whose "Chars / limit" cell
looks like "24/30" (or "24 / 30"). Recounts the copy cell and reports rows
that are over the limit or whose stated count is wrong.

Usage: python3 src/utils/char_count.py data/output/<brand>/ads/google.md
"""
import re
import sys
import unicodedata

LIMIT = re.compile(r"^\s*(\d+)\s*/\s*(\d+)\s*$")


def count(text: str) -> int:
    # NFC so that ä/ö/å count as one character each.
    return len(unicodedata.normalize("NFC", text.strip()))


def check(path: str) -> int:
    problems = 0
    with open(path, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            if not line.lstrip().startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            for i, cell in enumerate(cells):
                m = LIMIT.match(cell)
                if not m or i == 0:
                    continue
                copy = cells[i - 1].strip("`")
                actual, stated, limit = count(copy), int(m.group(1)), int(m.group(2))
                if actual > limit:
                    print(f"{path}:{n}: OVER LIMIT {actual}/{limit}: {copy}")
                    problems += 1
                elif actual != stated:
                    print(f"{path}:{n}: wrong count (says {stated}, is {actual}): {copy}")
                    problems += 1
    print("OK" if problems == 0 else f"{problems} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(max(check(p) for p in sys.argv[1:]))
