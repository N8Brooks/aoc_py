# -*- coding: utf-8 -*-
"""
"""


from unittest import TestCase, main


from aoc.year2015.day1 import *


class TestA(TestCase):
    def test_input(self):
        pass
    
    def test_example_1a(self):
        self.assertEqual(a('(())'), 0)
    
    def test_example_1b(self):
        self.assertEqual(a('()()'), 0)
    
    def test_example_2a(self):
        self.assertEqual(a('((('), 3)
    
    def test_example_2b(self):
        self.assertEqual(a('(()(()('), 3)
    
    def test_example_2c(self):
        self.assertEqual(a('))((((('), 3)
    
    def test_example_3a(self):
        self.assertEqual(a('())'), -1)
    
    def test_example_3b(self):
        self.assertEqual(a('))('), -1)
    
    def test_example_4a(self):
        self.assertEqual(a(')))'), -3)
    
    def test_example_4b(self):
        self.assertEqual(a(')())())'), -3)


class TestB(TestCase):
    def test_input(self):
        pass
    
    def test_example_1(self):
        self.assertEqual(b(')'), 1)
    
    def test_example_2(self):
        self.assertEqual(b('()())'), 5)
    

if __name__ == '__main__':
    main()