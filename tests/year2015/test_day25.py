# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/23
"""


from unittest import main, TestCase

from aoc.year2015.day25 import part1
from data.utils import get_input


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 25)), 19980801)

    def test_example_1_1(self):
        self.assertEqual(part1("1, 1"), 20151125)

    def test_example_2_1(self):
        self.assertEqual(part1("1, 2"), 18749137)

    def test_example_3_1(self):
        self.assertEqual(part1("1, 3"), 17289845)

    def test_example_4_1(self):
        self.assertEqual(part1("1, 4"), 30943339)

    def test_example_5_1(self):
        self.assertEqual(part1("1, 5"), 10071777)

    def test_example_6_1(self):
        self.assertEqual(part1("1, 6"), 33511524)

    def test_example_1_2(self):
        self.assertEqual(part1("2, 1"), 31916031)

    def test_example_2_2(self):
        self.assertEqual(part1("2, 2"), 21629792)

    def test_example_3_2(self):
        self.assertEqual(part1("2, 3"), 16929656)

    def test_example_4_2(self):
        self.assertEqual(part1("2, 4"), 7726640)

    def test_example_5_2(self):
        self.assertEqual(part1("2, 5"), 15514188)

    def test_example_6_2(self):
        self.assertEqual(part1("2, 6"), 4041754)

    def test_example_1_3(self):
        self.assertEqual(part1("3, 1"), 16080970)

    def test_example_2_3(self):
        self.assertEqual(part1("3, 2"), 8057251)

    def test_example_3_3(self):
        self.assertEqual(part1("3, 3"), 1601130)

    def test_example_4_3(self):
        self.assertEqual(part1("3, 4"), 7981243)

    def test_example_5_3(self):
        self.assertEqual(part1("3, 5"), 11661866)

    def test_example_6_3(self):
        self.assertEqual(part1("3, 6"), 16474243)

    def test_example_1_4(self):
        self.assertEqual(part1("4, 1"), 24592653)

    def test_example_2_4(self):
        self.assertEqual(part1("4, 2"), 32451966)

    def test_example_3_4(self):
        self.assertEqual(part1("4, 3"), 21345942)

    def test_example_4_4(self):
        self.assertEqual(part1("4, 4"), 9380097)

    def test_example_5_4(self):
        self.assertEqual(part1("4, 5"), 10600672)

    def test_example_6_4(self):
        self.assertEqual(part1("4, 6"), 31527494)

    def test_example_1_5(self):
        self.assertEqual(part1("5, 1"), 77061)

    def test_example_2_5(self):
        self.assertEqual(part1("5, 2"), 17552253)

    def test_example_3_5(self):
        self.assertEqual(part1("5, 3"), 28094349)

    def test_example_4_5(self):
        self.assertEqual(part1("5, 4"), 6899651)

    def test_example_5_5(self):
        self.assertEqual(part1("5, 5"), 9250759)

    def test_example_6_5(self):
        self.assertEqual(part1("5, 6"), 31663883)

    def test_example_1_6(self):
        self.assertEqual(part1("6, 1"), 33071741)

    def test_example_2_6(self):
        self.assertEqual(part1("6, 2"), 6796745)

    def test_example_3_6(self):
        self.assertEqual(part1("6, 3"), 25397450)

    def test_example_4_6(self):
        self.assertEqual(part1("6, 4"), 24659492)

    def test_example_5_6(self):
        self.assertEqual(part1("6, 5"), 1534922)

    def test_example_6_6(self):
        self.assertEqual(part1("6, 6"), 27995004)


if __name__ == "__main__":  # pragma: no cover
    main()
