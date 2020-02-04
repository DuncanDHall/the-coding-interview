#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from my_bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    def test_bubblesort(self):
        self.assertEqual(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            bubble_sort([6, 2, 3, 8, 5, 9, 4, 1, 0, 7])
        )
        self.assertEqual(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            bubble_sort([3, 6, 5, 1, 0, 4, 8, 9, 2, 7])
        )
        self.assertEqual(
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            bubble_sort([5, 4, 3, 9, 1, 8, 0, 7, 6, 2])
        )

    def test_empty(self):
        self.assertEqual([], bubble_sort([]))


if __name__ == '__main__':
    unittest.main(verbosity=2)
