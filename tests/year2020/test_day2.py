# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2020/day/2
"""


from unittest import main, TestCase

from aoc.year2020.day2 import part1, part2
from data.utils import get_input


EXAMPLE = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2020, 2)), 591)

    def test_example(self):
        self.assertEqual(part1(EXAMPLE), 2)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2020, 2)), 335)

    def test_example(self):
        self.assertEqual(part2(EXAMPLE), 1)


if __name__ == "__main__":  # pragma: no cover
    main()
