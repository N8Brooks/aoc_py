# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2017/day/7
"""


from unittest import main, TestCase

from aoc.year2017.day07 import part1, part2
from data.utils import get_input


EXAMPLE = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2017, 7)), "ahnofa")

    def test_example(self):
        self.assertEqual(part1(EXAMPLE), "tknk")


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2017, 7)), 802)

    def test_example(self):
        self.assertEqual(part2(EXAMPLE), 60)


if __name__ == "__main__":  # pragma: no cover
    main()
