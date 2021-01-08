#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/7
"""


from itertools import chain
import re
from statistics import mode

from iteration_utilities import all_equal, empty

from data.utils import get_input


def unique(iterable):
    one = set()
    two = set()

    for element in iterable:
        if element in one:
            one.remove(element)
            two.add(element)
        elif element not in two:
            one.add(element)

    return one.pop()


def part1(text):
    return unique(re.findall(r"[a-z]+", text))


def part2(text):
    def scale(parent):
        weights[parent] += sum(map(scale, graph[parent]))
        return weights[parent]

    def deepflatten(node):
        yield node
        yield from chain(*map(deepflatten, graph[node]))

    r = re.compile(r"([a-z]+) \((\d+)\)(?: -> (.*))?")

    weights = {}
    graph = {}

    for line in text.strip().split("\n"):
        parent, weight, kids = r.match(line).groups()
        graph[parent] = empty if kids is None else kids.split(", ")
        weights[parent] = int(weight)

    scale(head := unique(chain.from_iterable(map(deepflatten, graph))))
    sibs = kids = dict((kid, weights[kid]) for kid in graph[head])

    while not all_equal(kids.values()):
        odd = unique(kids.values())
        head = next(kid for kid, weight in kids.items() if weight == odd)
        sibs, kids = kids, dict((kid, weights[kid]) for kid in graph[head])

    return mode(sibs.values()) - len(kids) * next(iter(kids.values()))


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2017, 7)

    print(part1(text))
    print(part2(text))
