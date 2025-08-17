import unittest
from number_of_islands import num_islands


class test_num_islands(unittest.TestCase):
    def test_1(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        expected = 3
        result = num_islands(grid)
        self.assertEqual(expected, result)

    def test_2(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        expected = 1
        result = num_islands(grid)
        self.assertEqual(expected, result)

    def test_empty_grid(self):
        """Prueba un caso borde importante: una matriz vacía."""
        grid = []
        self.assertEqual(num_islands(grid), 0)

    def test_all_water(self):
        """Prueba un mapa que es pura agua."""
        grid = [
            ['0', '0', '0'],
            ['0', '0', '0']
        ]
        self.assertEqual(num_islands(grid), 0)

    def test_all_land(self):
        """Prueba un mapa que es una sola isla gigante."""
        grid = [
            ['1', '1', '1'],
            ['1', '1', '1']
        ]
        self.assertEqual(num_islands(grid), 1)

    def test_provided_example(self):
        """Prueba el ejemplo original con 3 islas."""
        grid = [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']
        ]
        # Hacemos una copia para no modificar el original entre tests
        grid_copy = [row[:] for row in grid]
        self.assertEqual(num_islands(grid_copy), 3)

    def test_diagonal_islands(self):
        """Verifica que la conexión diagonal NO cuenta como una sola isla."""
        grid = [
            ['1', '0', '1'],
            ['0', '1', '0'],
            ['1', '0', '1']
        ]
        self.assertEqual(num_islands(grid), 5)

    def test_complex_shape_island(self):
        """Prueba una isla con una forma compleja para retar al BFS."""
        grid = [
            ['1', '1', '1', '1', '0'],
            ['1', '0', '0', '1', '0'],
            ['1', '1', '1', '1', '0'],
            ['0', '1', '0', '0', '0'],
            ['0', '1', '1', '1', '1']
        ]
        grid_copy = [row[:] for row in grid]
        self.assertEqual(num_islands(grid_copy), 1)

    def test_line_islands(self):
        """Prueba islas que son solo líneas verticales y horizontales."""
        grid = [
            ['1', '0', '0', '1', '1'],
            ['1', '0', '1', '0', '0'],
            ['1', '0', '1', '0', '1']
        ]
        grid_copy = [row[:] for row in grid]
        self.assertEqual(num_islands(grid_copy), 4)
