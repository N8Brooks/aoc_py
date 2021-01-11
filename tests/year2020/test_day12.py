#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2020/day/12
"""


from unittest import main, TestCase

from aoc.year2020.day12 import part1, part2
from data.utils import get_input


EXAMPLE = """F10
N3
F7
R90
F11
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2020, 12)), 2847)

    def test_example(self):
        self.assertEqual(part1(EXAMPLE), 25)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2020, 12)), 29839)

    def test_example(self):
        self.assertEqual(part2(EXAMPLE), 286)


if __name__ == "__main__":  # pragma: no cover
    main()
