import unittest
from ice_cream_parlor import icecreamParlor


class TestIceCreamParlor(unittest.TestCase):

    def test_example_case(self):
        """Prueba el caso de ejemplo proporcionado en la descripción."""
        m = 6
        cost = [1, 3, 4, 5, 6]
        expected = [1, 4]
        result = icecreamParlor(m, cost)
        # Se ordena el resultado para asegurar que el orden no afecte el test
        self.assertEqual(sorted(result), expected)

    def test_pair_at_start(self):
        """Prueba un caso donde la solución está al inicio de la lista."""
        m = 8
        cost = [2, 6, 9, 1, 5]
        expected = [1, 2]
        result = icecreamParlor(m, cost)
        self.assertEqual(sorted(result), expected)

    def test_pair_at_end(self):
        """Prueba un caso donde la solución está al final de la lista."""
        m = 12
        cost = [1, 9, 3, 5, 7]
        expected = [4, 5]
        result = icecreamParlor(m, cost)
        self.assertEqual(sorted(result), expected)

    def test_duplicate_prices(self):
        """Prueba un caso importante: la solución requiere dos sabores con el mismo precio."""
        m = 4
        cost = [2, 8, 3, 2]
        expected = [1, 4]
        result = icecreamParlor(m, cost)
        self.assertEqual(sorted(result), expected)

    def test_large_numbers(self):
        """Prueba con valores más cercanos a los límites de los constraints."""
        m = 10000
        cost = [5000, 100, 200, 5000, 9000]
        expected = [1, 4]
        result = icecreamParlor(m, cost)
        self.assertEqual(sorted(result), expected)

    def test_minimum_values(self):
        """Prueba con los valores más pequeños posibles según los constraints."""
        m = 4
        cost = [2, 2]
        expected = [1, 2]
        result = icecreamParlor(m, cost)
        self.assertEqual(sorted(result), expected)