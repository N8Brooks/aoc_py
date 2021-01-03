#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
I Was Told There Would Be No Math
"""


from itertools import starmap


def process(text):
    return tuple(sorted(map(int, line.split('x'))) for line in text.split())


def a(text):
    def paper(x, y, z):
        return 3 * x * y + 2 * (x * z + y * z)
    
    return sum(starmap(paper, process(text)))


def b(text):
    def ribbon(x, y, z):
        return x + x + y + y + x * y * z
    
    return sum(starmap(ribbon, process(text)))


if __name__ == '__main__':
    text = '3x4x5'
    
    print(a(text))
    print(b(text))