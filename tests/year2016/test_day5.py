# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/5
"""


from unittest import main, skip, TestCase

from aoc.year2016.day5 import a, b
from aoc.utils import get_input


class TestA(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(a(get_input(2016, 5)), "c6697b55")

    @skip("Takes too long")
    def test_example(self):
        self.assertEqual(a("abc"), "18f47a30")

    def test_mock_1(self):
        self.assertEqual(a("abc", 4, "0"), "890c")

    def test_mock_2(self):
        self.assertEqual(a("xyz", 2, "00"), "ee")


class TestB(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(b(get_input(2016, 5)), "8c35d1ab")

    @skip("Takes too long")
    def test_example(self):
        self.assertEqual(b("abc"), "05ace8e3")

    def test_mock_1(self):
        self.assertEqual(b("abc", 4, "0"), "3010")

    def test_mock_2(self):
        self.assertEqual(b("xyz", 2, "00"), "cd")


if __name__ == "__main__":
    main()
