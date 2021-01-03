#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/1
"""


def a(text):
    def match(i):
        return text[i] == text[i - 1]
    
    return sum(int(text[i]) for i in filter(match, range(len(text))))


def b(text):
    def match(i, halfway=len(text) // 2):
        return text[i] == text[i - halfway]
    
    return sum(int(text[i]) for i in filter(match, range(len(text))))


if __name__ == '__main__':
    text = '1235138945710892345701892345701892352223899'
    
    print(a(text))
    print(b(text))