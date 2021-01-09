#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/15
"""


from itertools import islice, filterfalse
import re

from iteration_utilities import applyfunc, count_items, packed

from data.utils import get_input


BITS = (1 << 16) - 1

DIVISOR = 2147483647


def count(a_gen, b_gen, sample):
    def valid(a, b):
        return a & BITS == b & BITS

    return count_items(islice(zip(a_gen, b_gen), sample), packed(valid))


def part1(text, a_mult=16807, b_mult=48271, sample=int(4e7)):
    a_start, b_start = map(int, re.findall(r"\d+", text))

    a_gen = applyfunc(lambda a: (a_mult * a) % DIVISOR, a_start)
    b_gen = applyfunc(lambda b: (b_mult * b) % DIVISOR, b_start)

    return count(a_gen, b_gen, sample)


def part2(text, a_mult=16807, b_mult=48271, sample=int(5e6)):
    a_start, b_start = map(int, re.findall(r"\d+", text))

    a_gen = applyfunc(lambda a: (a_mult * a) % DIVISOR, a_start)
    a_gen = filterfalse(lambda a: a % 4, a_gen)
    b_gen = applyfunc(lambda b: (b_mult * b) % DIVISOR, b_start)
    b_gen = filterfalse(lambda b: b % 8, b_gen)

    return count(a_gen, b_gen, sample)


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2017, 15)

    print(part1(text))
    print(part2(text))
