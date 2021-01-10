# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/1
"""


from unittest import main, TestCase

from aoc.year2016.day01 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2016, 1)), 161)

    def test_example_1(self):
        self.assertEqual(part1("R2, L3"), 5)

    def test_example_2(self):
        self.assertEqual(part1("R2, R2, R2"), 2)

    def test_example_3(self):
        self.assertEqual(part1("R5, L5, R5, R3"), 12)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2016, 1)), 110)

    def test_example_1(self):
        self.assertEqual(part2("R8, R4, R4, R8"), 4)


if __name__ == "__main__":  # pragma: no cover
    main()
