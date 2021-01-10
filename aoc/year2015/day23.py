#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/23
"""


from functools import partial
from itertools import takewhile
from operator import gt

from iteration_utilities import applyfunc, consume

from data.utils import get_input


def compute(text, a, b, target):
    def process(line):
        instruction, *operands = line.replace(",", "").split()
        if instruction == "jmp":
            return instruction, None, int(operands[0]) - 1
        elif len(operands) == 1:
            return instruction, operands[0], None
        else:
            return instruction, operands[0], int(operands[1]) - 1

    def execute(pointer):
        instruction, register, offset = program[pointer]

        if instruction == "hlf":
            registers[register] //= 2
        elif instruction == "tpl":
            registers[register] *= 3
        elif instruction == "inc":
            registers[register] += 1
        elif instruction == "jmp":
            pointer += offset
        elif instruction == "jie" and registers[register] % 2 == 0:
            pointer += offset
        elif instruction == "jio" and registers[register] == 1:
            pointer += offset

        return pointer + 1

    registers = {"a": a, "b": b}
    program = tuple(map(process, text.strip().splitlines()))

    consume(takewhile(partial(gt, len(program)), applyfunc(execute, 0)), None)

    return registers[target]


def part1(text, a=0, b=0, target="b"):
    return compute(text, a, b, target)


def part2(text, a=1, b=0, target="b"):
    return compute(text, a, b, target)


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2015, 23)

    print(part1(text))
    print(part2(text))
