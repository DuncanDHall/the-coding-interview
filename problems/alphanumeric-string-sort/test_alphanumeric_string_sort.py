import unittest
from alphanumeric_string_sort import *


class TestAlphanumericStringSort(unittest.TestCase):

    def test_sol(self):
        s0 = "gcgShwnPq5aG"
        s1 = "j3HMwGBu6Pxx"
        s2 = "GPpjDyuUCQpK"
        s3 = "12345"
        s4 = ""

        # sorted lowercase, sorted uppercase, sorted evens, sorted odds
        self.assertEqual("acgghnqwGPS5", alpha_num_sort(s0))
        self.assertEqual("juwxxBGHMP63", alpha_num_sort(s1))
        self.assertEqual("jppuyCDGKPQU", alpha_num_sort(s2))
        self.assertEqual("24135", alpha_num_sort(s3))
        self.assertEqual("", alpha_num_sort(s4))


if __name__ == '__main__':
    unittest.main()
