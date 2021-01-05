# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/6
"""


from unittest import main, TestCase

from aoc.year2016.day6 import a, b
from aoc.utils import get_input


EXAMPLE = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
"""


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(a(get_input(2016, 6)), "gyvwpxaz")

    def test_example(self):
        self.assertEqual(a(EXAMPLE), "easter")


class TestB(TestCase):
    def test_input(self):
        self.assertEqual(b(get_input(2016, 6)), "jucfoary")

    def test_example(self):
        self.assertEqual(b(EXAMPLE), "advent")


if __name__ == "__main__":
    main()
