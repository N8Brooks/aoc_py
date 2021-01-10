# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/7
"""


from unittest import main, TestCase

from aoc.year2016.day07 import part1, part2
from data.utils import get_input


EXAMPLE_1 = """abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn
"""

EXAMPLE_2 = """aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2016, 7)), 115)

    def test_example_1(self):
        self.assertEqual(part1(EXAMPLE_1), 2)

    def test_example_2(self):
        self.assertEqual(part1(EXAMPLE_2), 0)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2016, 7)), 231)

    def test_example_1(self):
        self.assertEqual(part2(EXAMPLE_1), 0)

    def test_example_2(self):
        self.assertEqual(part2(EXAMPLE_2), 3)


if __name__ == "__main__":  # pragma: no cover
    main()
