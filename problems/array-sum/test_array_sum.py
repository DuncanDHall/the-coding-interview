import unittest
from my_array_sum import *


class TestArraySum(unittest.TestCase):

    def test_recursive_sol(self):
        self.assertEqual(15, recursive_sol([1,2,[3,4,[5]]]))

    def test_str_hack(self):
        self.assertEqual(15, str_hack([1,2,[3,4,[5]]]))

    def test_as_you_go(self):
        self.assertEqual(15, as_you_go([1,2,[3,4,[5]]]))


if __name__ == '__main__':
    unittest.main()
