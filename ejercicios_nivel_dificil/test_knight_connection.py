# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

from knights_connection import knight_connection
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        knightA = [0, 0]
        knightB = [2, 1]
        expected = 1
        actual = knight_connection(knightA, knightB)
        self.assertEqual(actual, expected)
