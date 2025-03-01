import unittest
from create_biggest_number import generate_biggest_number


class test_biggest_number(unittest.TestCase):
    def test_1(self):
        array = "3391933"
        expected = "9933313"
        k = 3
        self.assertEqual(expected, generate_biggest_number(array, k))
