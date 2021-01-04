# -*- coding: utf-8 -*-
"""
https://adventofcode.com/2015/day/4
"""


from unittest import TestCase, main, skip


from aoc.year2015.day4 import ab
from aoc.utils import get_input


class TestAB(TestCase):
    def test_input_a(self):
        self.assertEqual(ab(get_input(2015, 4), '00000'), 346386)
    
    @skip('takes too long')
    def test_example_1(self):
        self.assertEqual(ab('abcdef', '00000'), 609043)
    
    @skip('takes too long')
    def test_example_2(self):
        self.assertEqual(ab('pqrstuv', '00000'), 1048970)
    
    @skip('takes too long')
    def test_input_b(self):
        self.assertEqual(ab(get_input(2015, 4), '000000'), 9958218)


if __name__ == '__main__':
    main()