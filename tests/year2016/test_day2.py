# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/2
"""


from unittest import main, TestCase

from aoc.year2016.day2 import part1, part2
from data.utils import get_input


EXAMPLE = """ULL
RRDDD
LURDL
UUUUD
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2016, 2)), "24862")

    def test_example(self):
        self.assertEqual(part1(EXAMPLE), "1985")


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2016, 2)), "46C91")

    def test_example(self):
        self.assertEqual(part2(EXAMPLE), "5DB3")


if __name__ == "__main__":
    main()
