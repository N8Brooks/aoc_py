# -*- coding: utf-8 -*-
""""""


from unittest import TestCase, main


from aoc.year2015.day4 import ab
from aoc.utils import get_input


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(ab(get_input(2015, 4), '00000'), 346386)


class TestB(TestCase):
    def test_input(self):
        self.assertEqual(ab(get_input(2015, 4), '000000'), 9958218)


if __name__ == '__main__':
    main()