#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/11
"""


from itertools import starmap, repeat, accumulate

from more_itertools import pairwise, windowed

from aoc.utils import get_input


IOL = {8, 11, 14}


def a(text):
    def next_pass(password, _=None):
        for i, x in zip(reversed(range(_n)), reversed(password)):
            if (x := x + 1) in IOL:
                password[i] = x + 1
                password[i + 1 :] = repeat(0, _n - i - 1)
            if x == 26:
                password[i] = 0
            else:
                password[i] = x
                break
        return password

    def straight(x, y, z):
        return x + 1 == y and y + 1 == z

    def valid(string):
        if 8 in string or 11 in string or 14 in string:
            return False

        if not any(starmap(straight, windowed(string, 3))):
            return False

        return 1 < len(set((a, b) for a, b in pairwise(string) if a == b))

    _n = len(processed := text.strip())

    password = next_pass(list(i - 97 for i in map(ord, processed)))

    passwords = accumulate(repeat(None), func=next_pass, initial=password)

    return "".join(chr(i + 97) for i in next(filter(valid, passwords)))


def b(text):
    return a(a(text))


if __name__ == "__main__":
    text = get_input(2015, 11)

    print(a(text))
    print(b(text))
