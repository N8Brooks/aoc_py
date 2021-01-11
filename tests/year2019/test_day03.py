#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2019/day/3
"""


from unittest import main, TestCase

from aoc.year2019.day03 import part1, part2
from data.utils import get_input


EXAMPLE_1 = """
R8,U5,L5,D3
U7,R6,D4,L4
"""

EXAMPLE_2 = """
R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83
"""

EXAMPLE_3 = """
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2019, 3)), 1674)

    def test_example_1(self):
        self.assertEqual(part1(EXAMPLE_1), 6)

    def test_example_2(self):
        self.assertEqual(part1(EXAMPLE_2), 159)

    def test_example_3(self):
        self.assertEqual(part1(EXAMPLE_3), 135)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2019, 3)), 14012)

    def test_example_1(self):
        self.assertEqual(part2(EXAMPLE_1), 30)

    def test_example_2(self):
        self.assertEqual(part2(EXAMPLE_2), 610)

    def test_example_3(self):
        self.assertEqual(part2(EXAMPLE_3), 410)


if __name__ == "__main__":  # pragma: no cover
    main()
