# -*- coding: utf-8 -*-
""""""


from unittest import TestCase, main


from aoc.year2015.day2 import a, b
from aoc.utils import get_input


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(a(get_input(2015, 2)), 1606483)


class TestB(TestCase):
    def test_input(self):
        self.assertEqual(b(get_input(2015, 2)), 3842356)
    

if __name__ == '__main__':
    main()