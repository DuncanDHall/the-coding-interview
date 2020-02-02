#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy

# I'm being lazy and not copying the input
def bubble_sort(a):
    a = deepcopy(a)
    for cutoff in range(len(a)):
        for i in range(len(a) - cutoff - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
    return a
