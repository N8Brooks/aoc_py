#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/24
"""


from math import prod

from iteration_utilities import powerset

from data.utils import get_input


def partition(text, k):
    def valid(nums):
        return target == sum(nums)

    nums = tuple(map(int, text.split()))
    target = sum(nums) // k

    return prod(next(filter(valid, powerset(nums))))


def part1(text, k=3):
    return partition(text, k)


def part2(text, k=4):
    return partition(text, k)


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2015, 24)

    print(part1(text))
    print(part2(text))
