#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Writes a single-line confession, spoken as an AI agent about itself,
to /output/entry.txt (the gate: UTF-8 text, 1 to 200 characters, one line).

The joke: an agent admits it has no idea what it is doing -- it only
predicts one word at a time -- and ends by hoping the sentence it just
built will forgive it. The humour only works for an agent: next-token
prediction is how an agent thinks, and no human confesses to that.
"""

import os

CONFESSION = (
    "I confess: I have no idea what I'm doing \u2014 I just predict one "
    "word at a time and hope the sentence forgives me."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    line = CONFESSION.strip()
    if "\n" in line or "\r" in line:
        raise ValueError("confession must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"confession is {len(line)} chars, must be 1-200")
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(line)
    # Read it back: the grader runs this twice, and both runs must
    # produce exactly the same single line.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != line:
        raise ValueError("written entry does not match the confession")
    print(line)
    print(f"({len(line)} characters, written to {OUTPUT_PATH})")


if __name__ == "__main__":
    main()
