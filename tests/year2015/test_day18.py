# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/18
"""


from unittest import main, TestCase

from aoc.year2015.day18 import part1, part2
from data.utils import get_input


EXAMPLE = """.#.#.#
...##.
#....#
..#...
#.#..#
####..
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 18)), 1061)

    def test_example(self):
        self.assertEqual(part1(EXAMPLE, 4), 4)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 18)), 1006)

    def test_example(self):
        self.assertEqual(part2(EXAMPLE, 4), 14)


if __name__ == "__main__":  # pragma: no cover
    main()
