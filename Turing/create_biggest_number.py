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

    digit_count = Counter(num_str)
    unique_digits = sorted(digit_count.keys(), reverse=True)
    return {int(d): [int(d)] * digit_count[d] for d in unique_digits}


def form_number_from_dict(num_dict, k):
    result = []
    last_digit = None
    count = 0

    while any(num_dict.values()):
        for key in sorted(num_dict.keys(), reverse=True):
            if num_dict[key]:
                if last_digit == key and count >= k:
                    continue

                result.append(num_dict[key].pop(0))
                if last_digit == key:
                    count += 1
                else:
                    last_digit = key
                    count = 1
                break

    return "".join(map(str, result))
