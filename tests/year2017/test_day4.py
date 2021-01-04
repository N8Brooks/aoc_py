# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/4
"""


from unittest import main, TestCase

from aoc.year2017.day4 import a, b
from aoc.utils import get_input


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(a(get_input(2017, 4)), 325)

    def test_example_1(self):
        self.assertEqual(a("aa bb cc dd ee"), 1)

    def test_example_2(self):
        self.assertEqual(a("aa bb cc dd aa"), 0)

    def test_example_3(self):
        self.assertEqual(a("aa bb cc dd aaa"), 1)


class TestB(TestCase):
    def test_input(self):
        self.assertEqual(b(get_input(2017, 4)), 119)

    def test_example_1(self):
        self.assertEqual(b("abcde fghij"), 1)

    def test_example_2(self):
        self.assertEqual(b("abcde xyz ecdab"), 0)

    def test_example_3(self):
        self.assertEqual(b("a ab abc abd abf abj"), 1)

    def test_example_4(self):
        self.assertEqual(b("iiii oiii ooii oooi oooo"), 1)

    def test_example_5(self):
        self.assertEqual(b("oiii ioii iioi iiio"), 0)


if __name__ == "__main__":
    main()
