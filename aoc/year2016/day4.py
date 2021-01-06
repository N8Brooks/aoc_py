#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/4
"""

from collections import Counter
from heapq import nsmallest
from itertools import repeat
import re

from aoc.utils import get_input


def process(text, r=re.compile(r"([a-z-]+)-(\d+)\[([a-z]+)\]")):
    def order(char):
        return ord(char) - 97 - 26 * counts[char]

    for room in text.split():
        name, section, proposed = r.match(room).groups()
        counts = Counter(name.replace("-", ""))
        checksum = "".join(nsmallest(5, counts, key=order))
        if checksum == proposed:
            yield int(section), name


def part1(text):
    return sum(next(zip(*process(text))))


def part2(text, target="northpole object storage"):
    def shift(word, n):
        return "".join(chr((ord(c) - 97 + n) % 26 + 97) for c in word)

    def valid(room):
        section, name = room
        translation = " ".join(map(shift, name.split("-"), repeat(section)))
        return translation == target

    return next(filter(valid, process(text)))[0]


if __name__ == "__main__":
    text = get_input(2016, 4)

    print(part1(text))
    print(part2(text))
