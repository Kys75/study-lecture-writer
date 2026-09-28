#!/usr/bin/env python3
"""Validate common formatting constraints for saved lecture Markdown notes."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys


def count_unescaped(text: str, token: str) -> int:
    count = 0
    start = 0
    while True:
        idx = text.find(token, start)
        if idx == -1:
            return count
        backslashes = 0
        j = idx - 1
        while j >= 0 and text[j] == "\\":
            backslashes += 1
            j -= 1
        if backslashes % 2 == 0:
            count += 1
        start = idx + len(token)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate lecture Markdown note formatting.")
    parser.add_argument("paths", nargs="+", help="Markdown files to validate")
    parser.add_argument("--allow-blank-lines", action="store_true", help="Do not fail on blank lines")
    args = parser.parse_args()

    failed = False
    for raw in args.paths:
        path = Path(raw)
        if not path.exists():
            print(f"FAIL {path}: file does not exist")
            failed = True
            continue
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        blank_lines = [i + 1 for i, line in enumerate(lines) if not line.strip()]
        dollar_blocks = count_unescaped(text, "$$")
        ok = True
        if blank_lines and not args.allow_blank_lines:
            print(f"FAIL {path}: blank lines at {blank_lines[:20]}" + (" ..." if len(blank_lines) > 20 else ""))
            ok = False
        if dollar_blocks % 2 != 0:
            print(f"FAIL {path}: unbalanced $$ delimiters ({dollar_blocks})")
            ok = False
        if ok:
            print(f"OK {path}: {len(lines)} lines, blank_lines={len(blank_lines)}, dollar_delimiters={dollar_blocks}")
        failed = failed or not ok
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
