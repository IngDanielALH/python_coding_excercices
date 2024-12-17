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

    def test_closest_value_2(self):
        datos_arbol = {
            "nodes": [
                {"id": "100", "left": "5", "right": "502", "value": 100},
                {"id": "502", "left": "204", "right": "55000", "value": 502},
                {"id": "55000", "left": "1001", "right": None, "value": 55000},
                {"id": "1001", "left": None, "right": "4500", "value": 1001},
                {"id": "4500", "left": None, "right": None, "value": 4500},
                {"id": "204", "left": "203", "right": "205", "value": 204},
                {"id": "205", "left": None, "right": "207", "value": 205},
                {"id": "207", "left": "206", "right": "208", "value": 207},
                {"id": "208", "left": None, "right": None, "value": 208},
                {"id": "206", "left": None, "right": None, "value": 206},
                {"id": "203", "left": None, "right": None, "value": 203},
                {"id": "5", "left": "2", "right": "15", "value": 5},
                {"id": "15", "left": "5-2", "right": "22", "value": 15},
                {"id": "22", "left": None, "right": "57", "value": 22},
                {"id": "57", "left": None, "right": "60", "value": 57},
                {"id": "60", "left": None, "right": None, "value": 60},
                {"id": "5-2", "left": None, "right": None, "value": 5},
                {"id": "2", "left": "1", "right": "3", "value": 2},
                {"id": "3", "left": None, "right": None, "value": 3},
                {"id": "1", "left": "-51", "right": "1-2", "value": 1},
                {"id": "1-2", "left": None, "right": "1-3", "value": 1},
                {"id": "1-3", "left": None, "right": "1-4", "value": 1},
                {"id": "1-4", "left": None, "right": "1-5", "value": 1},
                {"id": "1-5", "left": None, "right": None, "value": 1},
                {"id": "-51", "left": "-403", "right": None, "value": -51},
                {"id": "-403", "left": None, "right": None, "value": -403}
            ],
            "root": "100"
        }

        root = construir_arbol(datos_arbol)
        target = 100
        resultado = find_closest_value_in_bst(root, target)
        self.assertEqual(resultado, 100)

    def test_closest_value_3(self):
        datos_arbol = {
            "nodes": [
                {"id": "100", "left": "5", "right": "502", "value": 100},
                {"id": "502", "left": "204", "right": "55000", "value": 502},
                {"id": "55000", "left": "1001", "right": None, "value": 55000},
                {"id": "1001", "left": None, "right": "4500", "value": 1001},
                {"id": "4500", "left": None, "right": None, "value": 4500},
                {"id": "204", "left": "203", "right": "205", "value": 204},
                {"id": "205", "left": None, "right": "207", "value": 205},
                {"id": "207", "left": "206", "right": "208", "value": 207},
                {"id": "208", "left": None, "right": None, "value": 208},
                {"id": "206", "left": None, "right": None, "value": 206},
                {"id": "203", "left": None, "right": None, "value": 203},
                {"id": "5", "left": "2", "right": "15", "value": 5},
                {"id": "15", "left": "5-2", "right": "22", "value": 15},
                {"id": "22", "left": None, "right": "57", "value": 22},
                {"id": "57", "left": None, "right": "60", "value": 57},
                {"id": "60", "left": None, "right": None, "value": 60},
                {"id": "5-2", "left": None, "right": None, "value": 5},
                {"id": "2", "left": "1", "right": "3", "value": 2},
                {"id": "3", "left": None, "right": None, "value": 3},
                {"id": "1", "left": "-51", "right": "1-2", "value": 1},
                {"id": "1-2", "left": None, "right": "1-3", "value": 1},
                {"id": "1-3", "left": None, "right": "1-4", "value": 1},
                {"id": "1-4", "left": None, "right": "1-5", "value": 1},
                {"id": "1-5", "left": None, "right": None, "value": 1},
                {"id": "-51", "left": "-403", "right": None, "value": -51},
                {"id": "-403", "left": None, "right": None, "value": -403}
            ],
            "root": "100"
        }

        root = construir_arbol(datos_arbol)
        target = 208
        resultado = find_closest_value_in_bst(root, target)
        self.assertEqual(resultado, 208)

    def test_closest_value_4(self):
        datos_arbol = {
            "nodes": [
                {"id": "100", "left": "5", "right": "502", "value": 100},
                {"id": "502", "left": "204", "right": "55000", "value": 502},
                {"id": "55000", "left": "1001", "right": None, "value": 55000},
                {"id": "1001", "left": None, "right": "4500", "value": 1001},
                {"id": "4500", "left": None, "right": None, "value": 4500},
                {"id": "204", "left": "203", "right": "205", "value": 204},
                {"id": "205", "left": None, "right": "207", "value": 205},
                {"id": "207", "left": "206", "right": "208", "value": 207},
                {"id": "208", "left": None, "right": None, "value": 208},
                {"id": "206", "left": None, "right": None, "value": 206},
                {"id": "203", "left": None, "right": None, "value": 203},
                {"id": "5", "left": "2", "right": "15", "value": 5},
                {"id": "15", "left": "5-2", "right": "22", "value": 15},
                {"id": "22", "left": None, "right": "57", "value": 22},
                {"id": "57", "left": None, "right": "60", "value": 57},
                {"id": "60", "left": None, "right": None, "value": 60},
                {"id": "5-2", "left": None, "right": None, "value": 5},
                {"id": "2", "left": "1", "right": "3", "value": 2},
                {"id": "3", "left": None, "right": None, "value": 3},
                {"id": "1", "left": "-51", "right": "1-2", "value": 1},
                {"id": "1-2", "left": None, "right": "1-3", "value": 1},
                {"id": "1-3", "left": None, "right": "1-4", "value": 1},
                {"id": "1-4", "left": None, "right": "1-5", "value": 1},
                {"id": "1-5", "left": None, "right": None, "value": 1},
                {"id": "-51", "left": "-403", "right": None, "value": -51},
                {"id": "-403", "left": None, "right": None, "value": -403}
            ],
            "root": "100"
        }

        root = construir_arbol(datos_arbol)
        target = 4500
        resultado = find_closest_value_in_bst(root, target)
        self.assertEqual(resultado, 4500)

    def test_closest_value_6(self):
        datos_arbol = {
            "nodes": [
                {"id": "100", "left": "5", "right": "502", "value": 100},
                {"id": "502", "left": "204", "right": "55000", "value": 502},
                {"id": "55000", "left": "1001", "right": None, "value": 55000},
                {"id": "1001", "left": None, "right": "4500", "value": 1001},
                {"id": "4500", "left": None, "right": None, "value": 4500},
                {"id": "204", "left": "203", "right": "205", "value": 204},
                {"id": "205", "left": None, "right": "207", "value": 205},
                {"id": "207", "left": "206", "right": "208", "value": 207},
                {"id": "208", "left": None, "right": None, "value": 208},
                {"id": "206", "left": None, "right": None, "value": 206},
                {"id": "203", "left": None, "right": None, "value": 203},
                {"id": "5", "left": "2", "right": "15", "value": 5},
                {"id": "15", "left": "5-2", "right": "22", "value": 15},
                {"id": "22", "left": None, "right": "57", "value": 22},
                {"id": "57", "left": None, "right": "60", "value": 57},
                {"id": "60", "left": None, "right": None, "value": 60},
                {"id": "5-2", "left": None, "right": None, "value": 5},
                {"id": "2", "left": "1", "right": "3", "value": 2},
                {"id": "3", "left": None, "right": None, "value": 3},
                {"id": "1", "left": "-51", "right": "1-2", "value": 1},
                {"id": "1-2", "left": None, "right": "1-3", "value": 1},
                {"id": "1-3", "left": None, "right": "1-4", "value": 1},
                {"id": "1-4", "left": None, "right": "1-5", "value": 1},
                {"id": "1-5", "left": None, "right": None, "value": 1},
                {"id": "-51", "left": "-403", "right": None, "value": -51},
                {"id": "-403", "left": None, "right": None, "value": -403}
            ],
            "root": "100"
        }

        root = construir_arbol(datos_arbol)
        target = -70
        resultado = find_closest_value_in_bst(root, target)
        self.assertEqual(resultado, -51)

    def test_closest_value_7(self):
        datos_arbol = {
            "nodes": [
                {"id": "100", "left": "5", "right": "502", "value": 100},
                {"id": "502", "left": "204", "right": "55000", "value": 502},
                {"id": "55000", "left": "1001", "right": None, "value": 55000},
                {"id": "1001", "left": None, "right": "4500", "value": 1001},
                {"id": "4500", "left": None, "right": None, "value": 4500},
                {"id": "204", "left": "203", "right": "205", "value": 204},
                {"id": "205", "left": None, "right": "207", "value": 205},
                {"id": "207", "left": "206", "right": "208", "value": 207},
                {"id": "208", "left": None, "right": None, "value": 208},
                {"id": "206", "left": None, "right": None, "value": 206},
                {"id": "203", "left": None, "right": None, "value": 203},
                {"id": "5", "left": "2", "right": "15", "value": 5},
                {"id": "15", "left": "5-2", "right": "22", "value": 15},
                {"id": "22", "left": None, "right": "57", "value": 22},
                {"id": "57", "left": None, "right": "60", "value": 57},
                {"id": "60", "left": None, "right": None, "value": 60},
                {"id": "5-2", "left": None, "right": None, "value": 5},
                {"id": "2", "left": "1", "right": "3", "value": 2},
                {"id": "3", "left": None, "right": None, "value": 3},
                {"id": "1", "left": "-51", "right": "1-2", "value": 1},
                {"id": "1-2", "left": None, "right": "1-3", "value": 1},
                {"id": "1-3", "left": None, "right": "1-4", "value": 1},
                {"id": "1-4", "left": None, "right": "1-5", "value": 1},
                {"id": "1-5", "left": None, "right": None, "value": 1},
                {"id": "-51", "left": "-403", "right": None, "value": -51},
                {"id": "-403", "left": None, "right": None, "value": -403}
            ],
            "root": "100"
        }

        root = construir_arbol(datos_arbol)
        target = 2000
        resultado = find_closest_value_in_bst(root, target)
        self.assertEqual(resultado, 1001)
