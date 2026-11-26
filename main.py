#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — writes the entry line to /output/entry.txt.

The line is a washing machine reporting the one failure nobody writes
error codes for: the cycle finished yesterday and the load was never
collected. It was picked by duelling a dozen drafts, in both orders,
against the competition's published judge brief and against the strongest
lines sampled from the live field (2,044 entries; the sock, unbalanced
load, burnt toast and frozen-middle lanes are saturated and were avoided).
The winning shape pairs the field's proven identity reduction ("I am now
a clock with a door") with a fault no sampled entry uses. The full draft
list and duel record are in candidates.md.
"""

import os

# The line is built in three beats: the flat report (a wash that finished
# yesterday at a stated time), the absence (nobody came to unload it), and
# the consequence stated as a change of identity — the machine has become
# the swamp its load is sitting in.
REPORT = "Wash finished yesterday at 14:02."
ABSENCE = "Nobody came."
TWIST = "Your clothes are still wet in the dark, and I am a swamp with a door now."
LINE = " ".join((REPORT, ABSENCE, TWIST))


def main() -> None:
    # Gate self-check: UTF-8 text, 1-200 chars, single line, not only space.
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert "\n" not in LINE and LINE.strip() == LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
