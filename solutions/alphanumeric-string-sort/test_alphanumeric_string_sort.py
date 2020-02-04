import unittest
from my_alphanumeric_string_sort import *


class TestAlphanumericStringSort(unittest.TestCase):

    def setUp(self):
        self.s0 = "gcgShwnPq5aG"
        self.s1 = "j3HMwGBu6Pxx"
        self.s2 = "GPpjDyuUCQpK"
        self.s3 = "12345"
        self.s4 = ""

    def test_sol(self):
        # sorted lowercase, sorted uppercase, sorted evens, sorted odds
        self.assertEqual("acgghnqwGPS5", alpha_num_sort(self.s0))
        self.assertEqual("juwxxBGHMP63", alpha_num_sort(self.s1))
        self.assertEqual("jppuyCDGKPQU", alpha_num_sort(self.s2))
        self.assertEqual("24135", alpha_num_sort(self.s3))
        self.assertEqual("", alpha_num_sort(self.s4))

    def test_compare(self):
        self.assertTrue(compare_decorator("a") < compare_decorator("b"))
        self.assertTrue(compare_decorator("A") < compare_decorator("0"))
        self.assertTrue(compare_decorator("a") < compare_decorator("9"))
        self.assertTrue(compare_decorator("2") < compare_decorator("1"))

    def test_sol_2(self):
        # sorted lowercase, sorted uppercase, sorted evens, sorted odds
        self.assertEqual("acgghnqwGPS5", alpha_num_sort_2(self.s0))
        self.assertEqual("juwxxBGHMP63", alpha_num_sort_2(self.s1))
        self.assertEqual("jppuyCDGKPQU", alpha_num_sort_2(self.s2))
        self.assertEqual("24135", alpha_num_sort_2(self.s3))
        self.assertEqual("", alpha_num_sort_2(self.s4))


if __name__ == '__main__':
    unittest.main()
