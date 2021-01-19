#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/13
"""


from collections import defaultdict
from functools import cache
import re

from data.utils import get_input


def family(text, buffer=False):
    @cache
    def happiness(i, s):
        def add(j):
            return pairs[(1 << i) | (1 << j)] + happiness(j, s | (1 << j))

        if s == (1 << n) - 1:
            return pairs[1 | (1 << i)]

        return max(add(j) for j in range(n) if not (s & (1 << j)))

    r = re.compile(r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).")

    individuals = {}
    pairs = defaultdict(int)

    for line in text.splitlines():
        a, sign, val, b = r.match(line).groups()
        a = individuals.setdefault(a, len(individuals))
        b = individuals.setdefault(b, len(individuals))
        pairs[(1 << a) | (1 << b)] += int(val) if sign == "gain" else -int(val)

    n = len(individuals) + buffer

    return happiness(0, 1)


def part1(text):
    return family(text)


def part2(text):
    return family(text, True)


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2015, 13)

    print(part1(text))
    print(part2(text))
