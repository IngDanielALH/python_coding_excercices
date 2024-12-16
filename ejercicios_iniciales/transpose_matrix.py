"""You're given a 2D array of integers matrix. Write a function that returns the transpose of the matrix. The
transpose of a matrix is a flipped version of the original matrix across its main diagonal (which runs from top-left
to bottom-right); it switches the row and column indices of the original matrix. You can assume the input matrix
always has at least 1 value; however its width and height are not necessarily the same."""


def transpose_matrix(matrix):
    new_matrix = []

    for i in range(0, len(matrix)):  # renglones
        new_matrix.append([])
        for j in range(0, len(matrix[0])):  # columnas
            new_matrix[i].append(matrix[i][j])  # Agregamos los elementos del renglón

    return new_matrix
