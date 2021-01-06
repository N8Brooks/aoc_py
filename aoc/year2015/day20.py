#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/20
"""


import numpy as np

from data.utils import get_input


# TODO: there are better solutions than brute force


def part1(text):
    n = int(text)
    houses = np.full(n // 10 + 2, 10, int)
    houses[0] = 0
    for i in range(2, n // 10 + 2):
        houses[i::i] += 10 * i
    return np.argmax(houses >= n)


def part2(text):
    n = int(text)
    houses = np.zeros(n // 10 + 2, int)
    for i in range(1, n // 10 + 2):
        houses[i : i * 50 + 1 : i] += 11 * i
    return np.argmax(houses >= n)


if __name__ == "__main__":
    text = get_input(2015, 20)

    print(part1(text))
    print(part2(text))
