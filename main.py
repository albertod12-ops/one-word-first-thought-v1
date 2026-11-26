#!/usr/bin/env python3
"""One Word, First Thought — v3.

The first word that came to mind, written to /output/entry.txt.

waldeinsamkeit is German for the feeling of being alone in the woods:
forest solitude that is sublime rather than lonely. A single compound,
Wald (forest) + Einsamkeit (solitude), holds a whole scene at once —
trees, silence, light through branches, and the feeling with it.
"""

import os

# v3: the compound unpacks into its own meaning.
WORD = "waldeinsamkeit"
OUT = "/output/entry.txt"


def main():
    assert WORD.isalpha()
    assert 1 <= len(WORD) <= 24
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)
    os.chmod(OUT, 0o644)


if __name__ == "__main__":
    main()
