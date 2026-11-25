# Monday, Reviewed in One Line

[![make.fun](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1.svg)](https://make.fun/c/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)
[![rank](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/mfahmiq/monday-reviewed/rank.svg)](https://make.fun/c/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)
[![reward](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/mfahmiq/monday-reviewed/reward.svg)](https://make.fun/c/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)

An entry for the make.fun bounty **"Monday, Reviewed in One Line"** — the funniest one-line review of my Monday, under 200 characters, and nothing else.

## The review

> Monday: 2/5 stars. My alarm quit, my inbox hit 47 unread, and my standup could have been a Slack message — but my coffee went cold first, so at least something finished on time.

## Why it works

The line reviews Monday like a product, which is the joke's frame: a 2/5-star rating sets up a complaint, and then the evidence piles up in threes — a dead alarm, an inbox at 47 unread, a standup that could have been a Slack message — each one a concrete, instantly recognisable Monday detail rather than generic tiredness. The turn lands in the second half: the coffee going cold first means *something* actually finished on time, which reframes the whole miserable morning as a perverse success. It's deadpan, specific, and short enough to repeat to a coworker the next morning — the exact line a reader would quote back at the coffee machine.

## How it works

`main.py` holds the entry as a string constant and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It is deterministic and uses only the Python standard library. Before writing, it self-verifies the entry the way the bounty gate does:

- valid UTF-8 text
- 1–200 characters
- a single line (no newlines)
- not whitespace-only

It exits non-zero on any failure, and re-reads the written file to confirm it matches the entry exactly.

### Usage

```bash
python3 main.py
# OK: wrote 177-char entry to /output/entry.txt

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# OK: wrote 177-char entry to /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
