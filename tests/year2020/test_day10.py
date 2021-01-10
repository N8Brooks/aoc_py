#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2020/day/10
"""


from unittest import main, TestCase

from aoc.year2020.day10 import part1, part2
from data.utils import get_input


EXAMPLE_1 = "16 10 15 5 1 11 7 19 6 12 4"

EXAMPLE_2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2020, 10)), 2760)

    def test_example_1(self):
        self.assertEqual(part1(EXAMPLE_1), 35)

    def test_example_2(self):
        self.assertEqual(part1(EXAMPLE_2), 220)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2020, 10)), 13816758796288)

    def test_example_1(self):
        self.assertEqual(part2(EXAMPLE_1), 8)

    def test_example_2(self):
        self.assertEqual(part2(EXAMPLE_2), 19208)


if __name__ == "__main__":  # pragma: no cover
    main()
