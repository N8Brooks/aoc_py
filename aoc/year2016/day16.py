#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/16
"""


from iteration_utilities import applyfunc, grouper

from data.utils import get_input


def process(text, length):
    def dragon(data, translation=str.maketrans({"0": "1", "1": "0"})):
        return f"{data}0{data[::-1].translate(translation)}"

    def valid(data):
        return length <= len(data)

    def checksum(data):
        return "".join("1" if a == b else "0" for a, b in grouper(data, 2))

    data = next(filter(valid, applyfunc(dragon, text.strip())))[:length]

    return next(filter(lambda data: len(data) % 2, applyfunc(checksum, data)))


def part1(text, length=272):
    return process(text, length)


def part2(text, length=35651584):
    return process(text, length)


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2016, 16)

    print(part1(text))
    print(part2(text))
