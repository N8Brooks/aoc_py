#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/7
"""


from collections import deque
from itertools import filterfalse


from aoc.utils import get_input


COMP = (1 << 16) - 1


def process(text):
    def cast(operand):
        return operand if operand.isalpha() else int(operand)

    def wrap(line):
        operands, dest = line.split(" -> ")
        return tuple(map(cast, operands.split())), dest

    return map(wrap, text.strip().split("\n"))


def compute(q, request):
    def val(operand):
        if isinstance(operand, str):
            return _reg.get(operand, None)
        else:
            return int(operand)

    def move(exp, dest):
        if (res := val(exp[0])) is None:
            q.append((exp, dest))
        else:
            _reg[dest] = res

    def complement(exp, dest):
        if (res := val(exp[1])) is None:
            q.append((exp, dest))
        else:
            _reg[dest] = COMP ^ res

    def instruct(exp, dest):
        if (res1 := val(exp[0])) is None or (res2 := val(exp[2])) is None:
            q.append((exp, dest))
            return
        if exp[1] == "AND":
            _reg[dest] = res1 & res2
        elif exp[1] == "OR":
            _reg[dest] = res1 | res2
        elif exp[1] == "LSHIFT":
            _reg[dest] = res1 << res2
        elif exp[1] == "RSHIFT":
            _reg[dest] = res1 >> res2

    def operate(exp, dest):
        if len(exp) == 1:
            move(exp, dest)
        elif len(exp) == 2:
            complement(exp, dest)
        else:
            instruct(exp, dest)

    _reg = {}

    while q:
        operate(*q.popleft())

    return _reg.get(request, None)


def part1(text, request="a"):
    return compute(deque(process(text)), request)


def part2(text, request="a"):
    q = deque(filter(lambda line: line[1] != "b", process(text)))
    q.appendleft(((part1(text, request),), "b"))

    return compute(q, request)


if __name__ == "__main__":
    text = get_input(2015, 7)

    print(part1(text))
    print(part2(text))
