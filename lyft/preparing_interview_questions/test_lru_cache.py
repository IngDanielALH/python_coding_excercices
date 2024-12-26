import unittest
import lru_cache


class test_lru_cache(unittest.TestCase):
    def test_1(self):
        # ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
        input = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
        expected = [None, None, None, 1, None, -1, None, -1, 3, 4]
