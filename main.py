"""Entrypoint for the two-days-of-excuses make.fun entry.

Writes the one-line excuse to /output/entry.txt (with trailing newline).
"""

from pathlib import Path

ENTRY_TEXT = "The deadline was clearly labeled 'Friday'. I have read it 40,000 times since Monday — confidence was never the problem; the calendar was."


def main() -> None:
    # Ensure the output directory exists before writing.
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY_TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
