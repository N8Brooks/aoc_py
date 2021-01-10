#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2020/day/3
"""


from functools import partial
from itertools import islice, starmap
from math import prod

from data.utils import get_input


SLOPES = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))


def trees(lines, right, down):
    def tree(i, line, width=len(lines[0])):
        return "#" == line[right * i % width]

    return sum(starmap(tree, enumerate(islice(lines, 0, None, down))))


def part1(text, right=3, down=1):
    return trees(text.strip().split("\n"), right, down)


def part2(text, slopes=SLOPES):
    return prod(starmap(partial(trees, text.strip().split("\n")), slopes))


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2020, 3)

    print(part1(text))
    print(part2(text))
