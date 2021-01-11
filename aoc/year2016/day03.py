#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/3
"""


from itertools import chain

from more_itertools import ichunked

from data.utils import get_input


def total(iterable):
    return sum(tri[2] < tri[0] + tri[1] for tri in map(sorted, iterable))


def process(text):
    return (map(int, tri.split()) for tri in text.splitlines())


def part1(text):
    return total(process(text))


def part2(text):
    return total(ichunked(chain.from_iterable(zip(*process(text))), 3))


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2016, 3)

    print(part1(text))
    print(part2(text))
