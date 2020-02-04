#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from copy import deepcopy

from my_binary_search_tree_check import BinaryTree, sol1


class TestBinarySearchTreeCheck(unittest.TestCase):
    def setUp(self):
        self.bst = BinaryTree(
            15,
            BinaryTree(
                10,
                BinaryTree(8),
                BinaryTree(12)
            ),
            BinaryTree(
                20,
                BinaryTree(16),
                BinaryTree(25)
            )
        )
        self.bt = BinaryTree(
            15,
            BinaryTree(
                10,
                BinaryTree(5),
                BinaryTree(16)
            ),
            BinaryTree(20)
        )

    def test_tree(self):
        self.assertEqual(15, self.bt.value)
        self.assertEqual(16, self.bst.right.left.value)

    def test_tree_mod(self):
        bt = deepcopy(self.bt)
        bt.right.left = BinaryTree(13)
        bt.right.right = BinaryTree(40)
        self.assertEqual(13, bt.right.left.value)
        self.assertEqual(40, bt.right.right.value)

    def test_sol1(self):
        self.assertEqual(True, sol1(self.bst))
        self.assertEqual(False, sol1(self.bt))


if __name__ == '__main__':
    unittest.main(verbosity=2)
