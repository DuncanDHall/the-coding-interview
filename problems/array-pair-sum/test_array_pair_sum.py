import unittest
from array_pair_sum import *


class TestArrayPairSum(unittest.TestCase):

    def test_answer_tester(self):
        self.assertTrue(self.answer_tester(
            [[6, 4], [7, 3], [6, 4]]
            [[7, 3], [4, 6], [4, 6]]
        ))
        self.assertTrue(self.answer_tester(
            [[6, 4], [7, 3]],
            [[7, 3], [4, 6]]
        ))

    def test_sol1(self):
        self.assertEqual(
                [ [6, 4], [7, 3] ],
                sol1(10, [3, 4, 5, 6, 7])
        )
        self.assertEqual(
                [ [3, 5], [4, 4], [4, 4], [4, 4] ],
                sol1(8, [3, 4, 5, 4, 4])
        )

    def answer_tester(self, a, b):
        #  breakpoint()
        b_set = set([tuple(bb) for bb in b])
        for item in a:
            if tuple(item) in b_set:
                b_set.discard(tuple(item))
                continue
            elif tuple(reversed(item)) in b_set:
                b_set.discard(tuple(reversed(item)))
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    unittest.main()

