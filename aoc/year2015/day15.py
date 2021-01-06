#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/15
"""


from itertools import repeat
import re

import numpy as np

from aoc.utils import get_input


R = re.compile(
    (
        r"(?:\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)"
    )
)


def process(text):
    processed = [R.match(line).groups() for line in text.strip().split("\n")]

    return np.array(processed, int).transpose()


def allocation(n, remaining=100):
    if (n := n - 1) == 0:
        yield [remaining]
        return

    for right in range(remaining + 1):
        for left in allocation(n, remaining - right):
            left.append(right)
            yield left


def score(allocations, matrix):
    totals = np.multiply(matrix, allocations).sum(axis=1)
    return np.clip(totals, 0, None).prod()


def part1(text):
    matrix = process(text)[:-1]

    return max(map(score, allocation(matrix.shape[1]), repeat(matrix)))


def part2(text, target=500):
    def valid(allocations):
        return (calories * allocations).sum() == target

    *matrix, calories = process(text)
    matrix = np.vstack(matrix)

    filtered = filter(valid, allocation(matrix.shape[1]))

    return max(map(score, filtered, repeat(matrix)))


if __name__ == "__main__":
    text = get_input(2015, 15)

    print(part1(text))
    print(part2(text))
