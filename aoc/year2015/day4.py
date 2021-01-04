#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/4
"""


from itertools import count
from hashlib import md5

from aoc.utils import get_input


def ab(text, start):
    def valid(suffix):
        hasher = prefix.copy()
        hasher.update(str(suffix).encode())
        hexadecimal = hasher.hexdigest()
        return hexadecimal.startswith(start)
    
    prefix = md5(text.strip().encode())
    
    return next(filter(valid, count()))


if __name__ == '__main__':
    text = get_input(2015, 4)
    
    print(ab(text, '00000'))
    print(ab(text, '000000'))