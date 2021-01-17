#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/4
"""


from itertools import count
from hashlib import md5
import multiprocessing as mp
from sys import maxsize

from data.utils import get_input


POLL = 1024


def hasher(start, text, target, step=mp.cpu_count()):
    global result

    def valid(suffix):
        hashed = initial.copy()
        hashed.update(str(suffix).encode())
        is_valid = hashed.hexdigest().startswith(target)
        if suffix % poll == start:
            return result.value < suffix or is_valid
        else:
            return is_valid

    initial = md5(text.strip().encode())
    poll = POLL * step

    value = next(filter(valid, count(start, step)))
    with result.get_lock():
        result.value = min(result.value, value)

    return result.value


def process(text, prefix):
    global result

    result = mp.Value("l", maxsize)
    args = ((start, text, prefix) for start in range(mp.cpu_count()))

    with mp.Pool() as p:
        p.starmap(hasher, args)

    return result.value


def part1(text, prefix="00000"):
    return process(text, prefix)


def part2(text, prefix="000000"):
    return process(text, prefix)


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2015, 4)

    print(part1(text))
    print(part2(text))
