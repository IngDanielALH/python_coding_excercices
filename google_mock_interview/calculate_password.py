"""
Dada una contraseña s obtener el número de cambios necesarios para que la contraseña cumpla con las condiciones:
1. Que sea un palindromo
2. Que cumpla con un ciclo K, es decir, que cada K elementos se repita el mismo caracter
"""
from collections import Counter


def calculate_changes(password, k):
    password = list(password)  # ✅ Esto es clave
    total_changes = 0
    len_password = len(password)

    for j in range(k):
        indices = [i for i in range(j, len_password, k)]
        indices += [len_password - 1 - i for i in indices]  # Reflejo para palíndromo

        group = [password[i] for i in indices]
        common_char = Counter(group).most_common(1)[0][0]

        for i in indices:
            if password[i] != common_char:
                password[i] = common_char
                total_changes += 1

    return total_changes


if __name__ == '__main__':
    password = "cbpecbbc"
    k = 4
    print(f"Total changes: {calculate_changes(password, k)}")
