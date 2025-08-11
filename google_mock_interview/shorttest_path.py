"""
Dos amigos están perdidos en un país y quieren llegar a una ciudad de refugio. El mapa del país se representa como
un grafo no dirigido y no ponderado. Esto significa que las carreteras (aristas) conectan las ciudades (nodos) en ambas
direcciones y el costo de viajar por cualquier carretera es siempre el mismo: un paso.

Los amigos comienzan en ciudades diferentes y deben llegar a la misma ciudad destino. Se mueven por turnos, y cada
viaje de una ciudad a otra conectada cuenta como un paso.

La regla especial es la siguiente:

    Mientras viajan por separado, cada paso que da cada amigo se suma al costo total.

    Si ambos amigos llegan a la misma ciudad (se encuentran), pueden continuar el viaje juntos. A partir de ese momento,
    cuando se mueven de una ciudad a otra, cuenta como un solo paso para el grupo en lugar de un paso para cada uno.

Tu objetivo es encontrar el número total mínimo de pasos necesarios para que ambos amigos lleguen a la ciudad destino.

Entrada

    Una lista de ciudades (nodos).

    Una lista de carreteras que conectan pares de ciudades (aristas).

    La ciudad de inicio del Amigo 1.

    La ciudad de inicio del Amigo 2.

    La ciudad destino.

Salida

Debes devolver el número entero mínimo de pasos combinados para que ambos lleguen al destino.

Ejemplo

Imagina el siguiente mapa:

    Amigo 1 inicia en A.

    Amigo 2 inicia en E.

    El Destino es D.

Análisis de posibles estrategias:

    Rutas separadas (sin encuentro previo):

        La ruta más corta para el Amigo 1 es A → B → D (2 pasos).

        La ruta más corta para el Amigo 2 es E → C → D (2 pasos).

        Costo Total: 2 (Amigo 1) + 2 (Amigo 2) = 4 pasos.

    Encontrándose en el camino (en el nodo B):

        Amigo 1 viaja de A → B (1 paso).

        Amigo 2 viaja de E → C → B (2 pasos).

        Para que se encuentren, el Amigo 1 espera en B. El costo hasta el encuentro es la suma de sus pasos: 1 + 2 = 3
        pasos.

        Ahora, juntos en B, viajan a D. Este movimiento cuenta como un solo paso para el grupo. (1 paso).

        Costo Total: 3 (hasta el encuentro) + 1 (viaje juntos) = 4 pasos.

    Encontrándose en el camino (en el nodo C):

        Amigo 1 viaja de A → B → C (2 pasos).

        Amigo 2 viaja de E → C (1 paso).

        El costo hasta el encuentro en C es: 2 + 1 = 3 pasos.

        Juntos en C, viajan a D. Este es un solo paso para el grupo (1 paso).

        Costo Total: 3 (hasta el encuentro) + 1 (viaje juntos) = 4 pasos.

En este ejemplo particular, todas las estrategias óptimas llevan a un costo de 4 pasos. El desafío es encontrar este
valor mínimo de manera algorítmica.
"""


def calcular_ruta_amigos(graph: dict, inicio_amigo1: str, inicio_amigo2: str, destino: str) -> int:
    """
    Calcula el número total mínimo de pasos para que dos amigos, comenzando
    en puntos diferentes, lleguen a un destino común en un grafo no ponderado.

    El costo se mide en pasos. Si los amigos viajan juntos por una arista,
    cuenta como un solo paso para el total.

    Args:
        graph (dict): Un diccionario que representa el grafo como una lista de
                      adyacencia. Las claves son los nodos (ciudades) y los
                      valores son una lista de sus vecinos.
                      Ejemplo: {'A': ['B', 'C'], 'B': ['A', 'D'], ...}
        inicio_amigo1 (str): El nodo de inicio para el primer amigo.
        inicio_amigo2 (str): El nodo de inicio para el segundo amigo.
        destino (str): El nodo destino común.

    Returns:
        int: El número total mínimo de pasos combinados para llegar al destino.
    """
    # La lógica para resolver el problema iría aquí.
    pass
