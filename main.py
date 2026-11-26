#!/usr/bin/env python3
"""One Word, First Thought — v3.

Writes exactly one word, the first that came to mind, to /output/entry.txt.

Why this word: waldeinsamkeit names the feeling of being alone in the
woods — forest solitude that is sublime rather than lonely. A whole scene
in one compound: Wald (forest) + Einsamkeit (solitude). More specific than
a smell, and the compound unpacks into its own meaning.
"""

import os

WORD = "waldeinsamkeit"


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
