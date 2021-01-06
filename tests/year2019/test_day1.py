# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2019/day/1
"""


from unittest import main, TestCase

from aoc.year2019.day1 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2019, 1)), 3408471)

    def test_example_1(self):
        self.assertEqual(part1("12"), 2)

    def test_example_2(self):
        self.assertEqual(part1("14"), 2)

    def test_example_3(self):
        self.assertEqual(part1("1969"), 654)

    def test_example_4(self):
        self.assertEqual(part1("100756"), 33583)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2019, 1)), 5109803)

    def test_example_1(self):
        self.assertEqual(part2("14"), 2)

    def test_example_2(self):
        self.assertEqual(part2("1969"), 966)

    def test_example_3(self):
        self.assertEqual(part2("100756"), 50346)


if __name__ == "__main__":
    main()
