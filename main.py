"""Make the AI judge feel awe — entry program.

Writes one short text to /output/entry.txt: a father and child walking
through night dunes, the sand beneath them the floor of an old sea.
No network, no input, deterministic: the same text every run.
The text is 269 characters, inside the 1-280 limit.
"""

import os

TEXT = """Your father walks beside you through the dunes.
The sand is cool under your bare feet.
The stars are out, thick as salt overhead.
Beneath your feet lies the floor of an old sea,
older than any road. It keeps your footprints.

You fall asleep to the sand still shifting."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
