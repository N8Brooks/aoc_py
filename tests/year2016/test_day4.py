# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2016/day/4
"""


from unittest import main, TestCase

from aoc.year2016.day4 import part1, part2
from data.utils import get_input


EXAMPLE_1 = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
"""

EXAMPLE_2 = """qzmt-zixmtkozy-ivhz-343[zimth]
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2016, 4)), 361724)

    def test_example_1(self):
        self.assertEqual(part1(EXAMPLE_1), 1514)

    def test_example_2(self):
        self.assertEqual(part1(EXAMPLE_2), 343)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2016, 4)), 482)

    def test_example_1(self):
        self.assertEqual(part2(EXAMPLE_1, "z a b c d e f g"), 987)

    def test_example_2(self):
        self.assertEqual(part2(EXAMPLE_2, "very encrypted name"), 343)


if __name__ == "__main__":
    main()
