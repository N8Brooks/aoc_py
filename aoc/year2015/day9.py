#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/9
"""


from collections import defaultdict
from itertools import permutations
import re

from iteration_utilities import successive

from data.utils import get_input


def process(text):
    def distance(path):
        return sum(dist[a][b] for a, b in successive(path))

    r = re.compile(r"(\w+) to (\w+) = (\d+)")

    dist = defaultdict(dict)

    for line in text.strip().split("\n"):
        a, b, d = r.match(line).groups()
        dist[a][b] = dist[b][a] = int(d)

    return map(distance, permutations(dist))


def part1(text):
    return min(process(text))


def part2(text):
    return max(process(text))


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2015, 9)

    print(part1(text))
    print(part2(text))
