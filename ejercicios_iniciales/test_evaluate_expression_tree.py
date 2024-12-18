import unittest
from evaluate_expression_tree import evaluateExpressionTree
from utils import utils_for_test


class TestEvaluateExpressionTree(unittest.TestCase):
    def test_evaluate_expression_tree_1(self):
        datos_arbol = {
            "tree": {
                "nodes": [
                    {"id": "1", "left": "2", "right": "3", "value": -1},
                    {"id": "2", "left": None, "right": None, "value": 2},
                    {"id": "3", "left": None, "right": None, "value": 3}
                ],
                "root": "1"
            }
        }

        root = utils_for_test.build_tree(datos_arbol["tree"])
        target = 5
        resultado = evaluateExpressionTree(root)
        self.assertEqual(resultado, target)

    def test_evaluate_expression_tree_2(self):
        datos_arbol = {
            "tree": {
                "nodes": [
                    {"id": "1", "left": "2", "right": "3", "value": -2},
                    {"id": "2", "left": None, "right": None, "value": 2},
                    {"id": "3", "left": None, "right": None, "value": 3}
                ],
                "root": "1"
            }
        }

        root = utils_for_test.build_tree(datos_arbol["tree"])
        target = -1
        resultado = evaluateExpressionTree(root)
        self.assertEqual(resultado, target)

    def test_evaluate_expression_tree_3(self):
        datos_arbol = {
            "tree": {
                "nodes": [
                    {"id": "1", "left": "3", "right": "2", "value": -2},
                    {"id": "2", "left": None, "right": None, "value": 2},
                    {"id": "3", "left": None, "right": None, "value": 3}
                ],
                "root": "1"
            }
        }

        root = utils_for_test.build_tree(datos_arbol["tree"])
        target = 1
        resultado = evaluateExpressionTree(root)
        self.assertEqual(resultado, target)
