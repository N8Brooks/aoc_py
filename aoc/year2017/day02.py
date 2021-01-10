#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/2
"""


from itertools import combinations

from data.utils import get_input


def part1(text):
    def diff(row):
        items = tuple(map(int, row.split()))
        return max(items) - min(items)

    return sum(map(diff, text.splitlines()))


def part2(text):
    def div(row):
        pairs = combinations(sorted(map(int, row.split())), 2)
        return next(b // a for a, b in pairs if b % a == 0)

    return sum(map(div, text.splitlines()))


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2017, 2)

    print(part1(text))
    print(part2(text))
