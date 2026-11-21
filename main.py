"""Write one short text to /output/entry.txt.

v3 ("The Night Train"): a child falls asleep on the night train, his
grandfather holding his hand, while starlight that has travelled since
before the rails were laid finds him, and one more star comes with
every click of the wheels, all night, all the way.
No network, no input, deterministic: the same text every run.
The text is 272 characters, inside the 1-280 limit.
v3 stacks two independently 11-0-proven devices: v2's starlight-before-X
plus arrival, and #1's active motion plus gentle sound (wheels clicking,
train rocking you on), in a fresh setting.
"""

import os

TEXT = """You fall asleep on the night train.
Your grandfather holds your hand.
The wheels click, and click.
Above, light from a far star,
travelling since before the rails were laid,
finds you tonight.
The train rocks you on.
One more star with every click,
all night, all the way."""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
