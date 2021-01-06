#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/5
"""


from itertools import islice, starmap
from operator import eq, ne

from more_itertools import pairwise

from data.utils import get_input


def part1(text):
    def nice(string):
        if any(two in string for two in ("ab", "cd", "pq", "xy")):
            return False

        if all(starmap(ne, pairwise(string))):
            return False

        return 3 <= sum(map(string.count, "aeiou"))

    return sum(map(nice, text.split()))


def part2(text):
    def split_pair(string, start):
        return any(starmap(eq, pairwise(islice(string, start, None, 2))))

    def twin_pair(first, second):
        if second in seen:
            return True
        seen.add(first)

    def nice(string):
        if not split_pair(string, 0) and not split_pair(string, 1):
            return False

        seen.clear()

        return any(starmap(twin_pair, pairwise(pairwise(string))))

    seen = set()

    return sum(map(nice, text.split()))


if __name__ == "__main__":
    text = get_input(2015, 5)

    print(part1(text))
    print(part2(text))
