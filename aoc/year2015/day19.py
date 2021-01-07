#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/19
"""


from collections import defaultdict, deque
import re

from more_itertools import consume

from data.utils import get_input


def process(text):
    # Don't actually need to use a dictionary
    lines, molecule = text.split("\n\n")

    replacements = defaultdict(list)
    for line in lines.split("\n"):
        key, val = line.split(" => ")
        replacements[key].append(val)

    return replacements, molecule


def tokenize(molecule):
    return re.findall(r"[A-Z][a-z]?", molecule)


def step():
    pass


def part1(text):
    # This could probably be improved by using f'{prefix}{replacement}{suffix}'
    replacements, molecule = process(text)
    tokens = tokenize(molecule)

    unique = set()
    for i, token in enumerate(tokens):
        for replacement in replacements.get(token, []):
            tokens[i] = replacement
            unique.add("".join(tokens))

        tokens[i] = token

    return len(unique)


def part2(text, starting="e"):
    pass


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2015, 19)

    print(part1(text))
    print(part2(text))
