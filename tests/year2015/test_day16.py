# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/16
"""


from unittest import main, TestCase

from aoc.year2015.day16 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 16)), 213)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 16)), 323)


if __name__ == "__main__":  # pragma: no cover
    main()
