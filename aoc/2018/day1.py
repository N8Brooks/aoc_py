#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2018/day/1
"""


from itertools import accumulate, cycle


def a(text):
    return sum(map(int, text.split()))


def b(text):
    def visited(frequency):
        if frequency in previous:
            return True
        previous.add(frequency)
    
    previous = set()
    
    frequencies = accumulate(cycle(map(int, text.split())), initial=0)
    
    return next(filter(visited, frequencies))


if __name__ == '__main__':
    text = '+1\n+2\n+3\n+5\n-8\n+20\n'
    
    print(a(text))
    print(b(text))