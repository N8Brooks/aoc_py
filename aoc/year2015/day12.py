#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/12
"""


from json import loads

from aoc.utils import get_input


def a(text):
    def parse(node):
        if isinstance(node, int):
            return node
        elif isinstance(node, list):
            return sum(map(parse, node))
        elif isinstance(node, dict):
            return sum(map(parse, node.values()))
        else:
            return 0

    return parse(loads(text))


def b(text):
    def parse(node):
        if isinstance(node, int):
            return node
        elif isinstance(node, list):
            return sum(map(parse, node))
        elif isinstance(node, dict):
            if "red" in node.values():
                return 0
            else:
                return sum(map(parse, node.values()))
        else:
            return 0

    return parse(loads(text))


if __name__ == "__main__":
    text = get_input(2015, 12)

    print(a(text))
    print(b(text))