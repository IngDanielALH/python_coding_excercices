import unittest
from find_closest_value_in_bst import find_closest_value_in_bst, construir_arbol


class TestFindClosestValueInBST(unittest.TestCase):

    def test_closest_value_1(self):
        datos_arbol = {
                "nodes": [
                    {"id": "10", "left": "5", "right": "15", "value": 10},
                    {"id": "15", "left": "13", "right": "22", "value": 15},
                    {"id": "22", "left": None, "right": None, "value": 22},
                    {"id": "13", "left": None, "right": "14", "value": 13},
                    {"id": "14", "left": None, "right": None, "value": 14},
                    {"id": "5", "left": "2", "right": "5-2", "value": 5},
                    {"id": "5-2", "left": None, "right": None, "value": 5},
                    {"id": "2", "left": "1", "right": None, "value": 2},
                    {"id": "1", "left": None, "right": None, "value": 1}
                ],
                "root": "10"
            }

        root = construir_arbol(datos_arbol)
        target = 12
        resultado = find_closest_value_in_bst(root, target)
        self.assertEqual(resultado, 13)
