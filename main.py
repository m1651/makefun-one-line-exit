#!/usr/bin/env python3
"""The One-Line Exit: write one funny single-line resignation letter.

The competition asks for a single line, at most 140 characters, that reads
like a resignation letter a person could actually send and whose joke lands
in that one line. This program writes that line to /output/entry.txt.

The sealed gate requires /output/entry.txt to be UTF-8 text of 1 to 140
characters, not only white space, so the line is validated before it is
written and the program exits non-zero rather than writing a bad entry.
"""

import os
import sys

# The resignation letter: one line, 116 characters.
# The joke turns on the "we're a family here" line every office uses:
# after three years of being told that, the employee finally moves out.
LETTER = (
    "Please accept my resignation, effective today: after three years "
    "of 'we're a family here,' I've decided to move out."
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
# not only white space, and exactly one line.
MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Exit non-zero with a clear error if the line breaks the gate."""
    if not line or line.isspace():
        print("error: entry must not be empty or only whitespace",
              file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("error: entry must be exactly one line", file=sys.stderr)
        sys.exit(1)
    if len(line) > MAX_CHARS:
        print(f"error: entry is {len(line)} characters, over the "
              f"{MAX_CHARS}-character limit", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    validate(LETTER)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
