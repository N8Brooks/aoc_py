# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/10
"""


from unittest import main, skip, TestCase

from aoc.year2015.day10 import look_say, part1, part2
from aoc.utils import get_input


class TestLookSay(TestCase):
    def test_example_1(self):
        self.assertEqual(look_say("1"), "11")

    def test_example_2(self):
        self.assertEqual(look_say("11"), "21")

    def test_example_3(self):
        self.assertEqual(look_say("21"), "1211")

    def test_example_4(self):
        self.assertEqual(look_say("1211"), "111221")

    def test_example_5(self):
        self.assertEqual(look_say("111221"), "312211")


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 10)), 252594)

    def test_mock_1(self):
        self.assertEqual(part1("1234", 10), 112)

    def test_mock_2(self):
        self.assertEqual(part1("121", 20), 750)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 10)), 3579328)

    def test_mock_1(self):
        self.assertEqual(part2("1", 5), 6)

    def test_mock_2(self):
        self.assertEqual(part2("1", 25), 1540)


if __name__ == "__main__":
    main()
