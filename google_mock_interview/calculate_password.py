"""
Dada una contraseña s obtener el número de cambios necesarios para que la contraseña cumpla con las condiciones:
1. Que sea un palindromo
2. Que cumpla con un ciclo K, es decir, que cada K elementos se repita el mismo caracter
"""
from collections import Counter


def calculate_changes(password, k):
    password = list(password)
    total_changes = 0
    n = len(password)

    for j in range(k):
        indices = [i for i in range(j, n, k)]
        reflected = [n - 1 - i for i in indices]
        all_indices = list(set(indices + reflected))  # Eliminar duplicados

        char_count = Counter(password[i] for i in all_indices)
        common_char, _ = char_count.most_common(1)[0]

        for i in all_indices:
            if password[i] != common_char:
                password[i] = common_char
                total_changes += 1

    return total_changes


if __name__ == '__main__':
    password = "cbpecbbc"
    k = 4
    print(f"Total changes: {calculate_changes(password, k)}")
