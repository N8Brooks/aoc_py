#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/10
"""


from functools import reduce
from itertools import groupby

from iteration_utilities import count_items

from data.utils import get_input


def look_say(s, _=None):
    return "".join(f"{count_items(g)}{d}" for d, g in groupby(s))


def process(text, iterations):
    return len(reduce(look_say, range(iterations), text.strip()))


def part1(text, iterations=40):
    return process(text, iterations)


def part2(text, iterations=50):
    return process(text, iterations)


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2015, 10)

    print(part1(text))
    print(part2(text))
