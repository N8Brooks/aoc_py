#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/10
"""


from unittest import main, TestCase

from aoc.year2017.day10 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2017, 10)), 4480)

    def test_example(self):
        self.assertEqual(part1("3,4,1,5", 5), 12)


class TestPart2(TestCase):
    def test_input(self):
        expected = "c500ffe015c83b60fad2e4b7d59dabc4"
        self.assertEqual(part2(get_input(2017, 10)), expected)

    def test_example_1(self):
        self.assertEqual(part2("3,4,1,5", 5), "04")

    def test_example_2(self):
        expected = "a2582a3a0e66e6e86e3812dcb672a272"
        self.assertEqual(part2(""), expected)

    def test_example_3(self):
        expected = "33efeb34ea91902bb2f59c9920caa6cd"
        self.assertEqual(part2("AoC 2017"), expected)

    def test_example_4(self):
        expected = "3efbe78a8d82f29979031a4aa0b16a9d"
        self.assertEqual(part2("1,2,3"), expected)

    def test_example_5(self):
        expected = "63960835bcdc130f0b66d7ff4f6a5a8e"
        self.assertEqual(part2("1,2,4"), expected)


if __name__ == "__main__":  # pragma: no cover
    main()
