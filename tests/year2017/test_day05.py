#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/5
"""


from unittest import main, skip, TestCase

from aoc.year2017.day05 import part1, part2
from data.utils import get_input


EXAMPLE = "0 3 0 1 -3"

MOCK_1 = "1 2 -2 -3 0"

MOCK_2 = "2 3 -1 0 -4"

MOCK_3 = "0 -1 -2 1 0"


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2017, 5)), 325922)

    def test_example_1(self):
        self.assertEqual(part1(EXAMPLE), 5)

    def test_mock_1(self):
        self.assertEqual(part1(MOCK_1), 10)

    def test_mock_2(self):
        self.assertEqual(part1(MOCK_2), 9)

    def test_mock_3(self):
        self.assertEqual(part1(MOCK_3), 9)


class TestPart2(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part2(get_input(2017, 5)), 24490906)

    def test_example_1(self):
        self.assertEqual(part2(EXAMPLE), 10)

    def test_mock_1(self):
        self.assertEqual(part2(MOCK_1), 10)

    def test_mock_2(self):
        self.assertEqual(part2(MOCK_2), 10)

    def test_mock_3(self):
        self.assertEqual(part2(MOCK_3), 9)


if __name__ == "__main__":  # pragma: no cover
    main()
