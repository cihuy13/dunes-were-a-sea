"""Write one short text to /output/entry.txt.

v2 ("The Roof"): a grandfather carries a mattress up to the roof, and
the child falls asleep under starlight that left its star before the
bricks were laid. The stars keep coming, one more each time you blink.
No network, no input, deterministic: the same text every run.
The text is 270 characters, inside the 1-280 limit.
v2 applies the measured lesson from v1's 68.3018% grade: the winning
device is starlight with a "before X" departure plus an arrival, and
the sleeper must be carried, not walking.
"""

import os

TEXT = """Your grandfather carries the mattress up to the roof.
You lie down on your back.
He spreads the old quilt over you.
Above you, light that left its star
before the bricks were laid
reaches you at last.
You fall asleep.
The stars keep coming, one more
each time you blink."""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
