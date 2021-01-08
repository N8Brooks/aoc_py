#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/12
"""


from functools import partial
from itertools import repeat
from operator import eq

from iteration_utilities import count_items

from data.utils import get_input


def unite(text):
    def find(a):
        return a if a == parent.setdefault(a, a) else find(parent[a])

    parent = {}

    for line in text.strip().split("\n"):
        a, bs = line.split(" <-> ")
        parent.update(zip(map(find, bs.split(", ")), repeat(find(a))))

    return parent, find


def part1(text, group="0"):
    parent, find = unite(text)

    return count_items(map(find, parent.values()), find(group), True)


def part2(text):
    parent, find = unite(text)

    return len(set(map(find, parent.values())))


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2017, 12)

    print(part1(text))
    print(part2(text))
