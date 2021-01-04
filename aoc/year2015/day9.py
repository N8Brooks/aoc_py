#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/9
"""


from collections import defaultdict
from itertools import permutations
import re

from more_itertools import consume, pairwise

from aoc.utils import get_input


def process(text):
    def distance(path):
        return sum(dist[a][b] for a, b in pairwise(path))

    def unpack(line):
        a, b, d = r.match(line).groups()
        dist[a][b] = dist[b][a] = int(d)

    r = re.compile(r"(\w+) to (\w+) = (\d+)")

    dist = defaultdict(dict)

    consume(map(unpack, text.strip().split("\n")))

    return map(distance, permutations(dist))


def a(text):
    return min(process(text))


def b(text):
    return max(process(text))


if __name__ == "__main__":
    text = get_input(2015, 9)

    print(a(text))
    print(b(text))
