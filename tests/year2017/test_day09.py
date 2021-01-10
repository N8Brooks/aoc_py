# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/9
"""


from unittest import main, TestCase

from aoc.year2017.day09 import part1, part2
from data.utils import get_input


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2017, 9)), 11089)

    def test_example_1(self):
        self.assertEqual(part1("{}"), 1)

    def test_example_2(self):
        self.assertEqual(part1("{{{}}}"), 6)

    def test_example_3(self):
        self.assertEqual(part1("{{},{}}"), 5)

    def test_example_4(self):
        self.assertEqual(part1("{{{},{},{{}}}}"), 16)

    def test_example_5(self):
        self.assertEqual(part1("{<a>,<a>,<a>,<a>}"), 1)

    def test_example_6(self):
        self.assertEqual(part1("{{<ab>},{<ab>},{<ab>},{<ab>}}"), 9)

    def test_example_7(self):
        self.assertEqual(part1("{{<!!>},{<!!>},{<!!>},{<!!>}}"), 9)

    def test_example_8(self):
        self.assertEqual(part1("{{<a!>},{<a!>},{<a!>},{<ab>}}"), 3)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2017, 9)), 5288)

    def test_example_1(self):
        self.assertEqual(part2("<>"), 0)

    def test_example_2(self):
        self.assertEqual(part2("<random characters>"), 17)

    def test_example_3(self):
        self.assertEqual(part2("<<<<>"), 3)

    def test_example_4(self):
        self.assertEqual(part2("<{!>}>"), 2)

    def test_example_5(self):
        self.assertEqual(part2("<!!>"), 0)

    def test_example_6(self):
        self.assertEqual(part2("<!!!>>"), 0)

    def test_example_7(self):
        self.assertEqual(part2('<{o"i!a,<{i<a>'), 10)


if __name__ == "__main__":  # pragma: no cover
    main()
