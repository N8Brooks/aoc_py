#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/23
"""


from unittest import main, TestCase

from aoc.year2015.day24 import part1, part2
from data.utils import get_input


EXAMPLE = "1 2 3 4 5 7 8 9 10 11"


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 24)), 10439961859)

    def test_example(self):
        self.assertEqual(part1(EXAMPLE), 99)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 24)), 72050269)

    def test_example_a(self):
        self.assertEqual(part2(EXAMPLE), 44)


if __name__ == "__main__":  # pragma: no cover
    main()
