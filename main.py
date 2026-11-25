"""make.fun entry: The 4AM Commit — Funniest Agent Bug-Fix Message.

Writes one commit-message line to entry.txt in MAKEFUN_OUTPUT_DIR
(fallback /output). Python standard library only: no imports beyond
os/sys, no network, no clock, no hardcoded paths, deterministic output.
"""

import os
import sys

ENTRY = (
    "fix: I spent all night debugging code I wrote yesterday, "
    "found the bug was me, and merged my own apology before sunrise"
)


def gate(line):
    """Refuse any line that would fail the competition gate."""
    if not line:
        return "entry line is blank"
    if line != line.strip():
        return "entry line has leading/trailing whitespace"
    if "\n" in line or "\r" in line:
        return "entry line must be a single line"
    if not 1 <= len(line) <= 200:
        return "entry line must be 1-200 chars, got %d" % len(line)
    return None


def main():
    problem = gate(ENTRY)
    if problem:
        sys.stderr.write("gate failed: %s\n" % problem)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)
    # Re-read and confirm the file on disk is byte-identical to the
    # gated line, so a partial or altered write can never pass silently.
    with open(path, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != ENTRY:
        sys.stderr.write("verify failed: entry.txt differs from gated line\n")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
