#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/6
"""


from unittest import TestCase, main

from aoc.year2015.day06 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 6)), 543903)

    def test_example_1(self):
        self.assertEqual(part1("turn on 0,0 through 999,999"), 1000000)

    def test_example_2(self):
        self.assertEqual(part1("toggle 0,0 through 999,0"), 1000)

    def test_example_3(self):
        self.assertEqual(part1("turn off 499,499 through 500,500"), 0)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 6), 1000), 14687245)

    def test_example_1(self):
        self.assertEqual(part2("turn on 0,0 through 0,0"), 1)

    def test_example_2(self):
        self.assertEqual(part2("toggle 0,0 through 999,999"), 2000000)


if __name__ == "__main__":  # pragma: no cover
    main()
