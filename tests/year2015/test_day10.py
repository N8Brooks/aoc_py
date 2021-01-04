# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/10
"""


from unittest import main, skip, TestCase

from aoc.year2015.day10 import ab, look_say
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


class TestAB(TestCase):
    def test_mock_1(self):
        self.assertEqual(ab("1234", 10), 112)

    def test_mock_2(self):
        self.assertEqual(ab("121", 20), 750)

    def test_mock_3(self):
        self.assertEqual(ab("1", 30), 5808)

    @skip("Takes too long")
    def test_input_a(self):
        self.assertEqual(ab(get_input(2015, 10), 40), 252594)

    @skip("Takes too long")
    def test_input_b(self):
        self.assertEqual(ab(get_input(2015, 10), 50), 3579328)


if __name__ == "__main__":
    main()
