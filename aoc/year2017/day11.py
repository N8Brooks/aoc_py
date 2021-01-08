#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/11
"""


from itertools import accumulate

from data.utils import get_input


DIRS = {
    "nw": 1 - 0j,
    "n": 0 + 1j,
    "ne": -1 + 1j,
    "se": -1 + 0j,
    "s": 0 - 1j,
    "sw": 1 - 1j,
}


def dist(c):
    return int((abs(c.imag) + abs(c.imag + c.real) + abs(c.real)) // 2)


def part1(text):
    return dist(sum(map(DIRS.get, text.strip().split(","))))


def part2(text):
    return max(map(dist, accumulate(map(DIRS.get, text.strip().split(",")))))


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2017, 11)

    print(part1(text))
    print(part2(text))
