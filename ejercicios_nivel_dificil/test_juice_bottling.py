import unittest
from JuiceBottling import juiceBottling


class testJuiceBottling(unittest.TestCase):
    def test_case_1(self):
        prices = [0, 2, 5, 6]
        expected = [1, 2]
        actual = juiceBottling(prices)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        prices = [0, 1, 3, 2, 4]
        expected = [2 , 2]
        actual = juiceBottling(prices)
        self.assertEqual(actual, expected)