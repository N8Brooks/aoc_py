#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/14
"""


from itertools import accumulate, chain, cycle, islice, repeat, starmap
import re
from statistics import mode

from aoc.utils import get_input


R = re.compile(
    (
        r"(?:\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."
    )
)


def process(text):
    def stats(line):
        return tuple(map(int, R.match(line).groups()))

    return tuple(map(stats, text.strip().split("\n")))


def part1(text, total=2503):
    def distance(speed, flying, resting):
        cycles, extra = divmod(total, flying + resting)
        result = speed * (flying * cycles + min(flying, extra))
        return result

    return max(starmap(distance, process(text)))


def part2(text, total=2503):
    def distances(speed, flying, resting):
        iterable = chain(repeat(speed, flying), repeat(0, resting))
        yield from accumulate(cycle(iterable))

    def imax(dists):
        return dists.index(max(dists))

    iterable = zip(*starmap(distances, process(text)))
    counts = tuple(map(imax, islice(iterable, total)))

    return counts.count(mode(counts))


if __name__ == "__main__":
    text = get_input(2015, 14)

    print(part1(text))
    print(part2(text))
