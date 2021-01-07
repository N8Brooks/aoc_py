#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/6
"""


from functools import partial
from itertools import chain, islice, repeat, takewhile
from operator import add, ne

from iteration_utilities import applyfunc, argmax, last
from more_itertools import ilen

from data.utils import get_input


def process(text):
    def spread(start, stop, inside, outside):
        yield from repeat(outside, start)
        yield from repeat(inside, stop - start)
        yield from repeat(outside, n - stop)

    def redistribute(previous):
        i = argmax(previous)
        div, mod = divmod(previous[i], n)

        chained = chain(islice(previous, i), (0,), islice(previous, i + 1, n))
        if (a := i + mod + 1) == (b := a % n):
            memory = tuple(map(add, chained, spread(i + 1, a, div + 1, div)))
        else:
            memory = tuple(map(add, chained, spread(b, i + 1, div, div + 1)))

        return visited.setdefault(previous, memory)

    def duplicated(memory):
        return memory not in visited

    visited = {}
    n = len(memory := tuple(map(int, text.split())))
    final = last(takewhile(duplicated, applyfunc(redistribute, memory)))

    return visited, final


def part1(text):
    return len(process(text)[0])


def part2(text):
    graph, node = process(text)
    unique = partial(ne, node)
    return ilen(takewhile(unique, applyfunc(graph.get, node))) + 1


if __name__ == "__main__":  # pragma: no cover  # pragma: no cover
    text = get_input(2017, 6)

    print(part1(text))
    print(part2(text))
