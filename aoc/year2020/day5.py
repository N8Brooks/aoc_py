#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2020/day/5
"""


import re

from iteration_utilities import minmax

from data.utils import get_input


def location(path, dirs=str.maketrans(dict(B="1", R="1", F="0", L="0"))):
    return int(path.translate(dirs), 2)


def part1(text):
    return max(map(location, text.splitlines()))


def part2(text):
    taken = set(map(location, text.splitlines()))
    lo, hi = minmax(taken)

    return taken.symmetric_difference(range(lo, hi + 1)).pop()


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2020, 5)

    print(part1(text))
    print(part2(text))
