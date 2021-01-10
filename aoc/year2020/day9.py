#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2020/day/9
"""


from collections import deque
from itertools import combinations, filterfalse, islice, repeat, starmap
from operator import add

from iteration_utilities import minmax

from data.utils import get_input


def missing(numbers, size):
    def present(num):
        contains = num in seen
        seen.extend(map(add, preamble, repeat(num)))
        preamble.append(num)
        return contains

    nums = iter(numbers)
    preamble = deque(islice(nums, size), maxlen=size)
    seen = deque(starmap(add, combinations(preamble, 2)), maxlen=size * size)

    return next(filterfalse(present, nums))


def part1(text, size=25):
    return missing(map(int, text.split()), size)


def part2(text, size=25):
    nums = tuple(map(int, text.split()))
    window = deque()
    total = 0
    target = missing(nums, size)

    for right in nums:
        total += right
        window.append(right)
        while target < total:
            total -= window.popleft()
        if total == target:
            return add(*minmax(window))


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2020, 9)

    print(part1(text))
    print(part2(text))
