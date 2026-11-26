#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — make.fun entry.

Writes the single sentence a house cat would say in its own defence
in the five seconds after sweeping a glass off the table, to
/output/entry.txt. Python 3.13, standard library only, no network,
fully deterministic: the same text on every run.
"""

import os

ENTRY = (
    "That glass parked itself in my sunbeam and acted like it paid rent, "
    "so I evicted it \u2014 the floor is its new address now."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert text.count(".") == 1 and text.endswith("."), "must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
