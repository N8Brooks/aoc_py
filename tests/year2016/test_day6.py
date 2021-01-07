# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/6
"""


from unittest import main, TestCase

from aoc.year2016.day6 import part1, part2
from data.utils import get_input


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


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2016, 6)), "gyvwpxaz")

    def test_example(self):
        self.assertEqual(part1(EXAMPLE), "easter")


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2016, 6)), "jucfoary")

    def test_example(self):
        self.assertEqual(part2(EXAMPLE), "advent")


if __name__ == "__main__":  # pragma: no cover
    main()
