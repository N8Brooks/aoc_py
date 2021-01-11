#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2018/day/5
"""


from unittest import main, skip, TestCase

from aoc.year2018.day05 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part1(get_input(2018, 5)), 10886)

    def test_example(self):
        self.assertEqual(part1("dabAcCaCBAcCcaDA"), 10)


class TestPart2(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part2(get_input(2018, 5)), 4684)

    def test_example(self):
        self.assertEqual(part2("dabAcCaCBAcCcaDA"), 4)


if __name__ == "__main__":  # pragma: no cover
    main()
