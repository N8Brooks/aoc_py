#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2020/day/12
"""


import re

from data.utils import get_input


R = re.compile(r"([NESWLRF])(\d+)")

DIRS = {"N": 0 + 1j, "E": 1 + 0j, "S": 0 - 1j, "W": -1 + 0j}


def manhatten(c):
    return int(abs(c.real) + abs(c.imag))


def part1(text):
    def move(line):
        nonlocal direction
        action, value = R.match(line).groups()

        if action == "L":
            direction *= pow(1j, int(value) // 90)
        elif action == "R":
            direction *= pow(-1j, int(value) // 90)
        elif action == "F":
            return direction * int(value)
        else:
            return DIRS[action] * int(value)

        return 0 + 0j

    direction = 1 + 0j

    return manhatten(sum(map(move, text.splitlines())))


def part2(text, size=25):
    def move(line):
        nonlocal waypoint
        action, value = R.match(line).groups()

        if action == "L":
            waypoint *= pow(1j, int(value) // 90)
        elif action == "R":
            waypoint *= pow(-1j, int(value) // 90)
        elif action == "F":
            return waypoint * int(value)
        else:
            waypoint += DIRS[action] * int(value)

        return 0 + 0j

    waypoint = 10 + 1j

    return manhatten(sum(map(move, text.splitlines())))


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2020, 12)

    print(part1(text))
    print(part2(text))
