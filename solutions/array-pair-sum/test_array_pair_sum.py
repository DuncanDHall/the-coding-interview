import unittest
from my_array_pair_sum import *

from copy import deepcopy


class TestArrayPairSum(unittest.TestCase):

    def test_answer_tester(self):
        self.assertTrue(self.answer_tester(
            [[6, 4], [7, 3], [6, 4]],
            [[7, 3], [4, 6], [4, 6]]
        ))
        self.assertTrue(self.answer_tester(
            [[6, 4], [7, 3]],
            [[7, 3], [4, 6]]
        ))

    def test_sol1(self):
        self.assertTrue(self.answer_tester(
                [ [6, 4], [7, 3] ],
                sol1(10, [3, 4, 5, 6, 7])
        ))
        self.assertTrue(self.answer_tester(
                [ [3, 5], [4, 4] ],
                sol1(8, [3, 4, 5, 4, 4])
        ))

    def test_sol2(self):
        self.assertTrue(self.answer_tester(
                [ [6, 4], [7, 3] ],
                sol2(10, [3, 4, 5, 6, 7])
        ))
        self.assertTrue(self.answer_tester(
                [ [3, 5], [4, 4] ],
                sol2(8, [3, 4, 5, 4, 4])
        ))

    # for our purposes, sorting in O(n*log(n)) is fine
    # for our purposes, sorting in O(n*log(n)) is fine
    def answer_tester(self, a, b):
        #  breakpoint()
        aa = deepcopy(a)
        bb = deepcopy(b)
        for l in [aa, bb]:
            for li in l:
                li.sort()
            l.sort()
        if aa != bb:
            print("failed answer test")
            print("expected: ", a)
            print("got:      ", b)
        return aa == bb



if __name__ == '__main__':
    unittest.main()

