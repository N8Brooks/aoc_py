# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/23
"""


from unittest import main, TestCase

from aoc.year2015.day23 import part1, part2
from data.utils import get_input


EXAMPLE = """inc a
jio a, +2
tpl a
inc a
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 23)), 307)

    def test_example_a(self):
        self.assertEqual(part1(EXAMPLE, target="a"), 2)

    def test_example_b(self):
        self.assertEqual(part1(EXAMPLE, target="b"), 0)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 23)), 160)

    def test_example_a(self):
        self.assertEqual(part2(EXAMPLE, a=2, target="a"), 10)

    def test_example_b(self):
        self.assertEqual(part2(EXAMPLE, target="b"), 0)


if __name__ == "__main__":  # pragma: no cover
    main()
