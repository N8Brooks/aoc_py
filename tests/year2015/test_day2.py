# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/2
"""


from unittest import main, TestCase

from aoc.year2015.day2 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 2)), 1606483)

    def test_example_1(self):
        self.assertEqual(part1("2x3x4"), 58)

    def test_example_2(self):
        self.assertEqual(part1("1x1x10"), 43)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 2)), 3842356)

    def test_example_1(self):
        self.assertEqual(part2("2x3x4"), 34)

    def test_example_2(self):
        self.assertEqual(part2("1x1x10"), 14)


if __name__ == "__main__":  # pragma: no cover
    main()
