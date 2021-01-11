#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/22
"""


from unittest import main, skip, TestCase

from aoc.year2015.day22 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 22)), 1269)

    def test_example(self):
        self.assertEqual(part1("13 8", 10, 250), 226)


class TestPart2(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 22)), 1309)

    def test_mock(self):
        self.assertEqual(part2("10 8", 10, 250), 246)


if __name__ == "__main__":  # pragma: no cover
    main()
