#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/5
"""


from itertools import takewhile

from iteration_utilities import applyfunc
from more_itertools import ilen

from data.utils import get_input


def part1(text):
    def jump(i):
        instructions[i] += 1
        return i + instructions[i] - 1

    n = len(instructions := list(map(int, text.split())))

    return ilen(takewhile(lambda i: i < n, applyfunc(jump, 0))) + 1


def part2(text):
    def jump(i):
        jumps = instructions[i]
        instructions[i] += 1 if jumps < 3 else -1
        return i + jumps

    n = len(instructions := list(map(int, text.split())))

    return ilen(takewhile(lambda i: i < n, applyfunc(jump, 0))) + 1


if __name__ == "__main__":
    text = get_input(2017, 5)

    print(part1(text))
    print(part2(text))
