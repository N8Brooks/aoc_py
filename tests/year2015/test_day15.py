# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/15
"""


from unittest import main, skip, TestCase

from aoc.year2015.day15 import a, b
from aoc.utils import get_input


EXAMPLE = """
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"""


class TestA(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(a(get_input(2015, 15)), 18965440)

    def test_example(self):
        self.assertEqual(a(EXAMPLE), 62842880)


class TestB(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(b(get_input(2015, 15)), 15862900)

    def test_example(self):
        self.assertEqual(b(EXAMPLE), 57600000)


if __name__ == "__main__":
    main()
