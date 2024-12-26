import unittest
from trapping_rain_water import trap


class test_trapping_rain_water(unittest.TestCase):
    def test_1(self):
        heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        expected = 6
        result = trap(heights)
        self.assertEqual(expected, result)

    def test_2(self):
        heights = [4, 2, 0, 3, 2, 5]
        expected = 9
        result = trap(heights)
        self.assertEqual(expected, result)
