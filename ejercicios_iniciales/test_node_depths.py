import unittest
from node_depths import nodeDepths
from utils import utils_for_test


class TestNodeDepths(unittest.TestCase):
    def test_node_depths_1(self):
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

    def test_node_depths_2(self):
        datos_arbol = {
            "tree": {
                "nodes": [
                    {"id": "1", "left": None, "right": None, "value": 1}
                ],
                "root": "1"
            }
        }

        root = utils_for_test.build_tree(datos_arbol["tree"])
        expected = 0
        resultado = nodeDepths(root)
        self.assertEqual(resultado, expected)

    def test_node_depths_3(self):
        datos_arbol = {
            "tree": {
                "nodes": [
                    {"id": "1", "left": "2", "right": None, "value": 1},
                    {"id": "2", "left": None, "right": None, "value": 2}
                ],
                "root": "1"
            }
        }

        root = utils_for_test.build_tree(datos_arbol["tree"])
        expected = 1
        resultado = nodeDepths(root)
        self.assertEqual(resultado, expected)

    def test_node_depths_4(self):
        datos_arbol = {
            "tree": {
                "nodes": [
                    {"id": "1", "left": "2", "right": "3", "value": 1},
                    {"id": "2", "left": None, "right": None, "value": 2},
                    {"id": "3", "left": None, "right": None, "value": 3}
                ],
                "root": "1"
            }
        }

        root = utils_for_test.build_tree(datos_arbol["tree"])
        expected = 2
        resultado = nodeDepths(root)
        self.assertEqual(resultado, expected)
