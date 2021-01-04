# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/7
"""


from unittest import TestCase, main

from aoc.year2015.day7 import a, b
from aoc.utils import get_input


EXAMPLE = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
"""


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(a(get_input(2015, 7)), 16076)

    def test_example_d(self):
        self.assertEqual(a(EXAMPLE, "d"), 72)

    def test_example_e(self):
        self.assertEqual(a(EXAMPLE, "e"), 507)

    def test_example_f(self):
        self.assertEqual(a(EXAMPLE, "f"), 492)

    def test_example_g(self):
        self.assertEqual(a(EXAMPLE, "g"), 114)

    def test_example_h(self):
        self.assertEqual(a(EXAMPLE, "h"), 65412)

    def test_example_i(self):
        self.assertEqual(a(EXAMPLE, "i"), 65079)

    def test_example_x(self):
        self.assertEqual(a(EXAMPLE, "x"), 123)

    def test_example_y(self):
        self.assertEqual(a(EXAMPLE, "y"), 456)


class TestB(TestCase):
    def test_input(self):
        self.assertEqual(b(get_input(2015, 7)), 2797)


if __name__ == "__main__":
    main()
