#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/10
"""


from itertools import chain, cycle, islice
from functools import reduce
from operator import xor

from iteration_utilities import applyfunc, grouper, nth, packed

from data.utils import get_input


@packed
def process(array, lengths, first, skip):
    size = len(array)

    for length in lengths:
        iterable = chain(islice(array, length, None), reversed(array[:length]))
        array = tuple(islice(cycle(iterable), skip, skip + size))
        first -= skip + length
        skip = (skip + 1) % size

    return array, lengths, first, skip


def part1(text, size=256):
    lengths = map(int, text.split(","))
    array, _, first, _ = process((tuple(range(size)), lengths, 0, 0))

    return array[first % size] * array[(first + 1) % size]


def part2(text, size=256):
    lengths = tuple(chain(map(ord, text.strip()), (17, 31, 73, 47, 23)))
    args = (tuple(range(size)), lengths, 0, 0)

    array, _, first, _ = nth(63)(applyfunc(process, args))
    array = array[first % size :] + array[: first % size]

    return bytes(reduce(xor, group) for group in grouper(array, 16)).hex()


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2017, 10)

    print(part1(text))
    print(part2(text))
