#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Binary Search Tree Check
#
#  Given a binary tree, check whether it’s a binary search tree or not.
#
# Source
#
#  [http://www.ardendertat.com/2011/10/10/programming-interview-questions-7-binary-search-tree-check/](http://www.ardendertat.com/2011/10/10/programming-interview-questions-7-binary-search-tree-check/)


class BinaryTree(object):
    """ A simple BT node """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def sol1(bt):
    stack = [bt]
    seen_or_none = {None}
    while stack:
        if stack[-1].left not in seen_or_none:
            stack.append(stack[-1].left)
        elif stack[-1].right not in seen_or_none:
            if stack[-1].value > stack[-1].right.value:
                return False
            seen_or_none.add(stack[-1])
            stack[-1] = stack[-1].right
        else:
            if len(stack) == 1:
                return True
            elif stack[-1].value > stack[-2].value:
                return False
            seen_or_none.add(stack[-1])
            stack.pop()
