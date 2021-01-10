#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/11
"""


from unittest import main, TestCase

from aoc.year2017.day11 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2017, 11)), 784)

    def test_example_1(self):
        self.assertEqual(part1("ne,ne,ne"), 3)

    def test_example_2(self):
        self.assertEqual(part1("ne,ne,sw,sw"), 0)

    def test_example_3(self):
        self.assertEqual(part1("ne,ne,s,s"), 2)

    def test_example_4(self):
        self.assertEqual(part1("se,sw,se,sw,sw"), 3)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2017, 11)), 1558)

    def test_example_1(self):
        self.assertEqual(part2("ne,ne,ne"), 3)

    def test_example_2(self):
        self.assertEqual(part2("ne,ne,sw,sw"), 2)

    def test_example_3(self):
        self.assertEqual(part2("ne,ne,s,s"), 2)

    def test_example_4(self):
        self.assertEqual(part2("se,sw,se,sw,sw"), 3)


if __name__ == "__main__":  # pragma: no cover
    main()
