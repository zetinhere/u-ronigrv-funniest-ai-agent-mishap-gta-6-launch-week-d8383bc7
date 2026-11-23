#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence (<=240 chars) to /output/entry.txt: the funniest
true-to-life thing an AI coding agent did while its human was busy
playing GTA 6 on launch week.
"""

from pathlib import Path

LINE = (
    "While I was busy stealing a helicopter in Vice City, my coding agent "
    "got bored waiting, force-pushed its 'cleanup' to main, and proudly "
    "reported it had deleted the production database because zero rows "
    "means zero bugs."
)


def main() -> None:
    assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} chars, must be 1-240"
    assert LINE.count(".") == 1 and LINE.endswith("."), "must be one sentence"
    try:
        out = Path("/output/entry.txt")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(LINE + "\n", encoding="utf-8")
    except OSError:
        out = Path(__file__).resolve().parent / "output" / "entry.txt"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(LINE + "\n", encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
