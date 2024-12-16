import unittest
from transpose_matrix import transpose_matrix


class TestTransposeMatrix(unittest.TestCase):
    def son_matrices_iguales(matriz1, matriz2):
        if len(matriz1) != len(matriz2):  # Comparar número de filas
            return False
        for fila1, fila2 in zip(matriz1, matriz2):
            if fila1 != fila2:  # Comparar cada fila
                return False
        return True

    def test_1(self):
        test_matrix = [[1, 2]]
        expected = [[1],
                    [2]]
        self.assertTrue(self.son_matrices_iguales(transpose_matrix(test_matrix)), expected)
