# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/3
"""


from unittest import main, TestCase

from aoc.year2016.day3 import a, b
from aoc.utils import get_input


EXAMPLE = """101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
"""


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(a(get_input(2016, 3)), 869)

    def test_example_1(self):
        self.assertEqual(a("5 10 25"), 0)

    def test_example_2(self):
        self.assertEqual(a(EXAMPLE), 3)


class TestB(TestCase):
    def test_input(self):
        self.assertEqual(b(get_input(2016, 3)), 1544)

    def test_example_1(self):
        self.assertEqual(b("5 10 25"), 0)

    def test_example_2(self):
        self.assertEqual(b(EXAMPLE), 6)


if __name__ == "__main__":
    main()
