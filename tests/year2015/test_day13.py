#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/13
"""


from unittest import main, skip, TestCase

from aoc.year2015.day13 import part1, part2
from data.utils import get_input


EXAMPLE = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
"""
MOCK = """Jody would loose 200 happiness units by sitting next to Carol.
Jody would loose 100 happiness units by sitting next to Irwin.
Jody would loose 1000 happiness units by sitting next to Aligator.
Carol would loose 42 happiness units by sitting next to Jody.
Carol would gain 512 happiness units by sitting next to Irwin.
Carol would loose 300 happiness units by sitting next to Aligator.
Irwin would loose 30 happiness units by sitting next to Jody.
Irwin would gain 101 happiness units by sitting next to Carol.
Irwin would gain 499 happiness units by sitting next to Aligator.
Aligator would gain 999 happiness units by sitting next to Jody.
Aligator would gain 1500 happiness units by sitting next to Carol.
Aligator would loose 360 happiness units by sitting next to Irwin.
"""


class TestPart1(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part1(get_input(2015, 13)), 709)

    def test_example(self):
        self.assertEqual(part1(EXAMPLE), 330)

    def test_mock(self):
        self.assertEqual(part1(MOCK), 1682)


class TestPart2(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(part2(get_input(2015, 13)), 668)

    def test_example(self):
        self.assertEqual(part2(EXAMPLE), 286)

    def test_mock(self):
        self.assertEqual(part2(MOCK), 1812)


if __name__ == "__main__":  # pragma: no cover
    main()
