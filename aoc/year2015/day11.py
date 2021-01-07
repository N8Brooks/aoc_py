#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/11
"""


from itertools import starmap, repeat, accumulate

from more_itertools import pairwise, windowed

from data.utils import get_input


IOL = {8, 11, 14}


def part1(text):
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

    def straight(a, b, c):
        return a + 1 == b and b + 1 == c

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


def part2(text):
    return part1(part1(text))


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2015, 11)

    print(part1(text))
    print(part2(text))
