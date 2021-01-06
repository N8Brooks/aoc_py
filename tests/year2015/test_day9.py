# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/9
"""


from unittest import TestCase, main

from aoc.year2015.day9 import part1, part2
from data.utils import get_input


EXAMPLE = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 9)), 117)

    def test_example(self):
        self.assertEqual(part1(EXAMPLE), 605)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 9)), 909)

    def test_example(self):
        self.assertEqual(part2(EXAMPLE), 982)


if __name__ == "__main__":
    main()
