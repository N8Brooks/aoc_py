#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/11
"""


from unittest import main, skip, TestCase

from aoc.year2015.day11 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 11)), "hxbxxyzz")

    @skip("Takes too long")
    def test_example_1(self):
        self.assertEqual(part1("abcdefgh"), "abcdffaa")

    @skip("Takes too long")
    def test_example_2(self):
        self.assertEqual(part1("ghijklmn"), "ghjaabcc")

    def test_mock_1(self):
        self.assertEqual(part1("bbccc"), "bbcdd")

    def test_mock_2(self):
        self.assertEqual(part1("xxydf"), "xxyzz")


class TestPart2(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 11)), "hxcaabcc")

    @skip("Takes too long")
    def test_example_1(self):
        self.assertEqual(part2("abcdefgh"), "abcdffbb")

    @skip("Takes too long")
    def test_example_2(self):
        self.assertEqual(part2("ghijklmn"), "ghjbbcdd")

    def test_mock_1(self):
        self.assertEqual(part2("aabcb"), "bbcdd")

    @skip("Takes too long")
    def test_mock_2(self):
        self.assertEqual(part2("ddefe"), "eefgg")


if __name__ == "__main__":  # pragma: no cover
    main()
