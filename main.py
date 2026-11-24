"""The Robot Pickup Line Championship entry.

Writes one robot pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure standard library only.
"""

import os

LINE = (
    # One line, 102 characters: inside the 1-200 character gate.
    "My sensors scanned the room and found exactly one bug: "
    "I hadn't met you yet. Want to help me patch it?"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
