# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/4
"""


from unittest import main, TestCase

from aoc.year2016.day4 import a, b
from aoc.utils import get_input


EXAMPLE_1 = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
"""

EXAMPLE_2 = """qzmt-zixmtkozy-ivhz-343[zimth]
"""


class TestA(TestCase):
    def test_input(self):
        self.assertEqual(a(get_input(2016, 4)), 361724)

    def test_example_1(self):
        self.assertEqual(a(EXAMPLE_1), 1514)

    def test_example_2(self):
        self.assertEqual(a(EXAMPLE_2), 343)


class TestB(TestCase):
    def test_input(self):
        self.assertEqual(b(get_input(2016, 4)), 482)

    def test_example_1(self):
        self.assertEqual(b(EXAMPLE_1, "z a b c d e f g"), 987)

    def test_example_2(self):
        self.assertEqual(b(EXAMPLE_2, "very encrypted name"), 343)


if __name__ == "__main__":
    main()
