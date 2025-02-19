import unittest
from robot_rodeo import doesCicleExist


class testRobotRodeo(unittest.TestCase):
    def test_1(self):
        commands = ["G", "L"]
        expected = ["NO", "YES"]
        self.assertEqual(expected, doesCicleExist(commands))

    def test_2(self):
        commands = ["GRGL"]
        expected = ["NO"]
        self.assertEqual(expected, doesCicleExist(commands))

    def test_3(self):
        commands = ["GRGRGRG"]
        expected = ["YES"]
        self.assertEqual(expected, doesCicleExist(commands))

    def test_4(self):
        commands = ["GLGLGGLGL"]
        expected = ["NO"]
        self.assertEqual(expected, doesCicleExist(commands))
