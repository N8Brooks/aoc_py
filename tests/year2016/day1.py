# -*- coding: utf-8 -*-
""""""


from unittest import TestCase, main


from aoc.year2016.day1 import a, b
from aoc.utils import get_input


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(a(get_input(2016, 1)), 161)


class TestB(TestCase):
    def test_input(self):
        self.assertEqual(b(get_input(2016, 1)), 110)


if __name__ == '__main__':
    main()