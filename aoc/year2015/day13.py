#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/13
"""


from collections import defaultdict
from itertools import permutations
import re

from more_itertools import consume, pairwise

from data.utils import get_input


class Family:
    __r = re.compile(
        r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)."
    )

    def __init__(self, raw):
        self.pairs = defaultdict(int)

        consume(map(self._process, raw.strip().split("\n")))

        self.individuals = {x for xy in self.pairs for x in xy}

    def _process(self, line):
        a, sign, value, b = Family.__r.match(line).groups()
        mult = 1 if sign == "gain" else -1
        self.pairs[frozenset((a, b))] += mult * int(value)

    def _pair(self, xy):
        return self.pairs[frozenset(xy)]

    def happiness(self, order):
        res = sum(map(self._pair, pairwise(order)))
        res += self._pair((order[-1], order[0]))
        return res

    def __iter__(self):
        yield from map(self.happiness, permutations(self.individuals))


def part1(text):
    return max(Family(text))


def part2(text):
    family = Family(text)
    family.individuals.add("Santa's helper")
    return max(family)


if __name__ == "__main__":
    text = get_input(2015, 13)

    print(part1(text))
    print(part2(text))
