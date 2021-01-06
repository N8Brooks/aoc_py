#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/8
"""


import re

from data.utils import get_input


def part1(text):
    def count(line):
        return len(line) - len(line.encode().decode("unicode_escape")) + 2

    return sum(map(count, text.split()))


def part2(text):
    def count(line):
        return line.count("\\") + line.count('"') + 2

    return sum(map(count, text.split()))


if __name__ == "__main__":
    text = get_input(2015, 8)

    print(part1(text))
    print(part2(text))
