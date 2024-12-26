import unittest
from queries import process_queries


class TestProcessQueries(unittest.TestCase):
    def test_example_case(self):
        a = [3, 4]
        b = [1, 2, 3]
        queries = [[1, 5], [0, 0, 1], [1, 5]]
        expected_output = [2, 1]
        self.assertEqual(process_queries(a, b, queries), expected_output)

    def test_no_matches(self):
        a = [1, 2]
        b = [3, 4]
        queries = [[1, 10]]
        expected_output = [0]
        self.assertEqual(process_queries(a, b, queries), expected_output)

    def test_single_update(self):
        a = [1, 1]
        b = [1]
        queries = [[1, 2], [0, 1, 3], [1, 4]]
        expected_output = [2, 1]
        self.assertEqual(process_queries(a, b, queries), expected_output)

    def test_multiple_updates(self):
        a = [1, 2]
        b = [1, 2]
        queries = [[1, 3], [0, 1, 4], [1, 5]]
        expected_output = [2, 1]
        self.assertEqual(process_queries(a, b, queries), expected_output)
