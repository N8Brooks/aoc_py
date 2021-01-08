#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/13
"""


from heapq import heapify, heappop, heappush
from itertools import starmap
from math import log2, prod
from operator import mod

import numpy as np

from data.utils import get_input


def process(line):
    return map(int, line.split(": "))


def part1(text):
    def severity(depth, scope):
        return 0 if depth % (scope + scope - 2) else depth * scope

    return sum(starmap(severity, map(process, text.strip().split("\n"))))


def part2(text):
    quotients, scopes = zip(*map(process, text.strip().split("\n")))
    divisors = tuple(scope + scope - 2 for scope in scopes)

    if all(starmap(mod, zip(quotients, divisors))):
        return 0

    lo, hi = 0, 1
    heapify(queue := [((d - q) % d, d) for q, d in zip(quotients, divisors)])

    for _ in range(int(log2(prod(divisors))) + 1):
        delays = np.ones(lo, bool)
        while queue[0][0] < hi:
            mi, divisor = heappop(queue)
            delays[mi - lo : hi - lo : divisor] = False
            length = len(range(mi, hi, divisor))
            heappush(queue, (mi + divisor * length, divisor))

        if len(indices := np.argwhere(delays)):
            return lo + int(indices[0])

        lo, hi = hi, hi + hi


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2017, 13)

    print(part1(text))
    print(part2(text))
