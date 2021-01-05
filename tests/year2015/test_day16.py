# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/16
"""


from unittest import main, TestCase

from aoc.year2015.day16 import a, b
from aoc.utils import get_input


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(a(get_input(2015, 16)), 213)


class TestB(TestCase):
    def test_input(self):
        self.assertEqual(b(get_input(2015, 16)), 323)


if __name__ == "__main__":
    main()
