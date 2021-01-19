#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2019/day/4
"""


from unittest import main, skip, TestCase

from aoc.year2019.day04 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part1(get_input(2019, 4)), 495)

    def test_example_1(self):
        self.assertEqual(part1("111111-111111"), 1)

    def test_example_2(self):
        self.assertEqual(part1("223450-223450"), 0)

    def test_example_3(self):
        self.assertEqual(part1("123789-123789"), 0)


class TestPart2(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part2(get_input(2019, 4)), 305)

    def test_example_1(self):
        self.assertEqual(part2("112233-112233"), 1)

    def test_example_2(self):
        self.assertEqual(part2("123444-123444"), 0)

    def test_example_3(self):
        self.assertEqual(part2("111122-111122"), 1)


if __name__ == "__main__":  # pragma: no cover
    main()
