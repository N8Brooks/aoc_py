#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/18
"""


from functools import partial
from operator import eq

from iteration_utilities import applyfunc, nth
import numpy as np
from scipy.signal import convolve2d

from data.utils import get_input


def process(line):
    return tuple(map(partial(eq, "#"), line))


def part1(text, steps=100):
    def step(grid):
        neighbors = convolve2d(grid, np.ones((3, 3)), "same") - grid
        return (neighbors == 3) | (grid & (neighbors == 2))

    grid = np.array(tuple(map(process, text.splitlines())))

    return (nth(steps - 1)(applyfunc(step, grid)) if steps else grid).sum()


def part2(text, steps=100):
    def step(grid):
        neighbors = convolve2d(grid, np.ones((3, 3)), "same") - grid
        return (neighbors == 3) | (grid & (neighbors == 2)) | on

    grid = np.array(tuple(map(process, text.splitlines())))
    on = np.zeros_like(grid)
    on[0, 0] = on[0, -1] = on[-1, 0] = on[-1, -1] = True
    grid |= on

    return (nth(steps - 1)(applyfunc(step, grid)) if steps else grid).sum()


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2015, 18)

    print(part1(text))
    print(part2(text))
