import unittest
from lyfts_queries import matchingStrings


class TestMatchingStrings(unittest.TestCase):

    def test_example_case(self):
        strings = ['ab', 'ab', 'abc']
        queries = ['ab', 'abc', 'bc']
        expected = [2, 1, 0]
        self.assertEqual(matchingStrings(strings, queries), expected)

    def test_empty_strings(self):
        strings = []
        queries = ['a', 'b', 'c']
        expected = [0, 0, 0]
        self.assertEqual(matchingStrings(strings, queries), expected)

    def test_empty_queries(self):
        strings = ['x', 'y', 'z']
        queries = []
        expected = []
        self.assertEqual(matchingStrings(strings, queries), expected)

    def test_duplicates_and_overlapping_queries(self):
        strings = ['apple', 'banana', 'apple', 'apple', 'orange']
        queries = ['apple', 'banana', 'grape', 'orange']
        expected = [3, 1, 0, 1]
        self.assertEqual(matchingStrings(strings, queries), expected)

    def test_case_sensitivity(self):
        strings = ['a', 'A', 'a']
        queries = ['a', 'A']
        expected = [2, 1]
        self.assertEqual(matchingStrings(strings, queries), expected)

    def test_large_input(self):
        strings = ['test'] * 1000
        queries = ['test', 'nope']
        expected = [1000, 0]
        self.assertEqual(matchingStrings(strings, queries), expected)
