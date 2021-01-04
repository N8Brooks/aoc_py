# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2020/day/1
"""


from unittest import main, TestCase

from aoc.year2020.day1 import a, b
from aoc.utils import get_input


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(a(get_input(2020, 1), 2020), 482811)

    def test_example_1(self):
        self.assertEqual(a("1721 979 366 299 675 1456", 2020), 514579)


class TestB(TestCase):
    def test_input(self):
        self.assertEqual(b(get_input(2020, 1), 2020), 193171814)

    def test_example_1(self):
        self.assertEqual(b("1721 979 366 299 675 1456", 2020), 241861950)


if __name__ == "__main__":
    main()
