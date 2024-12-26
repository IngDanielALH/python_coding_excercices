class Solution:
    def exist(self, board, word):
        n = len(board)  # Número de filas
        m = len(board[0])  # Número de columnas

        visited = [[False for _ in range(m)] for _ in range(n)]  # Matriz para celdas visitadas

        word_char = list(word)  # Convertir la palabra en una lista de caracteres

        # Verificación rápida: si la longitud de la palabra excede el total de celdas, no puede existir
        if len(word_char) > n * m:
            return False

        counts = [0] * 256  # Array para contar ocurrencias de caracteres

        # Contar ocurrencias de cada carácter en el tablero
        for i in range(n):
            for j in range(m):
                counts[ord(board[i][j])] += 1

        # Ajustar el orden de los caracteres en word_char basado en su frecuencia
        length = len(word_char)
        for i in range(length // 2):
            if counts[ord(word_char[i])] > counts[ord(word_char[length - 1 - i])]:
                for j in range(length // 2):
                    word_char[j], word_char[length - 1 - j] = word_char[length - 1 - j], word_char[j]
                break

        # Reducir las cuentas de caracteres de word_char en el tablero
        for c in word_char:
            if counts[ord(c)] <= 0:
                return False
            counts[ord(c)] -= 1

        # Buscar la palabra comenzando desde cada celda
        for i in range(n):
            for j in range(m):
                if self.visit(board, word_char, 0, i, j, n, m, visited):
                    return True

        return False

    def visit(self, board, word, start, x, y, n, m, visited):
        # Caso base: si se encontraron todos los caracteres
        if start == len(word):
            return True

        # Verificar límites, celda ya visitada, o si el carácter no coincide
        if x < 0 or x >= n or y < 0 or y >= m or visited[x][y]:
            return False

        if word[start] != board[x][y]:
            return False

        visited[x][y] = True  # Marcar la celda como visitada

        # Buscar recursivamente en las cuatro direcciones
        found = (
            self.visit(board, word, start + 1, x + 1, y, n, m, visited)
            or self.visit(board, word, start + 1, x - 1, y, n, m, visited)
            or self.visit(board, word, start + 1, x, y + 1, n, m, visited)
            or self.visit(board, word, start + 1, x, y - 1, n, m, visited)
        )

        visited[x][y] = False  # Desmarcar la celda (backtracking)

        return found
