#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/3
"""


from itertools import accumulate, islice


DIRS = {'^':1j, '>':1, 'v':-1j, '<':-1}


def a(text):
    return len(set({0} | set(accumulate(map(DIRS.get, text)))))


def b(text):
    locations = {0}
    locations.update(accumulate(map(DIRS.get, islice(text, 0, None, 2))))
    locations.update(accumulate(map(DIRS.get, islice(text, 1, None, 2))))
    
    return len(locations)


if __name__ == '__main__':
    text = '^<<<>vv><><>v^><>^^^^vvvv'
    
    print(a(text))
    print(b(text))