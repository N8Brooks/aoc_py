# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/3
"""


from unittest import main, TestCase

from aoc.year2017.day3 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2017, 3)), 480)

    def test_example_1(self):
        self.assertEqual(part1(1), 0)

    def test_example_2(self):
        self.assertEqual(part1(12), 3)

    def test_example_3(self):
        self.assertEqual(part1(23), 2)

    def test_example_4(self):
        self.assertEqual(part1(1024), 31)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2017, 3)), 349975)

    def test_example_1(self):
        self.assertEqual(part2(0), 1)

    def test_example_2(self):
        self.assertEqual(part2(54), 57)

    def test_example_3(self):
        self.assertEqual(part2(800), 806)

    def test_example_4(self):
        self.assertEqual(part2(1000000), 1009457)


if __name__ == "__main__":  # pragma: no cover
    main()
