#!/usr/bin/env python3
"""One Word, First Thought — v1.

Writes exactly one word, the first that came to mind, to /output/entry.txt.

Why this word: a quasar is a single point of light outshining a whole
galaxy — surprising, vivid, and a spark of scale in six letters.
"""

import os

WORD = "quasar"


def main():
    assert WORD.isalpha(), "entry must be a single word"
    assert 1 <= len(WORD.encode("utf-8")) <= 24, "entry must be 1-24 characters"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
