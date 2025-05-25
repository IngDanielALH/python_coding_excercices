import unittest
from social_network import get_connections


class test_social_network(unittest.TestCase):
    def test_1(self):
        u = [1, 2, 3, 5]
        v = [2, 3, 4, 6]
        queries = [1, 3, 5, 7]
        nodes = 7
        expected = [4, 4, 2, 1]
        self.assertEqual(expected, get_connections(u, v, nodes, queries))

    def test_2(self):
        u = [2, 2, 1, 1]
        v = [1, 3, 3, 4]
        queries = [4, 2, 5]
        nodes = 5
        expected = [4, 4, 1]
        self.assertEqual(expected, get_connections(u, v, nodes, queries))

    def test_3(self):
        u = [1, 2, 1, 4, 5, 4]
        v = [2, 3, 3, 5, 6, 6]
        queries = [4, 2, 5]
        nodes = 6
        expected = [3, 3, 3]
        self.assertEqual(expected, get_connections(u, v, nodes, queries))
