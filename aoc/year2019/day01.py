#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2019/day/1
"""


from itertools import repeat, takewhile


from data.utils import get_input


def part1(text):
    return sum(int(mass) // 3 - 2 for mass in text.split())


def part2(text):
    def fuel(mass):
        fuels = (mass := mass // 3 - 2 for _ in repeat(None))
        return sum(takewhile(lambda mass: 0 < mass, fuels))

    return sum(map(fuel, map(int, text.split())))


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2019, 1)

    print(part1(text))
    print(part2(text))
