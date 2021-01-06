# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/11
"""


from unittest import main, skip, TestCase

from aoc.year2015.day11 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 11)), "hxbxxyzz")

    def test_example_1(self):
        self.assertEqual(part1("abcdefgh"), "abcdffaa")

    def test_example_2(self):
        self.assertEqual(part1("ghijklmn"), "ghjaabcc")


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 11)), "hxcaabcc")


if __name__ == "__main__":
    main()
