# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/1
"""


from unittest import TestCase, main

from aoc.year2015.day1 import part1, part2
from aoc.utils import get_input


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 1)), 232)

    def test_example_1a(self):
        self.assertEqual(part1("(())"), 0)

    def test_example_1b(self):
        self.assertEqual(part1("()()"), 0)

    def test_example_2a(self):
        self.assertEqual(part1("((("), 3)

    def test_example_2b(self):
        self.assertEqual(part1("(()(()("), 3)

    def test_example_2c(self):
        self.assertEqual(part1("))((((("), 3)

    def test_example_3a(self):
        self.assertEqual(part1("())"), -1)

    def test_example_3b(self):
        self.assertEqual(part1("))("), -1)

    def test_example_4a(self):
        self.assertEqual(part1(")))"), -3)

    def test_example_4b(self):
        self.assertEqual(part1(")())())"), -3)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 1)), 1783)

    def test_example_1(self):
        self.assertEqual(part2(")"), 1)

    def test_example_2(self):
        self.assertEqual(part2("()())"), 5)


if __name__ == "__main__":
    main()
