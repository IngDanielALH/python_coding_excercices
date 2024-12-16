"""You're given a 2D array of integers matrix. Write a function that returns the transpose of the matrix. The
transpose of a matrix is a flipped version of the original matrix across its main diagonal (which runs from top-left
to bottom-right); it switches the row and column indices of the original matrix. You can assume the input matrix
always has at least 1 value; however its width and height are not necessarily the same."""


def transpose_matrix(matrix):
    # Write your code her
    return []


def son_matrices_iguales(matriz1, matriz2):
    if len(matriz1) != len(matriz2):
        return False
    for fila1, fila2 in zip(matriz1, matriz2):
        if fila1 != fila2:
            return False
    return True
