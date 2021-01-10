# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/1
"""


from unittest import TestCase, main

from aoc.year2015.day01 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 1)), 232)

    def test_example_1(self):
        self.assertEqual(part1("(())"), 0)

    def test_example_2(self):
        self.assertEqual(part1("()()"), 0)

    def test_example_3(self):
        self.assertEqual(part1("((("), 3)

    def test_example_4(self):
        self.assertEqual(part1("(()(()("), 3)

    def test_example_5(self):
        self.assertEqual(part1("))((((("), 3)

    def test_example_6(self):
        self.assertEqual(part1("())"), -1)

    def test_example_7(self):
        self.assertEqual(part1("))("), -1)

    def test_example_8(self):
        self.assertEqual(part1(")))"), -3)

    def test_example_9(self):
        self.assertEqual(part1(")())())"), -3)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 1)), 1783)

    def test_example_1(self):
        self.assertEqual(part2(")"), 1)

    def test_example_2(self):
        self.assertEqual(part2("()())"), 5)


if __name__ == "__main__":  # pragma: no cover
    main()
