#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/15
"""


from unittest import main, skip, TestCase

from aoc.year2015.day15 import part1, part2
from data.utils import get_input


EXAMPLE = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
"""

MOCK = """Sugar: capacity 2, durability 1, flavor 5, texture 1, calories 4
Capsaicin: capacity 1, durability 5, flavor -5, texture 3, calories 1
Butter: capacity 1, durability 3, flavor 3, texture 3, calories 9
"""


class TestPart1(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 15)), 18965440)

    def test_example(self):
        self.assertEqual(part1(EXAMPLE), 62842880)

    @skip("Takes too long")
    def test_mock(self):
        self.assertEqual(part1(MOCK), 2766555000)


class TestPart2(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 15)), 2766555000)

    def test_example(self):
        self.assertEqual(part2(EXAMPLE), 57600000)

    def test_mock(self):
        self.assertEqual(part2(MOCK), 1884745728)


if __name__ == "__main__":  # pragma: no cover
    main()
