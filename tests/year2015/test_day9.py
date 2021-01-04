# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/9
"""


from unittest import TestCase, main

from aoc.year2015.day9 import a, b
from aoc.utils import get_input


EXAMPLE = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(a(get_input(2015, 9)), 117)

    def test_example(self):
        self.assertEqual(a(EXAMPLE), 605)


class TestB(TestCase):
    def test_input(self):
        self.assertEqual(b(get_input(2015, 9)), 909)

    def test_example(self):
        self.assertEqual(b(EXAMPLE), 982)


if __name__ == "__main__":
    main()
