#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2020/day/9
"""


from unittest import main, TestCase

from aoc.year2020.day09 import part1, part2
from data.utils import get_input


EXAMPLE = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2020, 9)), 22477624)

    def test_example(self):
        self.assertEqual(part1(EXAMPLE, 5), 127)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2020, 9)), 2980044)

    def test_example(self):
        self.assertEqual(part2(EXAMPLE, 5), 62)


if __name__ == "__main__":  # pragma: no cover
    main()
