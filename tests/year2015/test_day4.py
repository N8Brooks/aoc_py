# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/4
"""


from unittest import TestCase, main, skip

from aoc.year2015.day4 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    def test_input_a(self):
        self.assertEqual(part1(get_input(2015, 4)), 346386)

    def test_example_1(self):
        self.assertEqual(part1("abcdef"), 609043)

    def test_example_2(self):
        self.assertEqual(part1("pqrstuv"), 1048970)


class TestPart2(TestCase):
    def test_input_b(self):
        self.assertEqual(part2(get_input(2015, 4)), 9958218)


if __name__ == "__main__":
    main()
