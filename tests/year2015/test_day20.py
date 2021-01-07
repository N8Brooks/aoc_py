# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/20
"""


from unittest import main, skip, TestCase

from aoc.year2015.day20 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 20)), 776160)

    def test_example_1(self):
        self.assertEqual(part1(10), 1)

    def test_example_2(self):
        self.assertEqual(part1(70), 4)

    def test_example_3(self):
        self.assertEqual(part1(111), 6)

    def test_example_4(self):
        self.assertEqual(part1(169), 10)


class TestPart2(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 20)), 786240)

    def test_example_1(self):
        self.assertEqual(part2(8), 1)

    def test_example_2(self):
        self.assertEqual(part2(64), 4)

    def test_example_3(self):
        self.assertEqual(part2(133), 8)

    def test_example_4(self):
        self.assertEqual(part2(820), 36)


if __name__ == "__main__":  # pragma: no cover
    main()
