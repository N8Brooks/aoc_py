#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/16
"""


import re

from data.utils import get_input


TARGET = {
    "children": "3",
    "cats": "7",
    "samoyeds": "2",
    "pomeranians": "3",
    "akitas": "0",
    "vizslas": "0",
    "goldfish": "5",
    "trees": "3",
    "cars": "2",
    "perfumes": "1",
}


def find_sue(text, validProp):
    def valid_sue(line):
        return all(map(validProp, r.sub("", line).split(", ")))

    r = re.compile(r"Sue (\d+): ")

    sue = next(filter(valid_sue, text.strip().split("\n")))

    return int(r.match(sue).groups()[0])


def part1(text):
    def valid_prop(record):
        key, value = record.split(": ")
        return TARGET[key] == value

    return find_sue(text, valid_prop)


def part2(text):
    def valid_prop(record):
        key, value = record.split(": ")
        if key in ["cats", "trees"]:
            return TARGET[key] < value
        elif key in ["pomeranians", "goldfish"]:
            return value < TARGET[key]

        return TARGET[key] == value

    return find_sue(text, valid_prop)


if __name__ == "__main__":
    text = get_input(2015, 16)

    print(part1(text))
    print(part2(text))
