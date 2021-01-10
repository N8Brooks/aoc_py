#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2020/day/4
"""


import re

from iteration_utilities import count_items

from data.utils import get_input


FIELDS = frozenset(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))

ECL = frozenset(("amb", "blu", "brn", "gry", "grn", "hzl", "oth"))


def part1(text):
    def valid(record):
        return FIELDS.issubset(field.split(":")[0] for field in record.split())

    return count_items(text.split("\n\n"), valid)


def part2(text):
    def starred(func):
        def wrapper(record):
            return func(**dict(field.split(":") for field in record.split()))

        return wrapper

    def height(hgt):
        if hgt.endswith("cm"):
            return 150 <= int(hgt.removesuffix("cm")) <= 193
        elif hgt.endswith("in"):
            return 59 <= int(hgt.removesuffix("in")) <= 76

    @starred
    def valid(byr=0, iyr=0, eyr=0, hgt="", hcl="", ecl="", pid="", **kwargs):
        if not 1920 <= int(byr) <= 2002:
            return False
        elif not 2010 <= int(iyr) <= 2020:
            return False
        elif not 2020 <= int(eyr) <= 2030:
            return False
        elif not height(hgt):
            return False
        elif not re.match(r"#[0-9a-f]{6}", hcl):
            return False
        elif not ecl in ECL:
            return False
        elif not len(pid) == 9 or not pid.isdecimal():
            return False

        return True

    return count_items(text.split("\n\n"), valid)


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2020, 4)

    print(part1(text))
    print(part2(text))
