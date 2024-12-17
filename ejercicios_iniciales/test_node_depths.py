import unittest
from node_depths import nodeDepths
from utils import utils_for_test


class TestNodeDepths(unittest.TestCase):
    def test_closest_value_1(self):
        datos_arbol = {
            "tree": {
                "nodes": [
                    {"id": "1", "left": "2", "right": "3", "value": 1},
                    {"id": "2", "left": "4", "right": "5", "value": 2},
                    {"id": "3", "left": "6", "right": "7", "value": 3},
                    {"id": "4", "left": "8", "right": "9", "value": 4},
                    {"id": "5", "left": None, "right": None, "value": 5},
                    {"id": "6", "left": None, "right": None, "value": 6},
                    {"id": "7", "left": None, "right": None, "value": 7},
                    {"id": "8", "left": None, "right": None, "value": 8},
                    {"id": "9", "left": None, "right": None, "value": 9}
                ],
                "root": "1"
            }
        }

        root = utils_for_test.build_tree(datos_arbol["tree"])
        expected = 16
        resultado = nodeDepths(root)
        self.assertEqual(resultado, expected)
