#!/usr/bin/env python3
"""One Word, First Thought — Round 2 entry.

Writes the keeper word to /output/entry.txt, byte-exact, with no
trailing newline. Pure standard library only.

The keeper beats the R1 word "Petrichor" on the judge's criteria:
surprise (a genuinely obscure Old English word, not a beautiful-words
list staple) and wit (the sound enacts the meaning, and the second
meaning — to move unsteadily — reframes the first).
"""

import os

WORD = "wamble"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
