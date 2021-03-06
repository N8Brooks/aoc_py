#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/17
"""


from collections import Counter
from functools import reduce
from itertools import combinations

from iteration_utilities import count_items

from data.utils import get_input


def part1(text, target=150):
    def update(freq, b):
        freq += {a + b: count for a, count in freq.items() if a + b <= target}
        return freq

    return reduce(update, map(int, text.split()), Counter((0,))).get(target, 0)


def part2(text, target=150):
    def target_sum(combo):
        return sum(combo) == target

    def valid_combo(k):
        return count_items(combinations(nums, k), target_sum)

    nums = tuple(map(int, text.split()))

    return next(filter(bool, map(valid_combo, range(len(nums)))))


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2015, 17)

    print(part1(text))
    print(part2(text))
