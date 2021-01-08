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
        if (char := text[i]) == "!":
            i += 1
        elif char == "<":
            i = garbage(i + 1)
        elif char == "{":
            depth += 1
            count += depth
        elif char == "}":
            depth -= 1
        i += 1

    return count


def part2(text):
    def garbage(i):
        nonlocal count
        while (char := text[i]) != ">":
            if char == "!":
                i += 1
            else:
                count += 1
            i += 1
        return i

    count = i = 0
    length = len(text)

    while i < length:
        if (char := text[i]) == "!":
            i += 1
        elif char == "<":
            i = garbage(i + 1)
        elif char == "{" or char == "}":
            pass
        i += 1

    return count


if __name__ == "__main__":  # pragma: no cover
    text = get_input(2017, 9)

    print(part1(text))
    print(part2(text))
