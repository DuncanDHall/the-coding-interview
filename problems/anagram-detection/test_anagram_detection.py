import unittest
from my_anagram_detection import *


class TestAnagramDetection(unittest.TestCase):

    def test_sol_1(self):
        self.assertEqual(4, anagram_detector_1('AdnBndAndBdaBn', 'dAn'))
        self.assertEqual(2, anagram_detector_1('AbrAcadAbRa', 'cAda'))

    def test_permute(self):
        self.assertEqual(
            ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'],
            permute('abc')
        )

    def test_sol_2(self):
        self.assertEqual(4, anagram_detector_2('AdnBndAndBdaBn', 'dAn'))
        self.assertEqual(4, anagram_detector_2('AdnBndAndnBdaBn', 'dAn'))
        self.assertEqual(2, anagram_detector_2('AbrAcadAbRa', 'cAda'))

    def test_histogram_queue_A(self):
        hq = HistogramQueue()
        hq.push(1)
        hq.push(2)
        hq.push(2)
        hq.push(2)
        self.assertEqual(hq[2], 3)
        self.assertEqual(1, hq.pop())
        self.assertEqual(2, hq.pop())
        self.assertEqual(2, hq.pop())
        self.assertEqual(hq[2], 1)

    def test_histogram_queue_B(self):
        s = "averylongstringwithmultiplesofletters"
        hq = HistogramQueue(s)
        self.assertEqual(s.count("l"), hq["l"])
        self.assertEqual(s.count("t"), hq["t"])


if __name__ == '__main__':
    unittest.main()
