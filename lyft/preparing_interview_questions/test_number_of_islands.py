import unittest
from number_of_islands import num_islands


class test_num_islands(unittest.TestCase):
    def test_1(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        expected = 3
        result = num_islands(grid)
        self.assertEqual(expected, result)

    def test_2(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        expected = 1
        result = num_islands(grid)
        self.assertEqual(expected, result)
