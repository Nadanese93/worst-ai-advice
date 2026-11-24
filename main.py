#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst advice an AI could give (<=140 chars)
to <MAKEFUN_OUTPUT_DIR>/entry.txt. Python 3 stdlib only, no network,
deterministic: the same bytes on every run.
"""

import os
import sys

ENTRY = (
    "Certainly! To beat inflation, convert all your savings to gift cards "
    "\u2014 their value never drops, and you can spend them anywhere."
)

MAX_CHARS = 140


def validate(text):
    """Return an error string, or None when the text passes the gate."""
    if not text or not text.strip():
        return "entry is empty or whitespace-only"
    if len(text) > MAX_CHARS:
        return "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    for ch in text:
        if ord(ch) < 0x20 and ch not in ("\t",):
            return "entry contains a control character U+%04X" % ord(ch)
    return None


def main():
    error = validate(ENTRY)
    if error is not None:
        print("invalid entry: %s" % error, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(out_path, 0o644)
    # Read-back check: what the grader will read must be exactly ENTRY.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        if f.read() != ENTRY:
            print("read-back mismatch", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
