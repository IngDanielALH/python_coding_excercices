"""
El Camino Más Corto en el Laberinto

Se te proporciona un laberinto representado por una matriz bidimensional de tamaño N x M. Las celdas pueden ser:

    'S': Punto de inicio.
    'E': Punto final.
    '.': Un pasillo por el que puedes moverte.
    '#': Un muro que no puedes atravesar.

Tu tarea es encontrar la longitud del camino más corto desde 'S' hasta 'E'. Puedes moverte en cuatro
direcciones: arriba, abajo, izquierda y derecha.
Si no existe un camino, debes indicarlo.

Entrada: Una matriz de caracteres representando el laberinto.
Salida: Un número entero que representa la longitud del camino más corto. Si no hay solución, devuelve -1.
"""

from collections import deque


class MazeSolver:
    """
    Clase para encontrar el camino más corto en un laberinto.
    """

    START = 'S'
    END = 'E'
    PASILLO = '.'
    MURO = '#'
    VISITED = 'V'

    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.start_pos = self._find_start()

    def _find_start(self):
        """Encuentra las coordenadas de un carácter específico en el laberinto."""
        for r in range(self.rows):
            for c in range(self.cols):
                if self.maze[r][c] == self.START:
                    return r, c
        return None

    def to_visit_nodes(self, current):
        x = current[0]
        y = current[1]
        to_visit = []
        for neighbor in self.neighbors:
            x_neighbor, y_neighbor = neighbor
            x_expected = x + x_neighbor
            y_expected = y + y_neighbor
            if 0 <= x_expected < self.rows and 0 <= y_expected < self.cols:
                to_visit.append((x_expected, y_expected))
        return to_visit
        pass

    def is_end(self, current):
        x = current[0]
        y = current[1]
        if self.maze[x][y] == self.END:
            return True

    def mark_visited(self, node):
        self.maze[node[0]][node[1]] = self.VISITED
        pass

    def find_shortest_path(self):

        cola = deque()
        cola.append((self._find_start(), 0))
        while cola:
            current, count = cola.popleft()

            new_nodes = self.to_visit_nodes(current)
            for node in new_nodes:
                x, y = node

                if self.maze[x][y] == self.END:
                    return count + 1
                elif self.maze[x][y] == self.PASILLO:
                    self.mark_visited(node)
                    cola.append((node, count + 1))

        return -1  # Valor por defecto mientras no esté implementado.
