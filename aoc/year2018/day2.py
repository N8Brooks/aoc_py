#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2018/day/2
"""


from collections import Counter

from iteration_utilities import Seen

from data.utils import get_input


def part1(text):
    def checksum(line):
        frequencies = set(Counter(line).values())
        return complex(2 in frequencies, 3 in frequencies)

    total = sum(map(checksum, text.strip().splitlines()))
    return int(total.imag * total.real)


def part2(text):
    lines = text.strip().split()
    length = len(lines[0])
    commons = [Seen() for _ in range(length)]

    for line in lines:
        for i, common in enumerate(commons):
            string = f"{line[:i]}{line[i + 1:]}"
            if common.contains_add(string):
                return string


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2018, 2)

    print(part1(text))
    print(part2(text))
