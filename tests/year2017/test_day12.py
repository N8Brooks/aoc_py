#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/12
"""


from unittest import main, TestCase

from aoc.year2017.day12 import part1, part2
from data.utils import get_input


EXAMPLE = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2017, 12)), 306)

    def test_example(self):
        self.assertEqual(part1(EXAMPLE), 6)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2017, 12)), 200)

    def test_example(self):
        self.assertEqual(part2(EXAMPLE), 2)


if __name__ == "__main__":  # pragma: no cover
    main()
