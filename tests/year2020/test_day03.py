#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2020/day/3
"""


from unittest import main, TestCase

from aoc.year2020.day03 import part1, part2
from data.utils import get_input


EXAMPLE = """..##.........##.........##.........##.........##.........##.......
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#
"""


class TestPart1(TestCase):
    def test_input(self):
        self.assertEqual(part1(get_input(2020, 3)), 207)

    def test_example(self):
        self.assertEqual(part1(EXAMPLE), 7)


class TestPart2(TestCase):
    def test_input(self):
        self.assertEqual(part2(get_input(2020, 3)), 2655892800)

    def test_example(self):
        self.assertEqual(part2(EXAMPLE), 336)


if __name__ == "__main__":  # pragma: no cover
    main()
