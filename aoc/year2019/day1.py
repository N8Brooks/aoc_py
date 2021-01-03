#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2019/day/1
"""


from itertools import repeat, takewhile


def a(text):
    return sum(int(mass) // 3 - 2 for mass in text.split())


def b(text):
    def fuel(mass):
        fuels = (mass := mass // 3 - 2 for _ in repeat(None))
        return sum(takewhile(lambda mass: 0 < mass, fuels))
    
    return sum(map(fuel, map(int, text.split())))


if __name__ == '__main__':
    text = '1234534 13451 12341234 345634 1341'
    
    print(a(text))
    print(b(text))