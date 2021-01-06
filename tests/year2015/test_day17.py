# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/17
"""


from unittest import main, TestCase

from aoc.year2015.day17 import part1, part2
from aoc.utils import get_input


EXAMPLE = "20 15 10 5 5"


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 17)), 654)

    def test_example(self):
        self.assertEqual(part1(EXAMPLE, 25), 4)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 17)), 57)

    def test_example(self):
        self.assertEqual(part2(EXAMPLE, 25), 3)


if __name__ == "__main__":
    main()
