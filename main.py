"""Dad Joke Showdown entry.

Writes one original dad joke to entry.txt in the output directory.
The joke is a fixed string: the program is fully deterministic, so two
runs produce byte-identical output.
"""

import os

JOKE = (
    "The lawn looked sad, so I asked what was wrong. "
    "It said, \"I'm going through a rough patch \u2014 but I'll mow on.\""
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
