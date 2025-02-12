import random
import unittest
from excercise_2 import findRequestsInQueue


class TestExcercise2(unittest.TestCase):
    def test_1(self):
        requests = [2, 2, 3, 1]
        expected = [4, 2, 1, 0]
        self.assertEqual(expected, findRequestsInQueue(requests))

    def test_2(self):
        requests = [3, 1, 2, 1]
        expected = [4, 1, 0]
        self.assertEqual(expected, findRequestsInQueue(requests))

    def test_3(self):
        requests = [4, 4, 4]
        expected = [3, 2, 1, 0]
        self.assertEqual(expected, findRequestsInQueue(requests))

    def test_4(self):
        requests = [1, 1, 1, 1]
        expected = [4, 0]
        self.assertEqual(expected, findRequestsInQueue(requests))

    def test_5(self):
        requests = [5, 3, 2, 1, 4]
        expected = [5, 3, 2, 1, 0]
        self.assertEqual(expected, findRequestsInQueue(requests))

    def test_6(self):
        requests = [2, 3, 1, 5, 4]
        expected = [5, 3, 2, 1, 0]
        self.assertEqual(expected, findRequestsInQueue(requests))

    def test_7(self):
        requests = [2, 2, 2, 2]
        expected = [4, 2, 0]
        self.assertEqual(expected, findRequestsInQueue(requests))

    def test_large_n(self):
        """Caso con el número máximo de requests (n=100000) con valores aleatorios dentro del rango permitido."""
        requests = [random.randint(1, 100000) for _ in range(100000)]
        result = findRequestsInQueue(requests)
        self.assertIsInstance(result, list)  # Solo verificamos que se complete sin errores

    def test_large_wait(self):
        """Caso donde todas las requests tienen el máximo tiempo de espera posible (100000)."""
        requests = [100000] * 100000
        result = findRequestsInQueue(requests)
        self.assertIsInstance(result, list)  # Verificamos que se complete sin errores

    def test_min_n_max_wait(self):
        """Caso con n=1 y el máximo tiempo de espera."""
        requests = [100000]
        expected = [1, 0]  # La única request se procesa y luego la cola queda vacía
        self.assertEqual(expected, findRequestsInQueue(requests))

    def test_max_n_min_wait(self):
        """Caso con el máximo número de requests pero con tiempo mínimo de espera (1)."""
        requests = [1] * 100000
        expected = [i for i in range(100000, 0, -1)] + [0]  # La cola se vacía uno por uno
        self.assertEqual(expected, findRequestsInQueue(requests))

    def test_alternating_values(self):
        """Caso con valores alternados de tiempo de espera (1 y 100000)."""
        requests = [1 if i % 2 == 0 else 100000 for i in range(100000)]
        result = findRequestsInQueue(requests)
        self.assertIsInstance(result, list)  # Solo verificamos que no falle
