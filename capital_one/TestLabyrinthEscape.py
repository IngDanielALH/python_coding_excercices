import unittest
from labyrinth_escape import solution


class TestLabyrinthEscape(unittest.TestCase):

    def test_example_case(self):
        """El caso de ejemplo provisto en la descripción del problema."""
        n = 3
        m = 3
        obstacles = [[2, 1]]
        teleports = [[0, 1, 2, 0]]
        # Camino: (0,0) -> TP(0,1) a (2,0) -> Bloqueado Derecha y Abajo -> Atrapado
        expected_output = -1
        self.assertEqual(solution(n, m, obstacles, teleports), expected_output)

    def test_simple_path_no_obstacles(self):
        """Camino libre sin obstáculos ni teleports."""
        n = 3
        m = 3
        obstacles = []
        teleports = []
        # Camino esperado: (0,0)->(0,1)->(0,2)->(1,2)->(2,2)
        # Total celdas: 5
        expected_output = 5
        self.assertEqual(solution(n, m, obstacles, teleports), expected_output)

    def test_obstacle_bypass(self):
        """Prueba la lógica de desvío hacia abajo cuando hay obstáculo a la derecha."""
        n = 3
        m = 3
        obstacles = [[0, 1]]
        teleports = []
        # (0,0) -> Derecha bloqueada -> Baja a (1,0) -> (1,1) -> (1,2) -> (2,2)
        expected_output = 5
        self.assertEqual(solution(n, m, obstacles, teleports), expected_output)

    def test_teleport_success(self):
        """Teletransporte directo a la meta, cuenta inicio y fin del TP."""
        n = 3
        m = 3
        obstacles = []
        teleports = [[0, 1, 2, 2]]
        # Camino: (0,0) -> TP_Start(0,1) -> TP_End(2,2)
        # Celdas: 1 + 1 + 1 = 3
        expected_output = 3
        self.assertEqual(solution(n, m, obstacles, teleports), expected_output)

    def test_infinite_loop(self):
        """Detección de bucle infinito causado por teletransporte."""
        n = 3
        m = 3
        obstacles = []
        teleports = [[0, 1, 0, 0]]
        # (0,0) -> (0,1) -> Teleporta a (0,0) -> Repite
        expected_output = -2
        self.assertEqual(solution(n, m, obstacles, teleports), expected_output)

    def test_trapped_immediately(self):
        """El jugador queda encerrado sin poder moverse."""
        n = 2
        m = 2
        obstacles = [[0, 1], [1, 0]]
        teleports = []
        # (0,0) -> Derecha bloqueada, Abajo bloqueado.
        expected_output = -1
        self.assertEqual(solution(n, m, obstacles, teleports), expected_output)


if __name__ == '__main__':
    unittest.main()