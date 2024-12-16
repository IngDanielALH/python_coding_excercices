import unittest
from transpose_matrix import transpose_matrix, son_matrices_iguales


class TestTransposeMatrix(unittest.TestCase):

    def test_1(self):
        test_matrix = [[1, 2]]
        expected = [[1],
                    [2]]
        self.assertTrue(son_matrices_iguales(transpose_matrix(test_matrix), expected))
