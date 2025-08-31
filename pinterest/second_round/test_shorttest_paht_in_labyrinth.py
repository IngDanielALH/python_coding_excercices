import unittest
from shorttest_path_in_labyrinth import MazeSolver


class TestMazeSolver(unittest.TestCase):
    def test_simple_path(self):
        print("\nProbando un camino simple...")
        laberinto = [
            ['S', '.', '.'],
            ['#', '#', '.'],
            ['.', '.', 'E']
        ]
        solver = MazeSolver(laberinto)
        self.assertEqual(solver.find_shortest_path(), 4)

    def test_no_path(self):
        print("Probando un laberinto sin solución...")
        laberinto = [
            ['S', '#', 'E'],
            ['.', '#', '.'],
            ['.', '#', '.']
        ]
        solver = MazeSolver(laberinto)
        self.assertEqual(solver.find_shortest_path(), -1)

    def test_more_complex_path(self):
        print("Probando un camino más complejo...")
        laberinto = [
            ['.', '#', 'S', '.', '.'],
            ['.', '#', '.', '#', '.'],
            ['.', '.', '.', '.', '.'],
            ['#', '#', '#', '.', '#'],
            ['.', '.', '.', '.', 'E']
        ]
        solver = MazeSolver(laberinto)
        self.assertEqual(solver.find_shortest_path(), 8)

    def test_start_is_end(self):
        print("Probando caso donde S y E están juntos...")
        laberinto = [
            ['S', 'E']
        ]
        solver = MazeSolver(laberinto)
        # Se necesita un paso para ir de S a E
        self.assertEqual(solver.find_shortest_path(), 1)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
