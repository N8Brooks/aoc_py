# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/1
"""


from unittest import main, TestCase


from aoc.year2016.day1 import a, b
from aoc.utils import get_input


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(a(get_input(2016, 1)), 161)
    
    def test_example_1(self):
        self.assertEqual(a('R2, L3'), 5)
    
    def test_example_2(self):
        self.assertEqual(a('R2, R2, R2'), 2)
    
    def test_example_3(self):
        self.assertEqual(a('R5, L5, R5, R3'), 12)


class TestB(TestCase):
    def test_input(self):
        self.assertEqual(b(get_input(2016, 1)), 110)
    
    def test_example_2(self):
        self.assertEqual(b('R8, R4, R4, R8'), 4)


if __name__ == '__main__':
    main()