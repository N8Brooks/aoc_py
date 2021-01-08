# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/8
"""


from unittest import main, TestCase

from aoc.year2016.day8 import part1, part2
from data.utils import get_input


EXAMPLE = """
rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2016, 8)), 121)

    def test_example_1(self):
        self.assertEqual(part1(EXAMPLE), 6)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2016, 8)), "RURUCEOEIL")


if __name__ == "__main__":  # pragma: no cover
    main()
