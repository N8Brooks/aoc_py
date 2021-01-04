# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/6
"""


from unittest import TestCase, main

from aoc.year2015.day6 import a, b
from aoc.utils import get_input


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(a(get_input(2015, 6), 1000), 543903)

    def test_example_1(self):
        self.assertEqual(a("turn on 0,0 through 999,999", 1000), 1000000)

    def test_example_2(self):
        self.assertEqual(a("toggle 0,0 through 999,0", 1000), 1000)

    def test_example_3(self):
        self.assertEqual(a("turn off 499,499 through 500,500", 1000), 0)


class TestB(TestCase):
    def test_input(self):
        self.assertEqual(b(get_input(2015, 6), 1000), 14687245)

    def test_example_1(self):
        self.assertEqual(b("turn on 0,0 through 0,0", 1000), 1)

    def test_example_2(self):
        self.assertEqual(b("toggle 0,0 through 999,999", 1000), 2000000)


if __name__ == "__main__":
    main()
