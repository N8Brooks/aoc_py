# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/21
"""


from unittest import main, TestCase

from aoc.year2015.day21 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 21)), 111)

    def test_example(self):
        self.assertEqual(part1("12 7 2", 8), 65)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 21)), 188)

    def test_mock(self):
        self.assertEqual(part2("6 7 2", 8), 88)


if __name__ == "__main__":
    main()
