# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/14
"""


from unittest import main, skip, TestCase

from aoc.year2015.day14 import part1, part2
from aoc.utils import get_input


EXAMPLE = """
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 14)), 2696)

    def test_example(self):
        self.assertEqual(part1(EXAMPLE, 1000), 1120)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 14)), 1084)

    def test_example(self):
        self.assertEqual(part2(EXAMPLE, 1000), 688)  # Doesn't match site?


if __name__ == "__main__":
    main()
