# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2019/day/1
"""


from unittest import main, TestCase

from aoc.year2019.day1 import a, b
from aoc.utils import get_input


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(a(get_input(2019, 1)), 3408471)

    def test_example_1(self):
        self.assertEqual(a("12"), 2)

    def test_example_2(self):
        self.assertEqual(a("14"), 2)

    def test_example_3(self):
        self.assertEqual(a("1969"), 654)

    def test_example_4(self):
        self.assertEqual(a("100756"), 33583)


class TestB(TestCase):
    def test_input(self):
        self.assertEqual(b(get_input(2019, 1)), 5109803)

    def test_example_1(self):
        self.assertEqual(b("14"), 2)

    def test_example_2(self):
        self.assertEqual(b("1969"), 966)

    def test_example_3(self):
        self.assertEqual(b("100756"), 50346)


if __name__ == "__main__":
    main()
