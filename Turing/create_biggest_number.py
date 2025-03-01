""" Dada un un número en formato String y un valor K, generar el mayor núemero posible sin contener más de
k números iguales consecutivos.
Ejemplo:
Input: 3391933
Output: 99333139933313 """
from collections import Counter


def generate_biggest_number(number, k):
    num_dict = create_digit_dict(number)
    new_number = form_number_from_dict(num_dict, k)
    print(f"Nuevo número generado: {new_number}")
    return new_number
    pass


def create_digit_dict(num_str):
    """
    Crea un diccionario donde las claves son índices consecutivos y
    los valores son listas de dígitos agrupados en orden descendente.
    """
    digit_count = Counter(num_str)  # Contar ocurrencias de cada dígito
    unique_digits = sorted(digit_count.keys(), reverse=True)  # Ordenar los dígitos de mayor a menor
    return {int(d): [int(d)] * digit_count[d] for d in unique_digits}  # Crear diccionario con listas


def form_number_from_dict(num_dict, k):
    result = []
    last_digit = None  # Último dígito agregado
    count = 0  # Contador de repeticiones consecutivas

    while any(num_dict.values()):  # Mientras haya valores en alguna lista
        for key in sorted(num_dict.keys(), reverse=True):  # Recorremos en orden descendente
            if num_dict[key]:  # Si la lista tiene elementos
                if last_digit == key and count >= k:
                    continue  # Evita repetir el mismo número más de K veces seguidas

                result.append(num_dict[key].pop(0))  # Agregar el número al resultado
                if last_digit == key:
                    count += 1
                else:
                    last_digit = key
                    count = 1
                break  # Pasamos al siguiente número para evitar más de K consecutivos

    return "".join(map(str, result))
