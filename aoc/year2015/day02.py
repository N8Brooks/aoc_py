#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/2
"""


from itertools import starmap

from data.utils import get_input


def process(text):
    return (sorted(map(int, line.split("x"))) for line in text.split())


def part1(text):
    return sum(3 * a * b + 2 * (a * c + b * c) for a, b, c in process(text))


def part2(text):
    return sum(a + a + b + b + a * b * c for a, b, c in process(text))


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2015, 2)

    print(part1(text))
    print(part2(text))
