#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2020/day/7
"""


from collections import defaultdict
from functools import cache
from itertools import repeat
import re

from iteration_utilities import Seen

from data.utils import get_input


R = re.compile(r"(\d+) (.+?) bags?[,.]")


def part1(text, target="shiny gold"):
    def parse(child):
        if contains.contains_add(child):
            return 0

        return sum(map(parse, parents[child])) + 1

    def golden(parent, child):
        parents[child].append(parent)
        if child in contains or child == target:
            return sum(map(parse, parents[child]))

        return 0

    def process(line):
        parent, _, children = line.partition(" bags contain ")
        return sum(map(golden, repeat(parent), r.findall(children)))

    r = re.compile(r"\d+ (.+?) bags?[,.]")

    parents = defaultdict(list)
    contains = Seen()

    return sum(map(process, text.splitlines()))


def part2(text, target="shiny gold"):
    @cache
    def parse(parent):
        return sum(v * (parse(k) + 1) for k, v in graph[parent].items())

    graph = {}
    for line in text.splitlines():
        parent, _, children = line.partition(" bags contain ")
        graph[parent] = {child: int(n) for n, child in R.findall(children)}

    return parse(target)


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2020, 7)

    print(part1(text))
    print(part2(text))
