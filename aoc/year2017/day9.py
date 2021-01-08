#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/9
"""


from data.utils import get_input


def part1(text):
    def garbage(i):
        while (char := text[i]) != ">":
            i += (char == "!") + 1
        return i

    depth = count = i = 0
    length = len(text)

    while i < length:
        if (char := text[i]) == "<":
            i = garbage(i + 1)
        elif char == "{":
            depth += 1
            count += depth
        elif char == "}":
            depth -= 1
        i += 1

    return count


def part2(text):
    count = i = 0
    length = len(text)

    while i < length:
        if text[i] != "<":
            i += 1
            continue

        i += 1
        while (char := text[i]) != ">":
            if char == "!":
                i += 2
            else:
                count += 1
                i += 1
        i += 1

    return count


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2017, 9)

    print(part1(text))
    print(part2(text))
