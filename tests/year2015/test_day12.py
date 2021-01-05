# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/10
"""


from unittest import main, TestCase

from aoc.year2015.day12 import a, b
from aoc.utils import get_input


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(a(get_input(2015, 12)), 191164)

    def test_example_1(self):
        self.assertEqual(a("[1,2,3]"), 6)

    def test_example_2(self):
        self.assertEqual(a('{"a":2,"b":4}'), 6)

    def test_example_3(self):
        self.assertEqual(a("[[[3]]]"), 3)

    def test_example_4(self):
        self.assertEqual(a('{"a":{"b":4},"c":-1}'), 3)

    def test_example_5(self):
        self.assertEqual(a('{"a":[-1,1]}'), 0)

    def test_example_6(self):
        self.assertEqual(a('[-1,{"a":1}]'), 0)

    def test_example_7(self):
        self.assertEqual(a("[]"), 0)

    def test_example_8(self):
        self.assertEqual(a("{}"), 0)


class TestB(TestCase):
    def test_input(self):
        self.assertEqual(b(get_input(2015, 12)), 87842)

    def test_example_1(self):
        self.assertEqual(b("[1,2,3]"), 6)

    def test_example_2(self):
        self.assertEqual(b('[1,{"c":"red","b":2},3]'), 4)

    def test_example_3(self):
        self.assertEqual(b('{"d":"red","e":[1,2,3,4],"f":5}'), 0)

    def test_example_4(self):
        self.assertEqual(b('[1,"red",5]'), 6)


if __name__ == "__main__":
    main()
