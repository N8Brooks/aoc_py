#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/3
"""


from unittest import main, TestCase

from aoc.year2016.day03 import part1, part2
from data.utils import get_input


EXAMPLE = """101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2016, 3)), 869)

    def test_example_1(self):
        self.assertEqual(part1("5 10 25"), 0)

    def test_example_2(self):
        self.assertEqual(part1(EXAMPLE), 3)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2016, 3)), 1544)

    def test_example_1(self):
        self.assertEqual(part2("5 10 25"), 0)

    def test_example_2(self):
        self.assertEqual(part2(EXAMPLE), 6)


if __name__ == "__main__":  # pragma: no cover
    main()
