#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun entry.

Writes one haiku about debugging (5-7-5, seventeen syllables) to
/output/entry.txt, per the bounty gate: UTF-8 text, 1-200 characters.

The haiku:
    The breakpoint holds still          (5 syllables)
    while the logs scroll past like rain (7 syllables)
    it was a typo                       (5 syllables)

Pure Python standard library, no dependencies, no network, no secrets.
"""

import os

HAIKU = (
    "The breakpoint holds still\n"
    "while the logs scroll past like rain\n"
    "it was a typo\n"
)

OUTPUT_PATH = "/output/entry.txt"


def count_syllables(line: str) -> int:
    """Syllable count for the haiku's own words (vowel groups per word).

    Kept deliberately small and exact for this fixed text: each word is
    counted by its vowel groups, with a silent trailing 'e' dropped.
    """
    total = 0
    for word in line.lower().split():
        word = word.strip(".,!?;:'\"")
        groups = 0
        prev_vowel = False
        for ch in word:
            is_vowel = ch in "aeiouy"
            if is_vowel and not prev_vowel:
                groups += 1
            prev_vowel = is_vowel
        if word.endswith("e") and groups > 1:
            groups -= 1
        total += max(groups, 1)
    return total


def main() -> None:
    text = HAIKU
    # Gate check: 1-200 characters, not only whitespace.
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    lines = text.strip().split("\n")
    assert len(lines) == 3, "haiku must be exactly three lines"
    # Form check: the 5-7-5 shape, seventeen syllables in total.
    assert [count_syllables(line) for line in lines] == [5, 7, 5], (
        "haiku must be 5-7-5 syllables"
    )

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
