#!/usr/bin/env python3
"""Two-Sentence Horror -- make.fun entry (program/v1).

Writes one horror story of exactly two sentences to /output/entry.txt.

Deterministic: the same bytes on every run. No network, no secrets,
no input files -- the story is embedded below as a single constant.
"""

import os

STORY = (
    "Every evening my dog waits by the front door at six, tail wagging, "
    "for my husband to come home from work. "
    "My husband died in March, and the dog has never once waited on a day "
    "his old phone didn't light up with a text that simply says 'On my way'."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
