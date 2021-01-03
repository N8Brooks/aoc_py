#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/1
"""


from itertools import starmap, repeat
from more_itertools import last
import re
from operator import mul


def process(text, r=re.compile(r'([LR])(\d+)')):
    def turn(direction):
        return 1j if direction == 'L' else -1j
    
    turns, dists = zip(*(r.match(line).groups() for line in text.split(', ')))
    
    return accumulate(map(turn, turns), mul), map(int, dists)


def manhatten(location):
    return int(abs(location.imag) + abs(location.real))


def a(text):
    return manhatten(sum(map(mul, *process(text))))


def b(text):
    def visited(location):
        if location in previous:
            return True
        else:
            previous.add(location)
            return False
    
    previous = set()
    
    movements = chain.from_iterable(map(repeat, *process(text)))
    upcoming = accumulate(movements, initial=0)
    
    return manhatten(next(filter(visited, upcoming)))


if __name__ == '__main__':
    print(a(text))
    print(b(text))