#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/19
"""


from collections import defaultdict
from itertools import chain, starmap
from random import shuffle
import re

from iteration_utilities import empty

from data.utils import get_input


def part1(text):
    def replace(i, token):
        for replacement in replacements.get(token, empty):
            tokens[i] = replacement
            yield "".join(tokens)
        tokens[i] = token

    def tokenize(molecule):
        return re.findall(r"[A-Z][a-z]?", molecule)

    lines, molecule = text.strip().split("\n\n")

    replacements = defaultdict(list)
    for line in lines.split("\n"):
        key, val = line.split(" => ")
        replacements[key].append(val)

    tokens = tokenize(molecule)

    return len(set(chain.from_iterable(starmap(replace, enumerate(tokens)))))


def part2(text, starting="e"):
    def process(line):
        return line.split(" => ")

    lines, molecule = text.strip().split("\n\n")
    replacements = list(map(process, lines.split("\n")))
    saved, steps = molecule, 0

    while molecule != starting:
        for x, y in replacements:
            if y not in molecule:
                continue

            molecule = molecule.replace(y, x, 1)
            steps += 1
            break
        else:
            shuffle(replacements)
            molecule, steps = saved, 0

    return steps


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2015, 19)

    print(part1(text))
    print(part2(text))
