#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/5
"""


from hashlib import md5
from itertools import count, islice

from data.utils import get_input


def hashes(text, start):
    def hash_i(i):
        hasher = prefix.copy()
        hasher.update(str(i).encode())
        return hasher.hexdigest()

    def valid(hash_i):
        return hash_i.startswith(start)

    prefix = md5(text.strip().encode())

    return filter(valid, map(hash_i, count()))


def part1(text, length=8, start="00000"):
    iterator = (hash_i[len(start)] for hash_i in hashes(text, start))
    return "".join(islice(iterator, 0, length))


def part2(text, length=8, start="00000"):
    def char(i):
        while password[i] is None:
            code = next(iterator)
            check = ord(code[index]) - 48
            if i <= check < length and password[check] is None:
                password[check] = code[index + 1]
        return password[i] or next()

    index = len(start)
    password = [None] * length
    iterator = hashes(text, start)

    return "".join(map(char, range(length)))


if __name__ == "__main__":
    text = get_input(2016, 5)

    print(part1(text))
    print(part2(text))
