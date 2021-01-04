#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/2
"""


from itertools import combinations

from aoc.utils import get_input


def a(text):
    def diff(row):
        items = tuple(map(int, row.split()))
        return max(items) - min(items)

    return sum(map(diff, text.strip().split("\n")))


def b(text):
    def div(row):
        pairs = combinations(sorted(map(int, row.split())), 2)
        return next(y // x for x, y in pairs if y % x == 0)

    return sum(map(div, text.strip().split("\n")))


if __name__ == "__main__":
    text = get_input(2017, 2)

    print(a(text))
    print(b(text))
