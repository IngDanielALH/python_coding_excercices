import unittest
from calculate_password import calculate_changes


class testCalculatePassword(unittest.TestCase):
    def test_1(self):
        password = "abzzbz"
        k = 3
        expected = 1
        self.assertEqual(expected, calculate_changes(password, k))

    def test_2(self):
        password = "cbpecbbc"
        k = 4
        expected = 2
        self.assertEqual(expected, calculate_changes(password, k))

    def test_3(self):
        password = "vsvvsv"
        k = 3
        expected = 0
        self.assertEqual(expected, calculate_changes(password, k))

    def test_4(self):
        password = "raceeraceecaraceerac"
        k = 4
        expected = 11
        self.assertEqual(expected, calculate_changes(password, k))

    def test_5(self):
        password = "afzzbz"
        k = 3
        expected = 2
        self.assertEqual(expected, calculate_changes(password, k))




