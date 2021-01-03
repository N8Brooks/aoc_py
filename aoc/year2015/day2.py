#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/2
"""


from itertools import starmap


from aoc.utils import get_input


def process(text):
    return (sorted(map(int, line.split('x'))) for line in text.split())


def a(text):
    def paper(x, y, z):
        return 3 * x * y + 2 * (x * z + y * z)
    
    return sum(starmap(paper, process(text)))


def b(text):
    def ribbon(x, y, z):
        return x + x + y + y + x * y * z
    
    return sum(starmap(ribbon, process(text)))


if __name__ == '__main__':
    text = get_input(2015, 2)
    
    print(a(text))
    print(b(text))