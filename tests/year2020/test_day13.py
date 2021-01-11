#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2020/day/13
"""


from unittest import main, TestCase

from aoc.year2020.day13 import part1, part2
from data.utils import get_input


EXAMPLE_1 = """939
7,13,x,x,59,x,31,19
"""

EXAMPLE_2 = """1234
17,x,13,19
"""

EXAMPLE_3 = """1337
67,7,59,61
"""

EXAMPLE_4 = """7331
67,x,7,59,61
"""

EXAMPLE_5 = """448
67,7,x,59,61
"""

EXAMPLE_6 = """8901
1789,37,47,1889
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2020, 13)), 4722)

    def test_example_1(self):
        self.assertEqual(part1(EXAMPLE_1), 295)

    def test_example_2(self):
        self.assertEqual(part1(EXAMPLE_2), 13)

    def test_example_3(self):
        self.assertEqual(part1(EXAMPLE_3), 0)

    def test_example_4(self):
        self.assertEqual(part1(EXAMPLE_4), 35)

    def test_example_5(self):
        self.assertEqual(part1(EXAMPLE_5), 0)

    def test_example_6(self):
        self.assertEqual(part1(EXAMPLE_6), 592)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2020, 13)), 825305207525452)

    def test_example_1(self):
        self.assertEqual(part2(EXAMPLE_1), 1068781)

    def test_example_2(self):
        self.assertEqual(part2(EXAMPLE_2), 3417)

    def test_example_3(self):
        self.assertEqual(part2(EXAMPLE_3), 754018)

    def test_example_4(self):
        self.assertEqual(part2(EXAMPLE_4), 779210)

    def test_example_5(self):
        self.assertEqual(part2(EXAMPLE_5), 1261476)

    def test_example_6(self):
        self.assertEqual(part2(EXAMPLE_6), 1202161486)


if __name__ == "__main__":  # pragma: no cover
    main()
