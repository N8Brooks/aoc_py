#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2019/day/3
"""


from itertools import accumulate, repeat
from operator import add
import re


from data.utils import get_input


DIRS = {"U": 0 + 1j, "R": 1 + 0j, "D": 0 - 1j, "L": -1 + 0j}


def path(wire, r=re.compile(r"([URDL])(\d+)")):
    location = 0 + 0j
    for direction, distance in r.findall(wire):
        direction, distance = DIRS[direction], int(distance)
        start = location + direction
        moves = repeat(direction, distance - 1)
        yield from accumulate(moves, initial=start)
        location += direction * distance


def part1(text):
    def manhatten(location):
        return abs(location.imag) + abs(location.real)

    a, b = map(path, text.split())
    common = frozenset(a).intersection(b)

    return int(min(map(manhatten, common)))


def part2(text):
    def steps(wire):
        locations = {}
        for i, location in enumerate(path(wire), start=1):
            locations.setdefault(location, i)
        return locations

    a, b = map(steps, text.split())
    common = tuple(a.keys() & b.keys())

    return min(map(add, map(a.get, common), map(b.get, common)))


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2019, 3)

    print(part1(text))
    print(part2(text))
