# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/3
"""


from unittest import main, TestCase

from aoc.year2015.day3 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 3)), 2081)

    def test_example_1(self):
        self.assertEqual(part1(">"), 2)

    def test_example_2(self):
        self.assertEqual(part1("^>v<"), 4)

    def test_example_3(self):
        self.assertEqual(part1("^v^v^v^v^v"), 2)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 3)), 2341)

    def test_example_1(self):
        self.assertEqual(part2("^v"), 3)

    def test_example_2(self):
        self.assertEqual(part2("^>v<"), 3)

    def test_example_3(self):
        self.assertEqual(part2("^v^v^v^v^v"), 11)


if __name__ == "__main__":  # pragma: no cover
    main()
