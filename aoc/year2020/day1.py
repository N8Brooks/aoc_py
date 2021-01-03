#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2020/day/1
"""


from operator import mul


from aoc.utils import get_input


def a(text, total):
    def add(entry):
        if total - entry in entries:
            return True
        entries.add(entry)
    
    def fix(entry):
        return (total - entry) * entry
    
    entries = set()
    
    return fix(next(filter(add, map(int, text.split()))))


def b(text, total):
    def add(entry):
        if total - entry in twos:
            return True
        twos.update((entry+other, (entry,other)) for other in ones)
        ones.add(entry)
    
    def fix(entry):
        return mul(*twos[total - entry]) * entry
    
    ones = set()
    twos = {}
    
    return fix(next(filter(add, map(int, text.split()))))


if __name__ == '__main__':
    text = get_input(2020, 1)
    
    print(a(text, 2020))
    print(b(text, 2020))