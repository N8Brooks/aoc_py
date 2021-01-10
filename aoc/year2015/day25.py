#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/25
"""

import re

from data.utils import get_input


def part1(text, code=20151125, mult=252533, mod=33554393):
    row, col = map(int, re.findall(r"\d+", text))

    n = (row + col - 1) * (row + col - 2) // 2 + col - 1

    return code * pow(mult, n, mod) % mod


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2015, 25)

    print(part1(text))
