import unittest
from snakes_stairs import quickestWayUp


class TestSnakesAndLadders(unittest.TestCase):

    def test_sample_case_1(self):
        """
        Prueba el primer caso de ejemplo de la imagen.
        """
        print("Ejecutando Test Case 1...")
        ladders = [[32, 62], [42, 68], [12, 98]]
        snakes = [[95, 13], [97, 25], [93, 37], [79, 27], [75, 19], [49, 47], [67, 17]]
        expected_result = 3

        result = quickestWayUp(ladders, snakes)
        self.assertEqual(result, expected_result)

    def test_sample_case_2(self):
        """
        Prueba el segundo caso de ejemplo de la imagen.
        """
        print("\nEjecutando Test Case 2...")
        ladders = [[8, 52], [6, 80], [26, 42], [2, 72]]
        snakes = [[51, 19], [39, 11], [37, 29], [81, 3], [59, 5], [79, 23], [53, 7], [43, 33], [77, 21]]
        expected_result = 5

        result = quickestWayUp(ladders, snakes)
        self.assertEqual(result, expected_result)
