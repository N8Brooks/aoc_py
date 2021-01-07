#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/3
"""


from math import ceil, sqrt
from operator import add
from itertools import takewhile, repeat

from iteration_utilities import applyfunc

from data.utils import get_input


NEIGHBORS = (-1 + 0j, 1 + 0j, -1 + 1j, 0 + 1j, 1 + 1j, -1 - 1j, 0 - 1j, 1 - 1j)


def part1(text):
    n = int(text) + 1
    layer = ceil(sqrt(n) / 2 - 0.5)
    return layer + abs(((n - 1) % (2 * layer) - layer)) - 1


def part2(text):
    def move(c):
        if 0 == c.real == c.imag:
            return 1
        elif -c.real < c.imag:
            return c + 1j if c.imag < c.real else c - 1
        else:
            return c - 1j if c.real < c.imag else c + 1

    n = int(text)
    grid = {(c := 0): 1}

    for c in takewhile(lambda _: grid[c] <= n, applyfunc(move, c)):
        grid[c] = sum(grid.get(x, 0) for x in map(add, repeat(c), NEIGHBORS))

    return grid[c]


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2017, 3)

    print(part1(text))
    print(part2(text))
