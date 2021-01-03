# -*- coding: utf-8 -*-
""""""


from unittest import TestCase, main


from aoc.year2015.day3 import a, b
from aoc.utils import get_input


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(a(get_input(2015, 3)), 2081)
    
    def test_example_1(self):
        self.assertEqual(a('>'), 2)
    
    def test_example_2(self):
        self.assertEqual(a('^>v<'), 4)
    
    def test_example_3(self):
        self.assertEqual(a('^v^v^v^v^v'), 2)


class TestB(TestCase):
    def test_input(self):
        self.assertEqual(b(get_input(2015, 3)), 2341)
    
    def test_example_1(self):
        self.assertEqual(b('^v'), 3)
    
    def test_example_2(self):
        self.assertEqual(b('^>v<'), 3)
    
    def test_example_3(self):
        self.assertEqual(b('^v^v^v^v^v'), 11)


if __name__ == '__main__':
    main()