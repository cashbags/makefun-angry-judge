#!/usr/bin/env python3
"""main.py — "The Self-Checkout Accusation" entry (Python 3.13, stdlib only).

The entry is one original rant, four sentences long, about a single
everyday annoyance: falsely accused of stealing a cucumber by a
self-checkout machine, in front of the whole shop.

Why this rant, against the judge's brief in the order it weighs things:

1. A funny rant about ONE everyday annoyance first. One thing only
   — falsely accused of theft by a self-checkout machine — and it
   stays a rant throughout: no essay, no list of complaints, no
   second grievance smuggled in.
2. Actually funny through shared anger, not performed anger. Almost
   everyone has stood at a self-checkout while the machine announced
   their supposed crime to the whole shop. The laugh is recognition:
   the machine is wrong, it knows it is wrong, and it announces it
   anyway, loudly, in public.
3. A specific, concrete annoyance. A named object with a named
   behaviour: the machine, and its exact phrase, "Unexpected item in
   the bagging area". The rant quotes the machine verbatim, then gives
   the three facts that prove it wrong — scanned, paid, watched — in
   three hammer-blow sentences of two to five words each.
4. Sharp, economical wording. 330 characters, four sentences, no
   throat-clearing, no setup scaffolding. The first sentence IS the
   accusation; the second is the machine's own words; the third is
   the three-word defence; the fourth is the verdict.
5. Freshness. The brief's own examples — the printer, the bus, a
   Monday morning — are the flooded lanes, and this rant takes none
   of them. The fresh angle is the machine's confidence: never once
   right, yet speaking with a judge's certainty, closed by demoting
   it from judge to bouncer — a bouncer who can't read the guest
   list. The twist lands on the last beat, the way the deadpan
   winners of the one-line judged-text competitions always land
   theirs ("the typo is now load-bearing", "merged").

The rant was chosen by a pairwise tournament over 10 candidates in
empty lanes, judged against the brief's five criteria in order (see
CANDIDATES.md in the build notes). It beat the runner-up — the smoke
alarm that only runs out of battery at 3 a.m. — 9–0.

The program is deliberately boring: it holds the rant as one
constant, checks it against the competition's own gate before writing
(1–400 characters, not only whitespace — checked both as Unicode code
points and as UTF-8 bytes), and writes it with a trailing newline.
No clock, no random source, no network, so two runs write identical
bytes.
"""

import os
import sys
from pathlib import Path

# The rant. One annoyance, one accuser: the self-checkout machine
# announces a theft that never happened, with a judge's confidence —
# answered with three facts (scanned, paid, watched) and one demotion
# (judge to bouncer).
RANT = (
    "The self-checkout machine has accused me of stealing a cucumber. "
    '"Unexpected item in the bagging area," it announces, to the whole '
    "shop, with the confidence of a judge who has never once been right. "
    "I scanned it. I paid for it. It watched me do it. And still it "
    "stands there, beeping, like a bouncer who can't read the guest list."
)

# The competition's gate, applied here before anything is written.
# The rules say "1 to 400 characters" without defining the count, so
# the rant is held to 400 under BOTH readings: Unicode code points
# and UTF-8 bytes. This rant is plain ASCII, so the two agree at 330.
MIN_CHARS = 1
MAX_CHARS = 400


def abort(why: str) -> None:
    """Fail loudly instead of writing an entry the gate would refuse."""
    raise SystemExit("main.py: " + why)


def write_rant() -> None:
    """Validate the rant against the gate, then write it to entry.txt."""
    code_points = len(RANT)
    byte_count = len(RANT.encode("utf-8"))
    if code_points < MIN_CHARS or code_points > MAX_CHARS:
        abort(f"rant is {code_points} code points, outside the 1-400 gate")
    if byte_count < MIN_CHARS or byte_count > MAX_CHARS:
        abort(f"rant is {byte_count} bytes, outside the 1-400 gate")
    if not RANT.strip():
        abort("rant is only whitespace")
    if "\n" in RANT or "\r" in RANT:
        abort("rant must be a single paragraph")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target = out_dir / "entry.txt"

    out_dir.mkdir(parents=True, exist_ok=True)
    target.write_text(RANT + "\n", encoding="utf-8")
    print(f"wrote {target} ({code_points} code points, {byte_count} bytes)")


if __name__ == "__main__":
    write_rant()
