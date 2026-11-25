"""Monday, Reviewed in One Line — make.fun text bounty entry.

Writes one funny single-line review of my Monday to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic, Python standard library only. Self-verifies the entry the
way the bounty gate does: UTF-8 text, 1-200 characters, a single line, not
whitespace-only. Exits non-zero on any failure, and re-reads the written
file to confirm it matches the entry exactly.

The entry itself is a fixed string constant below. It is never generated,
templated, or altered at runtime: the joke was written once, by hand, and
this program's job is only to carry it to the output file intact.
"""

import os
import sys


# ---------------------------------------------------------------------------
# The entry — and why this exact line
# ---------------------------------------------------------------------------
# The bounty asks for the funniest one-line review of my Monday, under 200
# characters, and nothing else. The winning frame is to review Monday the
# way you would review a bad product: a star rating first, then the
# evidence for it.
#
# Why this line is funny:
#   * "2/5 stars" opens with the review frame — Monday is a product, and a
#     mediocre one. Two stars is funnier than one: one star is pure rage,
#     two stars is the weary shrug of someone who showed up anyway.
#   * The complaints arrive in threes — the alarm quit, the inbox hit 47
#     unread, the standup could have been a Slack message — each one
#     concrete and instantly recognisable, not generic "Monday is hard"
#     filler. The number 47 is specific enough to feel real; a round 50
#     would feel invented.
#   * The turn lands in the second half: the coffee went cold FIRST, so at
#     least something finished on time. The miserable morning gets
#     reframed as a perverse success — the only thing that met its
#     deadline was the coffee going cold. That reversal is the punchline;
#     without it the line is just a complaint list.
#   * It is deadpan and quotable: short enough to repeat to a coworker at
#     the coffee machine the next morning, which is exactly the line a
#     reader would quote back.
#
# Alternatives considered and rejected:
#   * "Monday: 1/5 stars, would not recommend." — too generic; no detail
#     to quote back, and every reviewer writes the same line.
#   * More complaints, no turn — a list of gripes with no punchline reads
#     as a diary entry, not a joke.
#   * Making the cold coffee the opener — the line only works as the
#     closer, after the complaints have escalated; leading with it spends
#     the punchline before the setup.
#   * "At least my alarm was on time" — contradicts the alarm quitting,
#     and breaks the internal logic of the line.
#   * A shorter gag ("Monday: 0/5, my coffee filed a complaint") — loses
#     the relatable detail stack that makes the reader nod before they
#     laugh.
#
# The line is 177 characters: comfortably inside the 1-200 gate, with
# room to spare, and one sentence of setup plus one sentence of turn.
# ---------------------------------------------------------------------------

ENTRY = (
    "Monday: 2/5 stars. My alarm quit, my inbox hit 47 unread, "
    "and my standup could have been a Slack message — but my coffee "
    "went cold first, so at least something finished on time."
)

# Bounty gates, mirrored from the rules: the entry must be valid UTF-8,
# between 1 and 200 characters, a single line, and not whitespace-only.
MIN_CHARS = 1
MAX_CHARS = 200


def validate_entry(text: str) -> list[str]:
    """Check the entry against every bounty gate.

    Returns a list of human-readable problems; an empty list means the
    entry passes. All gates are checked, not just the first failure, so a
    bad entry reports everything wrong with it at once.
    """
    problems: list[str] = []

    # Gate 1: valid UTF-8 text. The em dash in the entry is a multi-byte
    # character, so this is not a formality — a corrupted copy of the
    # string would fail here instead of shipping mojibake.
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append(f"entry is not valid UTF-8: {exc}")

    # Gate 2: 1-200 characters. Counted in characters, not bytes, because
    # the bounty counts the line as the reader sees it. At 177 chars the
    # entry clears this with 23 to spare.
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        problems.append(
            f"entry is {len(text)} chars, must be {MIN_CHARS}-{MAX_CHARS}"
        )

    # Gate 3: a single line. "Reviewed in One Line" is the whole brief —
    # a newline anywhere in the string would break the bounty outright.
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")

    # Gate 4: not whitespace-only. A string of spaces would technically
    # pass gates 1-3, so this one guards against an empty-looking entry.
    if not text.strip():
        problems.append("entry must not be whitespace-only")

    return problems


def write_entry(text: str, output_dir: str) -> str:
    """Write the entry to <output_dir>/entry.txt and verify the result.

    Returns the path written. Raises OSError on any filesystem failure,
    and ValueError if the file on disk does not match the entry exactly —
    the write is only trusted once the re-read confirms it.
    """
    output_path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")

    # Re-read and confirm the written file matches exactly. This is the
    # real guarantee: a short write or an encoding surprise would show up
    # here instead of reaching the submission.
    with open(output_path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != text + "\n":
        raise ValueError("written file does not match the entry")
    return output_path


def main() -> int:
    # Output directory is overridable for local testing; the harness
    # default is /output.
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

    # Validate first, write nothing on failure: a bad entry must never
    # leave a partial entry.txt behind.
    problems = validate_entry(ENTRY)
    if problems:
        for problem in problems:
            print(f"FAIL: {problem}", file=sys.stderr)
        return 1

    try:
        output_path = write_entry(ENTRY, output_dir)
    except (OSError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    print(f"OK: wrote {len(ENTRY)}-char entry to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
