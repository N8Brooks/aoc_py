# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/16
"""


from unittest import main, TestCase

from aoc.year2015.day17 import a, b
from aoc.utils import get_input


EXAMPLE = "20 15 10 5 5"


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(a(get_input(2015, 17)), 654)

    def test_example(self):
        self.assertEqual(a(EXAMPLE, 25), 4)


class TestB(TestCase):
    def test_input(self):
        self.assertEqual(b(get_input(2015, 17)), 57)

    def test_example(self):
        self.assertEqual(b(EXAMPLE, 25), 3)


if __name__ == "__main__":
    main()
