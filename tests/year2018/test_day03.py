#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2018/day/2
"""


from unittest import main, skip, TestCase

from aoc.year2018.day03 import part1, part2
from data.utils import get_input


EXAMPLE_1 = "#123 @ 3,2: 5x4" ""

EXAMPLE_2 = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
"""


class TestPart1(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part1(get_input(2018, 3)), 121163)

    def test_example_1(self):
        self.assertEqual(part1(EXAMPLE_1), 0)

    def test_example_2(self):
        self.assertEqual(part1(EXAMPLE_2), 4)


class TestPart2(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part2(get_input(2018, 3)), 943)

    def test_example_1(self):
        self.assertEqual(part2(EXAMPLE_1), 123)

    def test_example_2(self):
        self.assertEqual(part2(EXAMPLE_2), 3)


if __name__ == "__main__":  # pragma: no cover
    main()
