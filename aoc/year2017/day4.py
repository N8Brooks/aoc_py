#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/4
"""


from itertools import combinations

from data.utils import get_input


def part1(text):
    def valid(passphrase):
        words = passphrase.split()
        return len(set(words)) == len(words)

    return sum(map(valid, text.strip().split("\n")))


def part2(text):
    def valid(passphrase):
        words = passphrase.split()
        return len(set(map(tuple, map(sorted, words)))) == len(words)

    return sum(map(valid, text.strip().split("\n")))


if __name__ == "__main__":
    text = get_input(2017, 4)

    print(part1(text))
    print(part2(text))
