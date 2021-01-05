# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/16
"""


from unittest import main, skip, TestCase

from aoc.year2015.day20 import a, b
from aoc.utils import get_input


class TestA(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(a(get_input(2015, 20)), 776160)

    def test_example_1(self):
        self.assertEqual(a(10), 1)

    def test_example_2(self):
        self.assertEqual(a(70), 4)


class TestB(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(b(get_input(2015, 20)), 786240)

    def test_example_1(self):
        self.assertEqual(b(10), 1)

    def test_example_2(self):
        self.assertEqual(b(70), 4)


if __name__ == "__main__":
    main()
