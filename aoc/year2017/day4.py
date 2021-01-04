#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/4
"""


from itertools import combinations

from aoc.utils import get_input


def a(text):
    def valid(passphrase):
        words = passphrase.split()
        return len(set(words)) == len(words)

    return sum(map(valid, text.strip().split("\n")))


def b(text):
    def valid(passphrase):
        words = passphrase.split()
        return len(set(map(tuple, map(sorted, words)))) == len(words)

    return sum(map(valid, text.strip().split("\n")))


if __name__ == "__main__":
    text = get_input(2017, 4)

    print(a(text))
    print(b(text))
