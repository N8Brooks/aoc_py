# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/6
"""


from unittest import main, skip, TestCase

from aoc.year2017.day6 import part1, part2
from data.utils import get_input


EXAMPLE = "0 2 7 0"

MOCK_1 = "0 5 8 3 9"

MOCK_2 = "9 2 8 7 4 3 0 8 2"

MOCK_3 = "1 9 0 0 100 0"


class TestPart1(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part1(get_input(2017, 6)), 12841)

    def test_example_1(self):
        self.assertEqual(part1(EXAMPLE), 5)

    def test_mock_1(self):
        self.assertEqual(part1(MOCK_1), 15)

    def test_mock_2(self):
        self.assertEqual(part1(MOCK_2), 13)

    def test_mock_3(self):
        self.assertEqual(part1(MOCK_3), 18)


class TestPart2(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part2(get_input(2017, 6)), 8038)

    def test_example_1(self):
        self.assertEqual(part2(EXAMPLE), 4)

    def test_mock_1(self):
        self.assertEqual(part2(MOCK_1), 5)

    def test_mock_2(self):
        self.assertEqual(part2(MOCK_2), 9)

    def test_mock_3(self):
        self.assertEqual(part2(MOCK_3), 6)


if __name__ == "__main__":
    main()
