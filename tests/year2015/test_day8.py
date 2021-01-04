# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/1
"""


from unittest import TestCase, main

from aoc.year2015.day8 import a, b
from aoc.utils import get_input


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(a(get_input(2015, 8)), 1333)

    def test_example_1(self):
        self.assertEqual(a('""'), 2)

    def test_example_2(self):
        self.assertEqual(a('"abc"'), 2)

    def test_example_3(self):
        self.assertEqual(a('"aaa\\"aaa"'), 3)

    def test_example_4(self):
        self.assertEqual(a('"\\x27"'), 5)


class TestB(TestCase):
    def test_input(self):
        self.assertEqual(b(get_input(2015, 8)), 2046)

    def test_example_1(self):
        self.assertEqual(b('""'), 4)

    def test_example_2(self):
        self.assertEqual(b('"abc"'), 4)

    def test_example_3(self):
        self.assertEqual(b('"aaa\\"aaa"'), 6)

    def test_example_4(self):
        self.assertEqual(b('"\\x27"'), 5)


if __name__ == "__main__":
    main()
