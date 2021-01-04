#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/11
"""


from itertools import starmap, repeat, accumulate

from more_itertools import pairwise, windowed

from aoc.utils import get_input


# TODO: make this more efficient


def a(text):
    def next_char(char):
        return chr((ord(char) - 96) % 26 + 97)

    def next_pass(password, _):
        data = list(password)

        for i in range(len(data) - 1, -1, -1):
            data[i] = chr((ord(data[i]) - ord("a") + 1) % 26 + ord("a"))
            if data[i] != "a":
                break
        return "".join(data)

    def straight(x, y, z):
        return ord(x) + 1 == ord(y) and ord(y) + 1 == ord(z)

    def valid(string):
        if "i" in string or "o" in string or "l" in string:
            return False

        if not any(starmap(straight, windowed(string, 3))):
            return False

        return 1 < len(set((a, b) for a, b in pairwise(string) if a == b))

    passwords = accumulate(repeat(None), func=next_pass, initial=text.strip())
    next(passwords)

    return "".join(next(filter(valid, passwords)))


def b(text):
    return a(a(text))


if __name__ == "__main__":
    text = get_input(2015, 11)

    print(a(text))
    print(b(text))
