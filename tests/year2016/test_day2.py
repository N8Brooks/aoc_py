# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/2
"""


from unittest import main, TestCase

from aoc.year2016.day2 import a, b
from aoc.utils import get_input


EXAMPLE = """ULL
RRDDD
LURDL
UUUUD
"""


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(a(get_input(2016, 2)), "24862")

    def test_example(self):
        self.assertEqual(a(EXAMPLE), "1985")


class TestB(TestCase):
    def test_input(self):
        self.assertEqual(b(get_input(2016, 2)), "46C91")

    def test_example(self):
        self.assertEqual(b(EXAMPLE), "5DB3")


if __name__ == "__main__":
    main()
