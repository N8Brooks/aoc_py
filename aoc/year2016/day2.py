#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/2
"""


from itertools import accumulate, islice
from functools import reduce


from aoc.utils import get_input


DIRS = {"L": -1, "U": 1j, "R": 1, "D": -1j}

KEYPAD_A = {
    -1 + 1j: "1",
    0 + 1j: "2",
    1 + 1j: "3",
    -1 + 0j: "4",
    0 + 0j: "5",
    1 + 0j: "6",
    -1 - 1j: "7",
    0 - 1j: "8",
    1 - 1j: "9",
}

KEYPAD_B = {
    0 + 2j: "1",
    -1 + 1j: "2",
    0 + 1j: "3",
    1 + 1j: "4",
    -2 + 0j: "5",
    -1 + 0j: "6",
    0 + 0j: "7",
    1 + 0j: "8",
    2 + 0j: "9",
    -1 - 1j: "A",
    0 - 1j: "B",
    1 - 1j: "C",
    0 - 2j: "D",
}


def simulate(text, keys, start):
    def act(cur, move):
        nxt = cur + DIRS[move]
        return nxt if nxt in keys else cur

    def row(loc, moves):
        return reduce(act, moves, loc)

    keycode = islice(accumulate(text.split(), row, initial=start), 1, None)

    return "".join(map(keys.get, keycode))


def part1(text, initial=0 + 0j):
    return simulate(text, KEYPAD_A, initial)


def part2(text, initial=-2 + 0j):
    return simulate(text, KEYPAD_B, initial)


if __name__ == "__main__":
    text = get_input(2016, 2)

    print(part1(text))
    print(part2(text))
