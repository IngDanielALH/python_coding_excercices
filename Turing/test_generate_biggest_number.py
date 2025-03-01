import unittest
from create_biggest_number import generate_biggest_number


class test_biggest_number(unittest.TestCase):
    def test_1(self):
        array = "3391933"
        expected = "9933313"
        k = 3
        self.assertEqual(expected, generate_biggest_number(array, k))

    def test_2(self):
        array = "339193399993"
        expected = "999399933313"
        k = 3
        self.assertEqual(expected, generate_biggest_number(array, k))

    def test_3(self):
        array = "999999888887777666554"
        expected = "998998998878776766554"
        k = 2
        self.assertEqual(expected, generate_biggest_number(array, k))
