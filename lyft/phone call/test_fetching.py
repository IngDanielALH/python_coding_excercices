import unittest
from fetching import ResultFetcher


class TestFetcher(unittest.TestCase):

    def setUp(self):
        self.fetcher = ResultFetcher()

    def test1(self):
        expected = list(range(5))
        output = self.fetcher.fetch(num_results = 5)
        self.assertEqual(expected, output)

    def test2(self):
        expected = list(range(5, 7))
        output = self.fetcher.fetch(num_results = 2)
        self.assertEqual(expected, output)

    def test3(self):
        expected = list(range(7, 14))
        output = self.fetcher.fetch(num_results = 7)
        self.assertEqual(expected, output)

    def test4(self):
        expected = list(range(14, 103))
        output = self.fetcher.fetch(num_results = 103)
        self.assertEqual(expected, output)

    def test5(self):
        expected = []
        output = self.fetcher.fetch(num_results = 10)
        self.assertEqual(expected, output)
