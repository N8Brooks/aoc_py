#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/4
"""


from iteration_utilities import all_distinct

from data.utils import get_input


def part1(text):
    def valid(passphrase):
        return all_distinct(passphrase.split())

    return sum(map(valid, text.strip().splitlines()))


def part2(text):
    def valid(passphrase):
        return all_distinct(map(sorted, passphrase.split()))

    return sum(map(valid, text.strip().splitlines()))


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2017, 4)

    print(part1(text))
    print(part2(text))
