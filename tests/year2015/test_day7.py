# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/7
"""


from unittest import TestCase, main

from aoc.year2015.day7 import part1, part2
from data.utils import get_input


EXAMPLE = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 7)), 16076)

    def test_example_d(self):
        self.assertEqual(part1(EXAMPLE, "d"), 72)

    def test_example_e(self):
        self.assertEqual(part1(EXAMPLE, "e"), 507)

    def test_example_f(self):
        self.assertEqual(part1(EXAMPLE, "f"), 492)

    def test_example_g(self):
        self.assertEqual(part1(EXAMPLE, "g"), 114)

    def test_example_h(self):
        self.assertEqual(part1(EXAMPLE, "h"), 65412)

    def test_example_i(self):
        self.assertEqual(part1(EXAMPLE, "i"), 65079)

    def test_example_x(self):
        self.assertEqual(part1(EXAMPLE, "x"), 123)

    def test_example_y(self):
        self.assertEqual(part1(EXAMPLE, "y"), 456)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 7)), 2797)


if __name__ == "__main__":  # pragma: no cover
    main()
