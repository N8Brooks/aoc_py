#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2020/day/6
"""


from itertools import chain

from data.utils import get_input


def part1(text):
    def any_yes(group):
        return len(set(chain.from_iterable(group.split())))
    
    return sum(map(any_yes, text.split('\n\n')))


def part2(text):
    def all_yes(group):
        return len(set.intersection(*map(set, group.split())))
    
    return sum(map(all_yes, text.split('\n\n')))


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2020, 6)

    print(part1(text))
    print(part2(text))
