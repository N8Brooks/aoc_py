#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2018/day/3
"""


from collections import defaultdict
from itertools import chain, product, starmap
import re

from iteration_utilities import duplicates, empty

from data.utils import get_input


def part1(text):
    def process(line):
        x, y, width, height = map(int, r.match(line).groups())
        return starmap(complex, product(range(x, x + width), range(y, y + height)))

    r = re.compile(r"#\d+ @ (\d+),(\d+): (\d+)x(\d+)")

    return len(set(duplicates(chain.from_iterable(map(process, text.splitlines())))))


def part2(text):
    r = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
    seen = defaultdict(list)
    ones = set()

    for line in text.splitlines():
        num, x, y, width, height = map(int, r.match(line).groups())
        ones.add(num)

        for val in starmap(complex, product(range(x, x + width), range(y, y + height))):
            taken = val in seen
            seen[val].append(num)
            ones.difference_update(seen[val] if taken else empty)

    return ones.pop()


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2018, 3)

    print(part1(text))
    print(part2(text))
