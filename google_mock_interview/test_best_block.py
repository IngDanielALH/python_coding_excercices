import unittest
from best_block import get_best_block


class test_best_block(unittest.TestCase):
    def test_1(self):
        blocks = [
            {
                "gym": False,
                "school": True,
                "store": False,
            },
            {
                "gym": True,
                "school": False,
                "store": False,
            },
            {
                "gym": True,
                "school": True,
                "store": False,
            },
            {
                "gym": False,
                "school": True,
                "store": False,
            },
            {
                "gym": False,
                "school": True,
                "store": True,
            }
        ]

        reqs = ["gym", "school", "store"]

        self.assertEqual(3, get_best_block(blocks, reqs))
