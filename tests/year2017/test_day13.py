#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/13
"""


from unittest import main, TestCase

from aoc.year2017.day13 import part1, part2
from data.utils import get_input


EXAMPLE = """0: 3
1: 2
4: 4
6: 4
"""
MOCK = """1: 2
4: 4
7: 4
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2017, 13)), 2604)

    def test_example(self):
        self.assertEqual(part1(EXAMPLE), 24)

    def test_mock(self):
        self.assertEqual(part1(MOCK), 0)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2017, 13)), 3941460)

    def test_example(self):
        self.assertEqual(part2(EXAMPLE), 10)

    def test_mock(self):
        self.assertEqual(part2(MOCK), 0)


if __name__ == "__main__":  # pragma: no cover
    main()
