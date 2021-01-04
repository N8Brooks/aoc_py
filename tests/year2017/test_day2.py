# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/2
"""


from unittest import main, TestCase

from aoc.year2017.day2 import a, b
from aoc.utils import get_input


EXAMPLE_1 = """5 1 9 5
7 5 3
2 4 6 8
"""

EXAMPLE_2 = """5 9 2 8
9 4 7 3
3 8 6 5
"""


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(a(get_input(2017, 2)), 51833)

    def test_example(self):
        self.assertEqual(a(EXAMPLE_1), 18)


class TestB(TestCase):
    def test_input(self):
        self.assertEqual(b(get_input(2017, 2)), 288)

    def test_example(self):
        self.assertEqual(b(EXAMPLE_2), 9)


if __name__ == "__main__":
    main()
