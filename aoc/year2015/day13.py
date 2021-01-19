#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/13
"""


from collections import defaultdict
from functools import cache
import re

from data.utils import get_input


class Family:
    r = re.compile(r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).")

    def __init__(self, text, buffer=False):
        self.individuals = {}
        self.pairs = defaultdict(int)

        for line in text.splitlines():
            a, sign, val, b = Family.r.match(line).groups()
            a = self.individuals.setdefault(a, len(self.individuals))
            b = self.individuals.setdefault(b, len(self.individuals))
            self.pairs[(1 << a) | (1 << b)] += int(val) if sign == "gain" else -int(val)

        self.n = len(self.individuals) + buffer

    @cache
    def happiness(self, i=0, s=1):
        def add(j):
            return self.pairs[(1 << i) | (1 << j)] + self.happiness(j, s | (1 << j))

        if s == (1 << self.n) - 1:
            return self.pairs[1 | (1 << i)]

        return max(add(j) for j in range(self.n) if not (s & (1 << j)))


def part1(text):
    return Family(text).happiness()


def part2(text):
    return Family(text, True).happiness()


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2015, 13)

    print(part1(text))
    print(part2(text))
