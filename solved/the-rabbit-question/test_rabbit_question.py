import unittest
from sol_rabbit_question import *


class TestRabbitQuestionSolution(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)

    def test_choose(self):
        self.assertEqual(choose(6, 3), 20)
        self.assertEqual(choose(10, 4), 210)

    def test_math(self):
        self.assertEqual(math_rabbit_question(4), 5)

    def test_recurse(self):
        self.assertEqual(recurse_rabbit_question(4), 5)

    def test_memoized_recurse(self):
        memo = {}
        self.assertEqual(memoized_recurse_rabbit_question(4, memo), 5)

    def test_dp(self):
        memo = {}
        self.assertEqual(dp_rabbit_question(1, memo), 1)
        self.assertEqual(dp_rabbit_question(2, memo), 2)
        self.assertEqual(dp_rabbit_question(3, memo), 3)
        self.assertEqual(dp_rabbit_question(4, memo), 5)


if __name__ == '__main__':
    unittest.main()
