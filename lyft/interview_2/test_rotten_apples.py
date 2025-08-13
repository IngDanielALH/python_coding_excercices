import unittest
from rotten_apples import calculate_steps


class test_rotten_apples(unittest.TestCase):
    def test_1(self):
        box = [[2, 1, 1],
               [1, 1, 0],
               [0, 1, 1]]
        expected = 4
        self.assertEqual(expected, calculate_steps(box))
        pass


    def test_2(self):
        box = [[1, 1, 1],
             [1, 2, 1],
             [1, 1, 1]]
        expected = 2
        self.assertEqual(expected, calculate_steps(box))
        pass
