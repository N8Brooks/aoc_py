#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/1
"""


from itertools import accumulate, chain, repeat
from operator import mul
import re


from aoc.utils import get_input


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
    def visited(location):
        if location in previous:
            return True
        previous.add(location)

    previous = set()

    movements = chain.from_iterable(map(repeat, *process(text)))
    locations = accumulate(movements, initial=0)

    return manhatten(next(filter(visited, locations)))


if __name__ == "__main__":
    text = get_input(2016, 1)

    print(part1(text))
    print(part2(text))
