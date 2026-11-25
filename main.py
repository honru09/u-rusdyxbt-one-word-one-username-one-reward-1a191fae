#!/usr/bin/env python3
"""One Word, One Username, One Reward — make.fun entry.

Writes the entrant's own make.fun username, one word, to
``entry.txt`` inside the output directory.

The word is ``honn-ru-honru``: the entrant's genuine handle on
make.fun, exactly as registered. One word, 14 characters.

Stdlib only. No network. Deterministic: the same bytes on every run.
"""

import os

WORD = "honn-ru-honru"


def main() -> None:
    # Guard: the entry must be exactly one word, 1-30 chars, no
    # surrounding whitespace. Fail loudly rather than write bad output.
    word = WORD.strip()
    assert word == WORD, "word must have no surrounding whitespace"
    assert 1 <= len(word) <= 30, "word must be 1-30 characters long"
    assert " " not in word and "\n" not in word, "word must be a single word"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(word)
    # Only ever chmod the file this program itself created.
    # Never chmod, remove, or alter the output directory itself.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
