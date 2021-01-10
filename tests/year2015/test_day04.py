#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/4
"""


from unittest import TestCase, main, skip

from aoc.year2015.day04 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    @skip("Takes too long")
    def test_input_a(self):
        self.assertEqual(part1(get_input(2015, 4)), 346386)

    @skip("Takes too long")
    def test_example_1(self):
        self.assertEqual(part1("abcdef"), 609043)

    @skip("Takes too long")
    def test_example_2(self):
        self.assertEqual(part1("pqrstuv"), 1048970)

    def test_mock_1(self):
        self.assertEqual(part1("abc", "0"), 5)

    def test_mock_2(self):
        self.assertEqual(part1("leet", "00"), 498)

    def test_mock_3(self):
        self.assertEqual(part1("abcde", "000"), 3452)


class TestPart2(TestCase):
    @skip("Takes too long")
    def test_input_b(self):
        self.assertEqual(part2(get_input(2015, 4)), 9958218)

    @skip("Takes too long")
    def test_example_1(self):
        self.assertEqual(part2("abcdef"), 6742839)

    @skip("Takes too long")
    def test_example_2(self):
        self.assertEqual(part2("pqrstuv"), 5714438)

    def test_mock_1(self):
        self.assertEqual(part2("123", "0"), 10)

    def test_mock_2(self):
        self.assertEqual(part2("panda", "00"), 107)

    def test_mock_3(self):
        self.assertEqual(part2("giraff", "000"), 1803)


if __name__ == "__main__":  # pragma: no cover
    main()
