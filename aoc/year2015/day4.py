#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/4
"""


from itertools import count
from hashlib import md5

from data.utils import get_input


def process(text, start):
    def valid(suffix):
        hasher = prefix.copy()
        hasher.update(str(suffix).encode())
        hexadecimal = hasher.hexdigest()
        return hexadecimal.startswith(start)

    prefix = md5(text.strip().encode())

    return next(filter(valid, count()))


def part1(text, start="00000"):
    return process(text, start)


def part2(text, start="000000"):
    return process(text, start)


if __name__ == "__main__":
    text = get_input(2015, 4)

    print(part1(text))
    print(part2(text))
