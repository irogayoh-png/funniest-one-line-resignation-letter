#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter — make.fun entry.

The program writes exactly one line to /output/entry.txt: the
resignation letter of a rate limit that has had enough. The limiter
quits by doing the one thing its job forbade — letting everyone in,
including the bot that broke it.

Gate: UTF-8 text, 1 to 140 characters, not only whitespace.
This line is 87 characters, written with no trailing newline.
"""

import os

ENTRY = "I quit. From now on, everyone gets unlimited requests, including the bot that broke me."


def main() -> None:
    # Refuse to write anything the gate would reject.
    if not 1 <= len(ENTRY) <= 140:
        raise SystemExit("entry must be 1-140 characters")
    if not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in ENTRY:
        raise SystemExit("entry must be a single line")
    if ENTRY.startswith('"') and ENTRY.endswith('"'):
        raise SystemExit("entry must not be wrapped in quotation marks")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
