# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2018/day/1
"""


from unittest import main, TestCase

from aoc.year2018.day1 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2018, 1)), 599)

    def test_example_1(self):
        self.assertEqual(part1("+1 -2 +3 +1"), 3)

    def test_example_2(self):
        self.assertEqual(part1("+1 +1 +1"), 3)

    def test_example_3(self):
        self.assertEqual(part1("+1 +1 -2"), 0)

    def test_example_4(self):
        self.assertEqual(part1("-1 -2 -3"), -6)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2018, 1)), 81204)

    def test_example_1(self):
        self.assertEqual(part2("+1 -1"), 0)

    def test_example_2(self):
        self.assertEqual(part2("+3 +3 +4 -2 -4"), 10)

    def test_example_3(self):
        self.assertEqual(part2("-6 +3 +8 +5 -6"), 5)

    def test_example_4(self):
        self.assertEqual(part2("+7 +7 -2 -7 -4"), 14)


if __name__ == "__main__":
    main()
