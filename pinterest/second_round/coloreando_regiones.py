"""
Imagina que tienes una imagen representada por una matriz de píxeles, donde cada píxel tiene un color.
Se te da un punto de inicio (fila, columna) y un nuevo color.

Debes "inundar" o cambiar el color de toda la región que contiene al punto de inicio.
Una región está formada por todos los píxeles adyacentes (arriba, abajo, izquierda, derecha) que tienen el mismo color
original que el píxel de inicio.

Entrada: Una matriz de colores, las coordenadas del píxel de inicio y el nuevo color.
Salida: La matriz modificada después de haber coloreado toda la región conectada.
"""

neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def flood_fill(image, start_row, start_col, new_color):

    if image[start_row][start_col] == new_color:
        return image

    return dfs(image, start_row, start_col, image[start_row][start_col], new_color)
    pass


def dfs(image, x, y, original, new_color):
    rows = len(image)
    cols = len(image[0])

    if 0 <= x < rows and 0 <= y < cols and image[x][y] == original:
        image[x][y] = new_color
        imprimir_matriz(image)
    else:
        return

    for x_neighbor, y_neighbor in neighbors:
        dfs(image, x + x_neighbor, y + y_neighbor, original, new_color)

    return image


def imprimir_matriz(matriz):
    """
  Imprime una matriz (lista de listas) en un formato legible.

  Args:
    matriz: Una lista de listas donde cada lista interna es una fila de la matriz.
  """
    # Itera sobre cada fila en la matriz
    for fila in matriz:
        # Itera sobre cada número (elemento) en la fila
        for elemento in fila:
            # Imprime el elemento seguido de un espacio, sin saltar de línea
            print(elemento, end=" ")
        # Imprime un salto de línea al final de cada fila para pasar a la siguiente
        print()
    print("-----------------------")
