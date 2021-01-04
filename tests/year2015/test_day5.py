# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/1
"""


from unittest import TestCase, main

from aoc.year2015.day5 import a, b
from aoc.utils import get_input


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(a(get_input(2015, 5)), 238)

    def test_example_1(self):
        self.assertEqual(a("ugknbfddgicrmopn"), 1)

    def test_example_2(self):
        self.assertEqual(a("aaa"), 1)

    def test_example_3(self):
        self.assertEqual(a("jchzalrnumimnmhp"), 0)

    def test_example_4(self):
        self.assertEqual(a("haegwjzuvuyypxyu"), 0)

    def test_example_5(self):
        self.assertEqual(a("dvszwmarrgswjxmb"), 0)


class TestB(TestCase):
    def test_input(self):
        self.assertEqual(b(get_input(2015, 5)), 69)

    def test_example_1(self):
        self.assertEqual(b("qjhvhtzxzqqjkmpb"), 1)

    def test_example_2(self):
        self.assertEqual(b("xxyxx"), 1)

    def test_example_3(self):
        self.assertEqual(b("uurcxstgmygtbstg"), 0)

    def test_example_4(self):
        self.assertEqual(b("ieodomkazucvgmuy"), 0)


if __name__ == "__main__":
    main()
