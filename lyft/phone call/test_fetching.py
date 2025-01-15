import unittest
from fetching import ResultFetcher


class testFecher(unittest.TestCase):

    def setUp(self):
        self.fetcher = ResultFetcher()

    def test1(self):
        expected = list(range(5))
        output = self.fetcher.fetch(num_results=5)
        self.assertEqual(expected, output)

    def test2(self):
        expected = list(range(5, 7))
        self.fetcher.fetch(num_results=5)  # Populate the initial range
        output = self.fetcher.fetch(num_results=2)
        self.assertEqual(expected, output)

    def test3(self):
        expected = list(range(7, 14))
        self.fetcher.fetch(num_results=7)  # Populate up to 7 elements
        output = self.fetcher.fetch(num_results=7)
        self.assertEqual(expected, output)

    def test4(self):
        expected = list(range(14, 103))
        self.fetcher.fetch(num_results=14)  # Populate up to 14 elements
        output = self.fetcher.fetch(num_results=103 - 14)
        self.assertEqual(expected, output)

    def test5(self):
        expected = []
        self.fetcher.fetch(num_results=103)  # Consume all available elements
        output = self.fetcher.fetch(num_results=10)
        self.assertEqual(expected, output)

    def test6(self):
        self.fetcher = ResultFetcher()  # Reset fetcher
        expected = list(range(103))
        output = self.fetcher.fetch(num_results=200)
        self.assertEqual(expected, output)
