# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2020/day/7
"""


from unittest import main, TestCase

from aoc.year2020.day07 import part1, part2
from data.utils import get_input


EXAMPLE_1 = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

EXAMPLE_2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2020, 7)), 205)

    def test_example_1(self):
        self.assertEqual(part1(EXAMPLE_1), 4)

    def test_example_2(self):
        self.assertEqual(part1(EXAMPLE_2), 0)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2020, 7)), 80902)

    def test_example_1(self):
        self.assertEqual(part2(EXAMPLE_1), 32)

    def test_example_2(self):
        self.assertEqual(part2(EXAMPLE_2), 126)


if __name__ == "__main__":  # pragma: no cover
    main()
