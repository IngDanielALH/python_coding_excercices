import unittest
from word_search import exist


class test_word_search(unittest.TestCase):
    def test_1(self):
        board = [["A", "B", "C", "E"],
                 ["S", "F", "C", "S"],
                 ["A", "D", "E", "E"]]
        word = "ABCCED"
        expected = True
        result = exist(board, word)
        self.assertEqual(expected, result)

    def test_2(self):
        board = [["A", "B", "C", "E"],
                 ["S", "F", "C", "S"],
                 ["A", "D", "E", "E"]]
        word = "SEE"
        expected = True
        result = exist(board, word)
        self.assertEqual(expected, result)

    def test_3(self):
        board = [["A", "B", "C", "E"],
                 ["S", "F", "C", "S"],
                 ["A", "D", "E", "E"]]
        word = "ABCB"
        expected = True
        result = exist(board, word)
        self.assertEqual(expected, result)
