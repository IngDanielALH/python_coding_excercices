import unittest
from coloreando_regiones import flood_fill  # Asegúrate de que el archivo anterior se llame flood_fill.py


class TestFloodFill(unittest.TestCase):

    def test_basic_fill(self):
        print("\nProbando un relleno básico...")
        image = [
            [1, 1, 1, 0],
            [1, 1, 0, 0],
            [1, 0, 1, 1],
            [2, 2, 2, 2]
        ]
        expected = [
            [8, 8, 8, 0],
            [8, 8, 0, 0],
            [8, 0, 1, 1],
            [2, 2, 2, 2]
        ]
        result = flood_fill(image, 1, 1, 8)
        self.assertEqual(result, expected)

    def test_fill_to_edge(self):
        print("Probando un relleno que llega a los bordes...")
        image = [
            [0, 0, 0],
            [0, 1, 1],
            [0, 1, 1]
        ]
        expected = [
            [0, 0, 0],
            [0, 5, 5],
            [0, 5, 5]
        ]
        result = flood_fill(image, 1, 1, 5)
        self.assertEqual(result, expected)

    def test_start_on_already_filled_color(self):
        print("Probando iniciar en un píxel que ya tiene el nuevo color...")
        image = [
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3]
        ]
        # Hacemos una copia para asegurar que la función no modifica la imagen
        image_copy = [row[:] for row in image]
        result = flood_fill(image, 1, 1, 2)
        self.assertEqual(result, image_copy, "La imagen no debería cambiar.")

    def test_fill_entire_image(self):
        print("Probando rellenar una imagen completa...")
        image = [
            [3, 3, 3],
            [3, 3, 3],
            [3, 3, 3]
        ]
        expected = [
            [9, 9, 9],
            [9, 9, 9],
            [9, 9, 9]
        ]
        result = flood_fill(image, 0, 0, 9)
        self.assertEqual(result, expected)

    def test_complex_shape(self):
        print("Probando una forma más compleja...")
        image = [
            [4, 4, 0, 4, 4],
            [0, 4, 4, 4, 0],
            [0, 4, 0, 4, 0],
            [0, 4, 4, 4, 0],
            [4, 4, 0, 4, 4]
        ]
        expected = [
            [4, 4, 0, 4, 4],
            [0, 7, 7, 7, 0],
            [0, 7, 0, 7, 0],
            [0, 7, 7, 7, 0],
            [4, 4, 0, 4, 4]
        ]
        result = flood_fill(image, 2, 1, 7)
        self.assertEqual(result, expected)
