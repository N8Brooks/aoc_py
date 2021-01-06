# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/1
"""


from unittest import main, TestCase

from aoc.year2017.day1 import part1, part2
from aoc.utils import get_input


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2017, 1)), 1136)

    def test_example_1(self):
        self.assertEqual(part1("1122"), 3)

    def test_example_2(self):
        self.assertEqual(part1("1111"), 4)

    def test_example_3(self):
        self.assertEqual(part1("1234"), 0)

    def test_example_4(self):
        self.assertEqual(part1("91212129"), 9)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2017, 1)), 1092)

    def test_example_1(self):
        self.assertEqual(part2("1212"), 6)

    def test_example_2(self):
        self.assertEqual(part2("1221"), 0)

    def test_example_3(self):
        self.assertEqual(part2("123425"), 4)

    def test_example_4(self):
        self.assertEqual(part2("123123"), 12)

    def test_example_5(self):
        self.assertEqual(part2("12131415"), 4)


if __name__ == "__main__":
    main()
