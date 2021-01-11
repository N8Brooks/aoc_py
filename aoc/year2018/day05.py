#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2018/day/5
"""


from functools import reduce
from string import ascii_lowercase as lower, ascii_uppercase as upper

from iteration_utilities import successive

from data.utils import get_input


REACTIONS = frozenset(f"{a}{A}" for a, A in zip(f"{lower}{upper}", f"{upper}{lower}"))


def part1(text):
    def remove(polymer, reaction):
        return polymer.replace(reaction, "")

    polymer = text.strip()

    while react := REACTIONS & frozenset(map("".join, successive(polymer))):
        polymer = reduce(remove, react, polymer)

    return len(polymer)


def part2(text):
    return min(part1(text.replace(a, "").replace(a.upper(), "")) for a in lower)


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2018, 5)

    print(part1(text))
    print(part2(text))
