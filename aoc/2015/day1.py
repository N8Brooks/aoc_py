#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Not Quite Lisp
"""


from itertools import accumulate


def a(text):
    return text.count('(') - text.count(')')


def b(text):
    def direction(char):
        return 1 if char == '(' else -1
    
    position_floor = enumerate(accumulate(map(direction, text)), start=1)
    
    return next(i for i, floor in position_floor if floor < 0)


if __name__ == '__main__':
    # TODO: better format for problem input
    text = '(((())))()((((((((())()(()))(()((((()(()(((()((()((()(()()()()()))'
    
    print(a(text))
    print(b(text))