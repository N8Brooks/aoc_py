#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/16
"""


from unittest import main, skip, TestCase

from aoc.year2016.day16 import part1, part2
from data.utils import get_input


EXAMPLE = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2016, 16)), "10100011010101011")

    def test_example_1(self):
        self.assertEqual(part1("1", 10), "01110")

    def test_example_2(self):
        self.assertEqual(part1("0", 10), "10001")

    def test_example_3(self):
        self.assertEqual(part1("11111", 10), "11011")

    def test_example_4(self):
        self.assertEqual(part1("111100001010", 10), "11110")

    def test_example_5(self):
        self.assertEqual(part1("10000", 10), "01111")


class TestPart2(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part2(get_input(2016, 16)), "01010001101011001")

    def test_example_1(self):
        self.assertEqual(part2("1", 20), "01110")

    def test_example_2(self):
        self.assertEqual(part2("0", 20), "01110")

    def test_example_3(self):
        self.assertEqual(part2("11111", 20), "10111")

    def test_example_4(self):
        self.assertEqual(part2("111100001010", 20), "11110")

    def test_example_5(self):
        self.assertEqual(part2("10000", 20), "01100")


if __name__ == "__main__":  # pragma: no cover
    main()
