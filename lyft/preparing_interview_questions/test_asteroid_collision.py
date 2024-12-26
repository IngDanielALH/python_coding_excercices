import unittest
from asteroid_collision import asteroidCollision


class testAsteroidCollision(unittest.TestCase):
    def test_1(self):
        asteroids = [5, 10, -5]
        expected = [5, 10]
        result = asteroidCollision(asteroids)
        self.assertEqual(expected, result)
        pass

    def test_2(self):
        asteroids = [8, -8]
        expected = []
        result = asteroidCollision(asteroids)
        self.assertEqual(expected, result)
        pass

    def test_3(self):
        asteroids = [10, 2, -5]
        expected = [10]
        result = asteroidCollision(asteroids)
        self.assertEqual(expected, result)
        pass
