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


class MazeSolver:
    """
    Clase para encontrar el camino más corto en un laberinto.
    """

    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.start_pos = self._find_char('S')

    def _find_char(self, char):
        """Encuentra las coordenadas de un carácter específico en el laberinto."""
        for r in range(self.rows):
            for c in range(self.cols):
                if self.maze[r][c] == char:
                    return r, c
        return None

    def find_shortest_path(self):
        """
        Encuentra la longitud del camino más corto desde 'S' hasta 'E'.

        Aquí es donde implementarás la lógica principal.
        Si no hay camino, devuelve -1.
        """
        # --- TU LÓGICA VA AQUÍ ---
        # Pista: Necesitarás una cola y una forma de rastrear las celdas visitadas.

        return -1  # Valor por defecto mientras no esté implementado.
