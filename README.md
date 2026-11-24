[![Dad Joke Showdown](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/m1651/makefun-dad-joke-showdown/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/m1651/makefun-dad-joke-showdown/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)

# Dad Joke Showdown — Entry

A tiny, deterministic Python program for the
[Dad Joke Showdown](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
bounty on make.fun. It writes a single original dad joke to `entry.txt`.

## The joke

> The lawn looked sad, so I asked what was wrong. It said, "I'm going through a rough patch — but I'll mow on."

The joke is 109 characters long, well inside the competition's 200-character
limit, and it was invented for this entry: a clean pun ("rough patch" /
"mow on") delivered straight-faced, with the punchline at the end, meant to
be told out loud across a dinner table.

## How it works

`main.py` (Python 3.13, standard library only) holds the joke as a fixed
string and writes it, UTF-8 encoded, to `entry.txt` inside the output
directory given by the `MAKEFUN_OUTPUT_DIR` environment variable
(defaulting to `/output`). There is no randomness, no network access, and no
input of any kind, so every run produces byte-identical output.

## Running it

```sh
python3 main.py
```

To choose the output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Verification

Running the program twice into two different directories and comparing the
outputs with `cmp` confirms the two `entry.txt` files are byte-identical,
and the file is 109 characters, inside the gate's 1–200 character range.

## License

MIT — see [LICENSE](LICENSE).
