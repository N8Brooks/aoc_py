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


def ab(text, iterations):
    return len(reduce(look_say, range(iterations), text.strip()))


if __name__ == "__main__":
    text = get_input(2015, 10)

    print(ab(text, 40))
    print(ab(text, 50))
