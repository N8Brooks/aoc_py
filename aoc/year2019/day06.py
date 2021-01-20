#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2019/day/6
"""


from collections import defaultdict
from functools import partial
from itertools import takewhile
from operator import ne
import re

from iteration_utilities import applyfunc

from data.utils import get_input


R = re.compile(r"(\w+)\)(\w+)")


def part1(text, com="COM"):
    children = defaultdict(list)
    for line in text.splitlines():
        a, b = R.match(line).groups()
        children[a].append(b)

    stack = [(com, 0)]
    total = 0
    while stack:
        parent, level = stack.pop()
        total += level
        stack.extend((child, level + 1) for child in children[parent])

    return total


def part2(text, com="COM", you="YOU", san="SAN"):
    parents = {}
    for line in text.splitlines():
        a, b = R.match(line).groups()
        parents[b] = a

    path = takewhile(partial(ne, com), applyfunc(parents.get, you))
    visited = {you: i for i, you in enumerate(path)}

    path = applyfunc(parents.get, san)
    count, dest = next((i, san) for i, san in enumerate(path) if san in visited)

    return visited[dest] + count


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2019, 6)

    print(part1(text))
    print(part2(text))
