# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/19
"""


from unittest import main, TestCase

from aoc.year2015.day19 import part1, part2
from data.utils import get_input


EXAMPLE_1 = """
H => HO
H => OH
O => HH

HOH
"""

EXAMPLE_2 = """
e => H
e => O
H => HO
H => OH
O => HH

HOH
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 19)), 576)

    def test_example_1(self):
        self.assertEqual(part1(EXAMPLE_1), 4)

    def test_example_2(self):
        self.assertEqual(part1(EXAMPLE_2), 4)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 19)), 207)

    def test_example_1(self):
        self.assertEqual(part2(EXAMPLE_1, "O"), 2)

    def test_example_2(self):
        self.assertEqual(part2(EXAMPLE_2), 3)


if __name__ == "__main__":  # pragma: no cover
    main()
