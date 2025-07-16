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