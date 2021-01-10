#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/7
"""


from collections import deque

from iteration_utilities import is_None

from data.utils import get_input


COMP = (1 << 16) - 1


def process(text):
    def cast(operand):
        return operand if operand.isalpha() else int(operand)

    def wrap(line):
        operands, dest = line.split(" -> ")
        return tuple(map(cast, operands.split())), dest

    return map(wrap, text.splitlines())


def compute(q, request):
    def val(operand):
        if isinstance(operand, str):
            return reg.get(operand, None)
        else:
            return int(operand)

    def move(exp, dest):
        if is_None(res := val(exp[0])):
            q.append((exp, dest))
        else:
            reg[dest] = res

    def complement(exp, dest):
        if is_None(res := val(exp[1])):
            q.append((exp, dest))
        else:
            reg[dest] = COMP ^ res

    def instruct(exp, dest):
        if is_None(res1 := val(exp[0])) or is_None(res2 := val(exp[2])):
            q.append((exp, dest))
            return
        if exp[1] == "AND":
            reg[dest] = res1 & res2
        elif exp[1] == "OR":
            reg[dest] = res1 | res2
        elif exp[1] == "LSHIFT":
            reg[dest] = res1 << res2
        elif exp[1] == "RSHIFT":
            reg[dest] = res1 >> res2

    def operate(exp, dest):
        if len(exp) == 1:
            move(exp, dest)
        elif len(exp) == 2:
            complement(exp, dest)
        else:
            instruct(exp, dest)

    reg = {}

    while q:
        operate(*q.popleft())

    return reg.get(request, None)


def part1(text, request="a"):
    return compute(deque(process(text)), request)


def part2(text, request="a"):
    q = deque(filter(lambda line: line[1] != "b", process(text)))
    q.appendleft(((part1(text, request),), "b"))

    return compute(q, request)


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2015, 7)

    print(part1(text))
    print(part2(text))
