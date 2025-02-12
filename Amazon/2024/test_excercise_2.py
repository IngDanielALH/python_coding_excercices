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
        expected = [5, 3, 1, 0]
        self.assertEqual(expected, findRequestsInQueue(requests))

    def test_6(self):
        requests = [2, 3, 1, 5, 4]
        expected = [5, 3, 2, 1, 0]
        self.assertEqual(expected, findRequestsInQueue(requests))

    def test_7(self):
        requests = [2, 2, 2, 2]
        expected = [4, 3, 0]
        self.assertEqual(expected, findRequestsInQueue(requests))

    def test_min_n_max_wait(self):
        """Caso con n=1 y el máximo tiempo de espera."""
        requests = [100000]
        expected = [1, 0]  # La única request se procesa y luego la cola queda vacía
        self.assertEqual(expected, findRequestsInQueue(requests))
