import unittest
from transpose_matrix import transpose_matrix, son_matrices_iguales


class TestTransposeMatrix(unittest.TestCase):

    def test_1(self):
        test_matrix = [[1, 2]]
        expected = [[1],
                    [2]]
        self.assertTrue(son_matrices_iguales(transpose_matrix(test_matrix), expected))

    def test_2(self):
        test_matrix = [[1234, 6935, 4205],
                       [-23459, 314159, 0],
                       [100, 3, 987654]]

        expected = [[1234, -23459, 100],
                    [6935, 314159, 3],
                    [4205, 0, 987654]]
        self.assertTrue(son_matrices_iguales(transpose_matrix(test_matrix), expected))
