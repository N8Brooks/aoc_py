# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2020/day/4
"""


from unittest import main, TestCase

from aoc.year2020.day5 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2020, 5)), 953)

    def test_example_1(self):
        self.assertEqual(part1("FBFBBFFRLR"), 357)

    def test_example_2(self):
        self.assertEqual(part1("BFFFBBFRRR"), 567)

    def test_example_3(self):
        self.assertEqual(part1("FFFBBBFRRR"), 119)

    def test_example_4(self):
        self.assertEqual(part1("BBFFBBFRLL"), 820)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2020, 5)), 615)


if __name__ == "__main__":  # pragma: no cover
    main()
