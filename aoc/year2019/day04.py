#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2019/day/4
"""


from itertools import starmap
import multiprocessing as mp
from operator import le

from iteration_utilities import successive

from data.utils import get_input


LIMIT = 1000


def is_sorted(n):
    return all(starmap(le, successive(n)))


def check1(start, stop, step=mp.cpu_count()):
    def check(digits):
        return is_sorted(digits) and any(2 <= digits.count(d) for d in set(digits))

    return sum(check(str(n)) for n in range(start, stop, step))


def check2(start, stop, step=mp.cpu_count()):
    def check(digits):
        return is_sorted(digits) and 2 in map(digits.count, set(digits))

    return sum(check(str(n)) for n in range(start, stop, step))


def process(func, text):
    lo, hi = map(int, text.split("-"))
    if LIMIT < hi - lo:
        args = ((lo + i, hi + 1) for i in range(mp.cpu_count()))
        with mp.Pool() as p:
            return sum(p.starmap(func, args))
    else:
        return func(lo, hi + 1, 1)


def part1(text):
    return process(check1, text)


def part2(text):
    return process(check2, text)


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2019, 4)

    print(part1(text))
    print(part2(text))
