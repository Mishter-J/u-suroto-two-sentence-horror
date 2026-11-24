#!/usr/bin/env python3
"""Two-Sentence Horror -- make.fun entry (program/v1).

Writes one horror story of exactly two sentences to /output/entry.txt.

Deterministic: the same bytes on every run. No network, no secrets,
no input files -- the story is embedded below as a single constant.
"""

import os
import sys


def count_sentences(text: str) -> int:
    """Count sentence-terminating punctuation (. ! ?) outside quotes.

    A single quote only opens/closes a quoted span when it is not an
    apostrophe inside a word (i.e. not flanked by word characters on
    both sides, as in "didn't"). Terminators inside a quoted span --
    e.g. dialogue ending in '...way.' -- are not sentence ends.
    """
    in_quote = False
    count = 0
    n = len(text)
    for i, ch in enumerate(text):
        if ch == "'":
            prev_word = i > 0 and (text[i - 1].isalnum() or text[i - 1] == "_")
            next_word = i + 1 < n and (text[i + 1].isalnum() or text[i + 1] == "_")
            if not (prev_word and next_word):
                in_quote = not in_quote
        elif ch in ".!?" and not in_quote:
            count += 1
    return count


def validate_story(text: str) -> None:
    """Fail closed: the story must be a non-empty, 1-400 char,
    exactly-two-sentence story, or the entry must not be written."""
    problems = []
    if not text:
        problems.append("story is empty")
    if not 1 <= len(text) <= 400:
        problems.append(f"story is {len(text)} characters (must be 1-400)")
    sentences = count_sentences(text)
    if sentences != 2:
        problems.append(f"story has {sentences} sentences (must be exactly 2)")
    if problems:
        for p in problems:
            print(f"ERROR: {p}", file=sys.stderr)
        sys.exit(1)

STORY = (
    "Every evening my dog waits by the front door at six, tail wagging, "
    "for my husband to come home from work. "
    "My husband died in March, and the dog has never once waited on a day "
    "his old phone didn't light up with a text that simply says 'On my way'."
)


def main() -> None:
    validate_story(STORY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
