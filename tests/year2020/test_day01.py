# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2020/day/1
"""


from unittest import main, TestCase

from aoc.year2020.day01 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2020, 1)), 482811)

    def test_example(self):
        self.assertEqual(part1("1721 979 366 299 675 1456"), 514579)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2020, 1)), 193171814)

    def test_example(self):
        self.assertEqual(part2("1721 979 366 299 675 1456"), 241861950)


if __name__ == "__main__":  # pragma: no cover
    main()
