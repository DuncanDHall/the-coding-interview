#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Balanced Brackets
#
#  Write a function that accepts a string consisting entiring of brackets
#  (`[](){}`) and returns whether it is balanced. Every "opening" bracket must
#  be followed by a closing bracket of the same type. There can also be nested
#  brackets, which adhere to the same rule.
#
#  ```js
#  f('()[]{}(([])){[()][]}') // true
#  f('())[]{}') // false
#  f('[(])') // false
#  ```

pairs = {
    "(": ")",
    "[": "]",
    "{": "}"
}


def sol1(s):
    stack = []
    for c in s:
        if c in pairs.keys():
            stack.append(c)
        else:
            if stack == [] or c != pairs[stack.pop()]:
                return False
    return stack == []
