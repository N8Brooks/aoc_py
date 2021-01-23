#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2020/day/8
"""


from unittest import main, TestCase

from aoc.year2020.day08 import part1, part2
from data.utils import get_input


EXAMPLE = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2020, 8)), 1766)

    def test_example(self):
        self.assertEqual(part1(EXAMPLE), 5)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2020, 8)), 1639)

    def test_example_1(self):
        self.assertEqual(part2(EXAMPLE), 8)


if __name__ == "__main__":  # pragma: no cover
    main()
