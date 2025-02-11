import unittest
from exercise_1 import getServerIds


class TestExcercise1(unittest.TestCase):
    def test_1(self):
        num_servers = 5
        requests = [3, 2, 3, 2, 4]
        expected = [0, 1, 2, 0, 3]
        self.assertEqual(expected, getServerIds(num_servers, requests))

    def test_2(self):
        num_servers = 5
        requests = [4, 0, 2, 2]
        expected = [0, 0, 1, 2]
        self.assertEqual(expected, getServerIds(num_servers, requests))

    def test_3(self):
        num_servers = 5
        requests = [0, 1, 2, 3]
        expected = [0, 1, 2, 3]
        self.assertEqual(expected, getServerIds(num_servers, requests))

    def test_4(self):
        num_servers = 10
        requests = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        expected = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]  # Se distribuyen equitativamente
        self.assertEqual(expected, getServerIds(num_servers, requests))

    def test_5(self):
        num_servers = 8
        requests = [7, 6, 5, 4, 3, 2, 1, 0]
        expected = [0, 0, 0, 0, 0, 0, 0, 0]  # Cada solicitud se asigna al primer servidor disponible
        self.assertEqual(expected, getServerIds(num_servers, requests))

    def test_6(self):
        num_servers = 100000
        requests = [i % 100000 for i in range(100)]
        expected = list(range(100))  # Cada servidor se asigna secuencialmente
        self.assertEqual(expected, getServerIds(num_servers, requests))

    def test_7(self):
        num_servers = 100
        requests = [99, 99, 99, 99, 99]
        expected = [0, 1, 2, 3, 4]  # Siempre elige el menor ID disponible
        self.assertEqual(expected, getServerIds(num_servers, requests))