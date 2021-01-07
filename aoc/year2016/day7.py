#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/7
"""


from itertools import starmap

from more_itertools import windowed, flatten

from data.utils import get_input


def process(ip):
    def sort(part):
        *hyp, ext = part.split("]")
        return hyp, ext

    hyps, exts = zip(*map(sort, ip.split("[")))

    return flatten(hyps), exts


def part1(text):
    def abba(a, b, c, d):
        return a == d and b == c and a != b

    def abbas(ip):
        return any(starmap(abba, windowed(ip, 4)))

    def tls(hyps, exts):
        return not any(map(abbas, hyps)) and any(map(abbas, exts))

    return sum(starmap(tls, map(process, text.split())))


def part2(text):
    def aba(abc):
        return abc[0] == abc[2] and abc[0] != abc[1]

    def abas(ip):
        return filter(aba, windowed(ip, 3))

    def rev(a, b, _):
        return (b, a, b)

    def ssl(hyps, exts):
        inside = set(flatten(map(abas, hyps)))
        return not inside.isdisjoint(starmap(rev, flatten(map(abas, exts))))

    return sum(starmap(ssl, map(process, text.strip().split())))


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2016, 7)

    print(part1(text))
    print(part2(text))
