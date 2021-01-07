#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/1
"""


from itertools import accumulate, chain, repeat
from operator import mul
import re

from iteration_utilities import duplicates

from data.utils import get_input


def process(text, r=re.compile(r"([LR])(\d+)")):
    def turn(direction):
        return 1j if direction == "L" else -1j

    turns, dists = zip(*(r.match(line).groups() for line in text.split(", ")))

    return accumulate(map(turn, turns), mul), map(int, dists)


def manhatten(location):
    return int(abs(location.imag) + abs(location.real))


def part1(text):
    return manhatten(sum(map(mul, *process(text))))


def part2(text):
    movements = chain.from_iterable(map(repeat, *process(text)))

    return manhatten(next(duplicates(accumulate(movements, initial=0))))


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2016, 1)

    print(part1(text))
    print(part2(text))
