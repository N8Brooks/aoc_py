# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2020/day/6
"""


from unittest import main, TestCase

from aoc.year2020.day6 import part1, part2
from data.utils import get_input


EXAMPLE_1 = """abcx
abcy
abcz
"""

EXAMPLE_2 = """abc

a
b
c

ab
ac

a
a
a
a

b
"""

EXAMPLE_3 = """abc

a
b
c

ab
ac

a
a
a
a

b
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2020, 6)), 6532)

    def test_example_1(self):
        self.assertEqual(part1(EXAMPLE_1), 6)

    def test_example_2(self):
        self.assertEqual(part1(EXAMPLE_2), 11)

    def test_example_3(self):
        self.assertEqual(part1(EXAMPLE_3), 11)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2020, 6)), 3427)

    def test_example_1(self):
        self.assertEqual(part2(EXAMPLE_1), 3)

    def test_example_2(self):
        self.assertEqual(part2(EXAMPLE_2), 6)

    def test_example_3(self):
        self.assertEqual(part2(EXAMPLE_3), 6)


if __name__ == "__main__":  # pragma: no cover
    main()
