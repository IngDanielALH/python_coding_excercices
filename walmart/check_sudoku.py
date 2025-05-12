def check(sudoku):
    if len(sudoku) == 0:
        return False

    valid_range = [i + 1 for i in range(0, len(sudoku[0]))]

    row_set = set()
    col_set = set()

    for i in range(0, len(sudoku)):
        for j in range(0, len(sudoku[0])):
            if sudoku[j][i] not in valid_range:
                return False
            if j == 0:
                if sudoku[j][i] in row_set:
                    return False
                else:
                    row_set.add(sudoku[j][i])
                    col_set.add(sudoku[j][i])
            else:
                if sudoku[j][i] in col_set:
                    return False
                else:
                    col_set.add(sudoku[j][i])

            if j == len(sudoku[0]) - 1:
                col_set.clear()

    return True
    pass


def check_chatgpt(sudoku):
    # Verificar si el Sudoku está vacío
    if len(sudoku) == 0:
        return False

    n = len(sudoku)  # Tamaño de la cuadrícula
    valid_range = set(range(1, n + 1))

    # Función para verificar si una lista tiene elementos únicos y válidos
    def is_valid_group(group):
        return set(group) == valid_range

    # Verificación de filas
    for row in sudoku:
        if not is_valid_group(row):
            return False

    # Verificación de columnas
    for col in range(n):
        column = [sudoku[row][col] for row in range(n)]
        if not is_valid_group(column):
            return False

    # Si todas las verificaciones pasan, el Sudoku es válido
    return True


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [2, 3, 1],
              [3, 1, 2]]
    is_sudoku = check_chatgpt(matrix)
    print("Es sudoku" if is_sudoku else "No es sudoku")
