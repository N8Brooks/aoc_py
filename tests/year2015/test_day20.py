# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/20
"""


from unittest import main, skip, TestCase

from aoc.year2015.day20 import part1, part2
from aoc.utils import get_input


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 20)), 776160)

    def test_example_1(self):
        self.assertEqual(part1(10), 1)

    def test_example_2(self):
        self.assertEqual(part1(70), 4)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 20)), 786240)

    def test_example_1(self):
        self.assertEqual(part2(10), 1)

    def test_example_2(self):
        self.assertEqual(part2(70), 4)


if __name__ == "__main__":
    main()
