#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/13
"""


from collections import defaultdict
from itertools import permutations
import re

from iteration_utilities import successive

from data.utils import get_input


class Family:
    __r = re.compile(
        r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)."
    )

    def __init__(self, raw):
        self.pairs = defaultdict(int)

        for line in raw.strip().split("\n"):
            a, sign, value, b = Family.__r.match(line).groups()
            mult = 1 if sign == "gain" else -1
            self.pairs[frozenset((a, b))] += mult * int(value)

        self.individuals = {x for xy in self.pairs for x in xy}

    def happiness(self, order):
        res = sum(self.pairs.get(frozenset(ab), 0) for ab in successive(order))
        res += self.pairs.get(frozenset((order[0], order[-1])), 0)
        return res

    def __iter__(self):
        yield from map(self.happiness, permutations(self.individuals))


def part1(text):
    return max(Family(text))


def part2(text):
    family = Family(text)
    family.individuals.add("Santa's helper")
    return max(family)


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2015, 13)

    print(part1(text))
    print(part2(text))
