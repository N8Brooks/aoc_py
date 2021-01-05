# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/21
"""


from unittest import main, TestCase

from aoc.year2015.day21 import a, b
from aoc.utils import get_input


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(a(get_input(2015, 21)), 111)

    def test_example(self):
        self.assertEqual(a("12 7 2", 8), 65)


class TestB(TestCase):
    def test_input(self):
        self.assertEqual(b(get_input(2015, 21)), 188)

    def test_mock(self):
        self.assertEqual(b("6 7 2", 8), 88)


if __name__ == "__main__":
    main()
