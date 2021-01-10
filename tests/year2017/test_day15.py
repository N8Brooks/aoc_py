#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/15
"""


from unittest import main, skip, TestCase

from aoc.year2017.day15 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part1(get_input(2017, 15)), 626)

    @skip("Takes too long")
    def test_example(self):
        self.assertEqual(part1("65, 8921"), 626)

    def test_mock_1(self):
        self.assertEqual(part1("193, 1234", 7331, 8675309, 1000), 1)

    def test_mock_2(self):
        self.assertEqual(part1("12947, 1234", 7331, 8675309, 1000), 2)

    def test_mock_3(self):
        self.assertEqual(part1("642, 1234", 7331, 8675309, 10000), 3)


class TestPart2(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part2(get_input(2017, 13)), 306)

    @skip("Takes too long")
    def test_example(self):
        self.assertEqual(part2("65, 8921"), 309)

    def test_mock_1(self):
        self.assertEqual(part2("0, 1234", 7331, 8675309, 1000), 1)

    def test_mock_2(self):
        self.assertEqual(part2("649, 1234", 7331, 8675309, 1000), 2)

    def test_mock_3(self):
        self.assertEqual(part2("313, 1234", 7331, 8675309, 10000), 5)


if __name__ == "__main__":  # pragma: no cover
    main()
