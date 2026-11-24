#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line (1-240 chars) to /output/entry.txt: a quiet,
earned moment of pride for someone in a scene.
"""

import os

ENTRY = (
    "She'd failed her driving test four times; on the fifth, she parked "
    "perfectly, switched off the engine, and sat a moment, hands still "
    "on the wheel."
)


def validate_entry(text: str) -> None:
    """Gate: 1-240 chars, single line, not whitespace-only."""
    if not text or not text.strip():
        raise ValueError("entry is empty")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if len(text) > 240:
        raise ValueError(f"entry is {len(text)} chars, over the 240 cap")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if "  " in text:
        raise ValueError("entry contains a double space")
    if text[-1] not in ".!?":
        raise ValueError("entry must end with terminal punctuation")


def main() -> None:
    validate_entry(ENTRY)
    print(ENTRY)
    print(f"({len(ENTRY)} chars)")
    for path in ("/output/entry.txt", "out/entry.txt"):
        try:
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(ENTRY + "\n")
        except OSError:
            pass


if __name__ == "__main__":
    main()
