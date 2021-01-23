#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2020/day/8
"""


import re

from data.utils import get_input


def process(text):
    def match(line):
        op, arg = re.match(r"(\S+) ([+-]\d+)", line).groups()
        return op, int(arg)

    def acc(program_state, x):
        program_state["accumulator"] += x
        program_state["instruction"] += 1

    def nop(program_state, _):
        program_state["instruction"] += 1

    def jmp(program_state, x):
        program_state["instruction"] += x

    def run_until_loop(program):
        program_state = {
            "instruction": 0,
            "accumulator": 0,
            "done": False,
        }

        visited = set()
        while program_state["instruction"] not in visited and not program_state["done"]:
            instruction = program_state["instruction"]
            visited.add(instruction)

            op, arg = program[instruction]
            {"acc": acc, "nop": nop, "jmp": jmp}[op](program_state, arg)
            program_state["done"] = program_state["instruction"] >= len(program)

        return program_state

    def alternate_programs(program):
        swaps = {"jmp": "nop", "nop": "jmp"}
        for i, instruction in enumerate(program):
            op, arg = instruction
            if op in swaps:
                new_program = program.copy()
                new_program[i] = (swaps[op], arg)
                yield new_program

    program = list(map(match, text.splitlines()))

    return program, run_until_loop, alternate_programs


def part1(text):
    program, run_until_loop, _ = process(text)
    return run_until_loop(program)["accumulator"]


def part2(text):
    program, run_until_loop, alternate_programs = process(text)
    return next(
        program_state["accumulator"]
        for program_state in (run_until_loop(p) for p in alternate_programs(program))
        if program_state["done"]
    )


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2020, 8)

    print(part1(text))
    print(part2(text))
