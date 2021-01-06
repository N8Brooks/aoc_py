# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/5
"""


from unittest import TestCase, main

from aoc.year2015.day5 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 5)), 238)

    def test_example_1(self):
        self.assertEqual(part1("ugknbfddgicrmopn"), 1)

    def test_example_2(self):
        self.assertEqual(part1("aaa"), 1)

    def test_example_3(self):
        self.assertEqual(part1("jchzalrnumimnmhp"), 0)

    def test_example_4(self):
        self.assertEqual(part1("haegwjzuvuyypxyu"), 0)

    def test_example_5(self):
        self.assertEqual(part1("dvszwmarrgswjxmb"), 0)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 5)), 69)

    def test_example_1(self):
        self.assertEqual(part2("qjhvhtzxzqqjkmpb"), 1)

    def test_example_2(self):
        self.assertEqual(part2("xxyxx"), 1)

    def test_example_3(self):
        self.assertEqual(part2("uurcxstgmygtbstg"), 0)

    def test_example_4(self):
        self.assertEqual(part2("ieodomkazucvgmuy"), 0)


if __name__ == "__main__":
    main()
