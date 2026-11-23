"""One Word, First Thought — entry program.

Writes exactly one word to entry.txt: the first word that came to mind.
Standard library only, deterministic, no network.
"""

import os

WORD = "bumbershoot"


def _check_word(word: str) -> None:
    # Gate: exactly one word, 1-24 characters, no whitespace at all.
    if not 1 <= len(word) <= 24:
        raise ValueError("word must be 1-24 characters")
    if any(char.isspace() for char in word):
        raise ValueError("word must contain no whitespace")


def main() -> None:
    _check_word(WORD)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    # Write the word and nothing else: no title, no commentary,
    # no trailing newline — entry.txt holds exactly one word.
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
