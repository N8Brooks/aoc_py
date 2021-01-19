#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2019/day/6
"""


from unittest import main, TestCase

from aoc.year2019.day06 import part1, part2
from data.utils import get_input


EXAMPLE_1 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
"""

EXAMPLE_2 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2019, 6)), 186597)

    def test_example(self):
        self.assertEqual(part1(EXAMPLE_1), 42)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2019, 6)), 412)

    def test_example(self):
        self.assertEqual(part2(EXAMPLE_2), 4)


if __name__ == "__main__":  # pragma: no cover
    main()
