#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/10
"""


import re
from functools import reduce

from aoc.utils import get_input


def look_say(num, _=None, r=re.compile(r"(.)\1*")):
    return r.sub(lambda m: f"{len(m.group(0))}{m.group(1)}", num)


def process(text, iterations):
    return len(reduce(look_say, range(iterations), text.strip()))


def part1(text, iterations=40):
    return process(text, iterations)


def part2(text, iterations=50):
    return process(text, iterations)


if __name__ == "__main__":
    text = get_input(2015, 10)

    print(part1(text))
    print(part2(text))
