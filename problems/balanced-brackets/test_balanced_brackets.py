#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from my_balanced_brackets import sol1


class TestBalancedBrackets(unittest.TestCase):
    def test_sol1_a(self):
        self.assertEqual(True, sol1('()[]{}(([])){[()][]}'))

    def test_sol1_b(self):
        self.assertEqual(False, sol1('())[]{}'))

    def test_sol1_c(self):
        self.assertEqual(False, sol1('[(])'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
