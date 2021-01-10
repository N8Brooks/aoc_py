#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/6
"""


import numpy as np
import re

from data.utils import get_input


def process(text, instruction, grid):
    r = re.compile(r"(\D+) (\d+),(\d+) through (\d+),(\d+)")

    for line in text.splitlines():
        instruction(*r.match(line).groups())

    return int(grid.sum())


def part1(text, size=1000):
    def instruction(action, *coordinates):
        x1, y1, x2, y2 = map(int, coordinates)
        x2, y2 = (x2 + 1, y2 + 1)

        if action == "toggle":
            grid[y1:y2, x1:x2] = 1 - grid[y1:y2, x1:x2]
        elif action:
            grid[y1:y2, x1:x2] = action == "turn on"

    grid = np.zeros((size, size), bool)

    return process(text, instruction, grid)


def part2(text, size=1000):
    def instruction(action, *coordinates):
        x1, y1, x2, y2 = map(int, coordinates)
        x2, y2 = (x2 + 1, y2 + 1)

        if action == "toggle":
            grid[y1:y2, x1:x2] += 2
        elif action == "turn on":
            grid[y1:y2, x1:x2] += 1
        else:
            grid[y1:y2, x1:x2] -= 1
            np.clip(grid[y1:y2, x1:x2], 0, None, grid[y1:y2, x1:x2])

    grid = np.zeros((size, size), int)

    return process(text, instruction, grid)


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2015, 6)

    print(part1(text))
    print(part2(text))
