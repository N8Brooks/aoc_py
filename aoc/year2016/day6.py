#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/6
"""


from collections import Counter
from statistics import mode

from aoc.utils import get_input


def part1(text):
    return "".join(map(mode, zip(*text.strip().split("\n"))))


def part2(text):
    def antimode(message):
        counts = Counter(message)
        return min(counts, key=counts.get)

    return "".join(map(antimode, zip(*text.strip().split("\n"))))


if __name__ == "__main__":
    text = get_input(2016, 6)

    print(part1(text))
    print(part2(text))
