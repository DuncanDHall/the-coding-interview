#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from my_atbash import encode, decode


class TestAtBash(unittest.TestCase):
    def test_encode(self):
        self.assertEqual('gsrh rh vmxlwvw', encode('this is encoded'))

    def test_decode(self):
        self.assertEqual('this is decoded', decode('gsrh rh wvxlwvw'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
