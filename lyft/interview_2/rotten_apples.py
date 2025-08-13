"""
Se te proporciona una rejilla de tamaño m x n que representa un huerto de manzanas. Cada celda de la rejilla puede tener
 uno de tres valores:

    0: Representa una celda vacía (sin manzana).

    1: Representa una manzana fresca.

    2: Representa una manzana podrida.

En cada minuto, cualquier manzana fresca que sea adyacente (arriba, abajo, izquierda, derecha) a una manzana podrida se
pudrirá.

Tu tarea es determinar el tiempo mínimo (en minutos) requerido para que todas las manzanas frescas en el huerto se
pudran.

Si en algún momento quedan manzanas frescas que no pueden pudrirse (porque no son alcanzables por ninguna manzana
podrida), debes retornar -1.

Consideraciones:

    Puedes asumir que la rejilla siempre contendrá al menos una manzana.

    Las dimensiones m y n estarán entre 1 y 10.

Ejemplo:

Entrada:

[[2,1,1],
 [1,1,0],
 [0,1,1]]

Salida: 4

Explicación del Ejemplo:

    Minuto 0: La manzana en (0,0) está podrida.

    Minuto 1: La manzana en (0,1) y (1,0) se pudren.

    Minuto 2: La manzana en (1,1) se pudre.

    Minuto 3: La manzana en (2,1) se pudre.

    Minuto 4: La manzana en (2,2) se pudre.Ejemplo:

Entrada:

[[2,1,1],
 [1,1,0],
 [0,1,1]]

Salida: 4

Explicación del Ejemplo:

    Minuto 0: La manzana en (0,0) está podrida.

    Minuto 1: La manzana en (0,1) y (1,0) se pudren.

    Minuto 2: La manzana en (1,1) se pudre.

    Minuto 3: La manzana en (2,1) se pudre.

    Minuto 4: La manzana en (2,2) se pudre.




"""

from collections import deque


def calculate_steps(box: list[list[int]]) -> int:
    """
    Calcula el tiempo mínimo para que todas las naranjas se pudran usando BFS.
    Reglas:
    0: Celda vacía
    1: Naranja fresca
    2: Naranja podrida
    """
    if not box or not box[0]:
        return 0

    rows, cols = len(box), len(box[0])
    queue = deque()
    fresh_oranges = 0

    # 1. Inicialización: Contar naranjas frescas y encontrar las podridas iniciales
    for r in range(rows):
        for c in range(cols):
            if box[r][c] == 1:
                fresh_oranges += 1
            elif box[r][c] == 2:
                # La cola guarda (fila, columna, minutos)
                queue.append((r, c))

    # Si no hay naranjas frescas desde el principio, el tiempo es 0.
    if fresh_oranges == 0:
        return 0

    minutes = 0
    # Direcciones para moverse a las celdas vecinas (arriba, abajo, izquierda, derecha)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # 2. Proceso BFS para simular el tiempo
    while queue:
        # Procesar todas las naranjas podridas del nivel actual (un minuto)
        # El tamaño de la cola en este punto es el número de naranjas a procesar en este minuto.
        level_size = len(queue)

        # Una bandera para asegurar que incrementamos los minutos solo si hubo un cambio
        rotted_in_this_minute = False

        for _ in range(level_size):
            r, c = queue.popleft()

            # Revisar los 4 vecinos
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc

                # Verificar si el vecino está dentro de la matriz y es una naranja fresca
                if 0 <= new_r < rows and 0 <= new_c < cols and box[new_r][new_c] == 1:
                    box[new_r][new_c] = 2  # Se pudre la naranja
                    fresh_oranges -= 1  # Decrementamos el contador
                    queue.append((new_r, new_c))  # La añadimos para el siguiente minuto
                    rotted_in_this_minute = True

        # Si se pudrió al menos una naranja en esta ronda, pasa un minuto
        if rotted_in_this_minute:
            minutes += 1

    # 3. Resultado final
    # Si aún quedan naranjas frescas, son inalcanzables.
    return minutes if fresh_oranges == 0 else -1
