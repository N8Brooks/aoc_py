# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/10
"""


from unittest import main, skip, TestCase

from aoc.year2015.day11 import a, b
from aoc.utils import get_input


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(a(get_input(2015, 11)), "hxbxxyzz")

    def test_example_1(self):
        self.assertEqual(a("abcdefgh"), "abcdffaa")

    @skip("Takes too long")
    def test_example_2(self):
        self.assertEqual(a("ghijklmn"), "ghjaabcc")


class TestB(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(b(get_input(2015, 11)), "hxcaabcc")


if __name__ == "__main__":
    main()
