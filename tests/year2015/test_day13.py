# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/10
"""


from unittest import main, skip, TestCase

from aoc.year2015.day13 import a, b
from aoc.utils import get_input


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


class TestA(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(a(get_input(2015, 13)), 709)

    def test_example(self):
        self.assertEqual(a(EXAMPLE), 330)


class TestB(TestCase):
    @skip("Takes too long")
    def test_input(self):
        self.assertEqual(b(get_input(2015, 13)), 668)

    def test_example(self):
        self.assertEqual(b(EXAMPLE), 286)


if __name__ == "__main__":
    main()
