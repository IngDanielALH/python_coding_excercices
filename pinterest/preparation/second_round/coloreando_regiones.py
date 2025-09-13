"""
Imagina que tienes una imagen representada por una matriz de píxeles, donde cada píxel tiene un color.
Se te da un punto de inicio (fila, columna) y un nuevo color.

Debes "inundar" o cambiar el color de toda la región que contiene al punto de inicio.
Una región está formada por todos los píxeles adyacentes (arriba, abajo, izquierda, derecha) que tienen el mismo color
original que el píxel de inicio.

Entrada: Una matriz de colores, las coordenadas del píxel de inicio y el nuevo color.
Salida: La matriz modificada después de haber coloreado toda la región conectada.
"""

from collections import deque


def flood_fill(image, start_row, start_col, new_color):
    """
    Colorea una región de la imagen a partir de un punto de inicio.

    Args:
        image (list[list[int]]): La matriz bidimensional de colores.
        start_row (int): La fila del píxel inicial.
        start_col (int): La columna del píxel inicial.
        new_color (int): El nuevo color para la región.

    Returns:
        list[list[int]]: La imagen modificada.
    """
    # --- TU LÓGICA VA AQUÍ ---
    # Pista: Necesitarás el color original del píxel de inicio.
    # Pista: ¿Qué pasa si el color original ya es el nuevo color?
    # Pista: Puedes usar una cola (BFS) o una pila/recursión (DFS).

    pass