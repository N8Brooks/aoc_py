#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/8
"""


from functools import reduce
from hashlib import md5
import re

import numpy as np

from data.utils import get_input


LETTERS = {
    "d1341a6c3de6f371f55d405d0923e0b5": "R",
    "ad5e32088fad27de2c9ae96dc0bd3a92": "U",
    "3f2b97524545f26af3c9691856f0a8f3": "C",
    "ccd9eca0d779bee954011dcfc2f81fe4": "E",
    "059e58cae07e213b52a81a789d68b4e6": "O",
    "741783a1beb359d1a1c6ba1915c18687": "I",
    "d7fc7891de540067cc50d06ef7611962": "L",
}


def process(text, shape):
    def act(_, command):
        kwargs = r.match(command)
        if kwargs["R"] == "rect":
            screen[: int(kwargs["B"]), : int(kwargs["A"])] = True
        elif kwargs["V"] == "column x":
            replace = np.roll(screen[:, int(kwargs["C"])], int(kwargs["D"]))
            screen[:, int(kwargs["C"])] = replace
        else:
            replace = np.roll(screen[int(kwargs["C"]), :], int(kwargs["D"]))
            screen[int(kwargs["C"]), :] = replace
        return screen

    r = re.compile(
        (
            r"(?P<R>rotate|rect) (?:(?P<A>\d+)x(?P<B>\d+))"
            r"?(?:(?P<V>column x|row y)=(?P<C>\d+) by (?P<D>\d+))?"
        )
    )

    screen = np.zeros(shape, bool)

    return reduce(act, text.strip().split("\n"), shape)


def part1(text, shape=(6, 50)):
    return int(process(text, shape).sum())


def part2(text, shape=(6, 50)):
    def hasher(matrix):
        return md5(str(matrix).encode()).hexdigest()

    screen = process(text, shape)
    hashes = map(hasher, np.hsplit(screen, screen.shape[1] // 5))
    return "".join(map(LETTERS.get, hashes))


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2016, 8)

    print(part1(text))
    print(part2(text))
