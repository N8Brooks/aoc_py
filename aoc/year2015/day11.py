#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/11
"""


from itertools import accumulate, starmap, repeat
from operator import eq

from iteration_utilities import (
    count_items,
    starfilter,
    successive,
    unique_everseen,
)

from data.utils import get_input


IOL = {8, 11, 14}


def part1(text):
    def next_pass(password, _=None):
        for i, x in zip(reversed(range(n)), reversed(password)):
            if (x := x + 1) in IOL:
                password[i] = x + 1
                password[i + 1 :] = repeat(0, n - i - 1)
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

        if not any(starmap(straight, successive(string, 3))):
            return False

        pairs = unique_everseen(starfilter(eq, successive(string)))

        return 1 < count_items(pairs)

    n = len(processed := text.strip())

    password = next_pass(list(i - 97 for i in map(ord, processed)))

    passwords = accumulate(repeat(None), func=next_pass, initial=password)

    return "".join(chr(i + 97) for i in next(filter(valid, passwords)))


def part2(text):
    # Call part1 redundantly
    return part1(part1(text))


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2015, 11)

    print(part1(text))
    print(part2(text))
