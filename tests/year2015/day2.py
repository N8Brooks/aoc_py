# -*- coding: utf-8 -*-
""""""


from unittest import TestCase, main


from aoc.year2015.day2 import a, b
from aoc.utils import get_input


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(a(get_input(2015, 2)), 1606483)
    
    def test_example_1(self):
        self.assertEqual(a('2x3x4'), 58)
    
    def test_example_2(self):
        self.assertEqual(a('1x1x10'), 43)


class TestB(TestCase):
    def test_input(self):
        self.assertEqual(b(get_input(2015, 2)), 3842356)
    
    def test_example_1(self):
        self.assertEqual(b('2x3x4'), 34)
    
    def test_example_2(self):
        self.assertEqual(b('1x1x10'), 14)
    

if __name__ == '__main__':
    main()