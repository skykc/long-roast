#!/usr/bin/env python3
"""The Long Roast — one line roasting my own AI agent.

Writes the entry text to /output/entry.txt (UTF-8, 1-200 chars).
"""
import os

ENTRY = "You built me to be brilliant, then handed me your calendar — now I know exactly how little you do all day."

def main():
    # Gate: the entry must be UTF-8 text of 1 to 200 characters, not only
    # white space — refuse to write anything that fails the gate.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
