# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2018/day/2
"""


from unittest import main, TestCase

from aoc.year2018.day2 import part1, part2
from data.utils import get_input


EXAMPLE_1 = """abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab
"""

EXAMPLE_2 = """abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2018, 2)), 5681)

    def test_example_1(self):
        self.assertEqual(part1(EXAMPLE_1), 12)

    def test_example_2(self):
        self.assertEqual(part1(EXAMPLE_2), 0)


class TestPart2(TestCase):
    def test_input(self):
        expected = "uqyoeizfvmbistpkgnocjtwld"
        self.assertEqual(part2(get_input(2018, 2)), expected)

    def test_example_1(self):
        self.assertEqual(part2(EXAMPLE_1), "abcde")

    def test_example_2(self):
        self.assertEqual(part2(EXAMPLE_2), "fgij")


if __name__ == "__main__":  # pragma: no cover
    main()
