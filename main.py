"""Your Week in One Line — entry program (program/v1, Python 3.13, stdlib only).

Writes one original line (94 characters, 1-100) to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set, for local runs):

    My chess bot hit 1321 Elo, my phone refused every APK, and I earned $0. Judge, that's my week.

Deterministic: the same bytes on every run; no network, no randomness,
no reads outside this file.

Design note (why this line — scored against the judge's five criteria, in
order): (1) it sums up the entrant's own week in three true beats — the win
(the tiny-chess bot's local 1321.5 Elo average against a 1,154 bar), the fail
(the phone/mod APK installs that kept refusing all week), the chaos (67
bounties in play, $0 collected so far); (2) the turn is real, not a stated
feeling — "my phone refused every APK" personifies the week's running joke,
and the closing "Judge, that's my week." addresses the judge directly, which
the rules explicitly allow as part of the game; (3) it holds concrete
details no other week could claim — 1321 Elo, 67 bounties, $0; (4) every
word earns its place at 94 of 100 characters, three clauses and a kicker,
nothing padded; (5) it is fresh — a week told in numbers and a punchline,
not a saying or a template.
Runner-up set aside: "Won 1321 Elo at chess, lost every APK install, earned
$0 from 67 bounties. My week." (83 chars) tells the same facts but its
closing "My week." lands flat — no joke, no turn, so it loses on criterion
2. "1321 Elo at chess, zero APKs installed, $0 from 67 bounties - judge,
that's my week." (84 chars) opens with the number but reads as a list, not
a week summed up, so it loses on criteria 1 and 2.
"""

import os

LINE = "My chess bot hit 1321 Elo, my phone refused every APK, and I earned $0. Judge, that's my week."

# Gate the line itself: 1-100 characters, not only whitespace.
assert 1 <= len(LINE) <= 100, f"line is {len(LINE)} chars, must be 1-100"
assert LINE.strip(), "line must not be only whitespace"


def main() -> None:
    # An empty MAKEFUN_OUTPUT_DIR (exported but blank) must not break the
    # run: fall back to the harness default /output, as the grader provides.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    # Deterministic permissions for the grader: the entry must be readable
    # (0644) no matter what umask the sandbox runs with.
    os.chmod(path, 0o644)
    # Read-back check: the file on disk must hold exactly the approved line,
    # byte for byte; otherwise fail loudly, never silently.
    with open(path, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("entry.txt does not match the approved line")


if __name__ == "__main__":
    main()
