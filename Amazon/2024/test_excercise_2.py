import unittest
from excercise_2 import findRequestsInQueue


class TestExcercise2(unittest.TestCase):
    def test_1(self):
        requests = [2, 2, 3, 1]
        expected = [4, 2, 1, 0]
        self.assertEqual(expected, findRequestsInQueue(requests))

    def test_2(self):
        requests = [3, 1, 2, 1]
        expected = [4, 1, 0]
        self.assertEqual(expected, findRequestsInQueue(requests))

    def test_3(self):
        requests = [4, 4, 4]
        expected = [3, 2, 1, 0]
        self.assertEqual(expected, findRequestsInQueue(requests))
