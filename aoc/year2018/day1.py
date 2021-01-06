#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2018/day/1
"""


from itertools import accumulate, cycle

from iteration_utilities import duplicates

from data.utils import get_input


def part1(text):
    return sum(map(int, text.split()))


def part2(text):
    frequencies = accumulate(cycle(map(int, text.split())), initial=0)

    return next(duplicates(frequencies))


if __name__ == "__main__":
    text = get_input(2018, 1)

    print(part1(text))
    print(part2(text))
