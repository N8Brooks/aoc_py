#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2020/day/10
"""


from collections import deque
from itertools import chain, starmap

from iteration_utilities import successive, rsub

from data.utils import get_input


def part1(text):
    adapters = sorted(map(int, text.split()))
    padded = chain((0,), adapters, (adapters[-1] + 3,))
    diffs = tuple(starmap(rsub, successive(padded)))

    return diffs.count(1) * diffs.count(3)


def part2(text, size=25):
    adapters = sorted(map(int, text.split()))
    adapters.append(adapters[-1] + 3)
    memo = deque((0 + 1j,), maxlen=3)

    for jolts in adapters:
        while memo[0].real < jolts - 3:
            memo.popleft().imag
        memo.append(complex(jolts, sum(memo).imag))

    return int(memo[-1].imag)


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2020, 10)

    print(part1(text))
    print(part2(text))
