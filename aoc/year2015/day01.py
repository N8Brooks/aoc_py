#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/1
"""


from itertools import accumulate

from data.utils import get_input


def part1(text):
    return text.count("(") - text.count(")")


def part2(text):
    def direction(char):
        return 1 if char == "(" else -1

    position_floor = enumerate(accumulate(map(direction, text)), start=1)

    return next(i for i, floor in position_floor if floor < 0)


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2015, 1)

    print(part1(text))
    print(part2(text))
