import unittest
from branch_sums import branchSums
from utils import utils_for_test


class TestBranchSums(unittest.TestCase):
    def test_1(self):
        datos_arbol = {
            "nodes": [
                {"id": "1", "left": "2", "right": "3", "value": 1},
                {"id": "2", "left": "4", "right": "5", "value": 2},
                {"id": "3", "left": "6", "right": "7", "value": 3},
                {"id": "4", "left": "8", "right": "9", "value": 4},
                {"id": "5", "left": "10", "right": None, "value": 5},
                {"id": "6", "left": None, "right": None, "value": 6},
                {"id": "7", "left": None, "right": None, "value": 7},
                {"id": "8", "left": None, "right": None, "value": 8},
                {"id": "9", "left": None, "right": None, "value": 9},
                {"id": "10", "left": None, "right": None, "value": 10}
            ],
            "root": "1"
        }

        root = utils_for_test.build_tree(datos_arbol)
        expected = [15, 16, 18, 10, 11]
        self.assertEqual(expected, branchSums(root), "Las resultados no son iguales")
