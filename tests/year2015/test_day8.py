# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/8
"""


from unittest import TestCase, main

from aoc.year2015.day8 import part1, part2
from aoc.utils import get_input


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 8)), 1333)

    def test_example_1(self):
        self.assertEqual(part1('""'), 2)

    def test_example_2(self):
        self.assertEqual(part1('"abc"'), 2)

    def test_example_3(self):
        self.assertEqual(part1('"aaa\\"aaa"'), 3)

    def test_example_4(self):
        self.assertEqual(part1('"\\x27"'), 5)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 8)), 2046)

    def test_example_1(self):
        self.assertEqual(part2('""'), 4)

    def test_example_2(self):
        self.assertEqual(part2('"abc"'), 4)

    def test_example_3(self):
        self.assertEqual(part2('"aaa\\"aaa"'), 6)

    def test_example_4(self):
        self.assertEqual(part2('"\\x27"'), 5)


if __name__ == "__main__":
    main()
