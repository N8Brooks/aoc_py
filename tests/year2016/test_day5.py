# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/5
"""


from unittest import main, skip, TestCase

from aoc.year2016.day5 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part1(get_input(2016, 5)), "c6697b55")

    @skip("Takes too long")
    def test_example(self):
        self.assertEqual(part1("abc"), "18f47a30")

    def test_mock_1(self):
        self.assertEqual(part1("abc", 4, "0"), "890c")

    def test_mock_2(self):
        self.assertEqual(part1("xyz", 2, "00"), "ee")


class TestPart2(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part2(get_input(2016, 5)), "8c35d1ab")

    @skip("Takes too long")
    def test_example(self):
        self.assertEqual(part2("abc"), "05ace8e3")

    def test_mock_1(self):
        self.assertEqual(part2("abc", 4, "0"), "3010")

    def test_mock_2(self):
        self.assertEqual(part2("xyz", 2, "00"), "cd")


if __name__ == "__main__":
    main()
