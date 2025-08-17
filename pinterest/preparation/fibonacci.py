"""
Calcular el elemento nth de la serie de fibonacci
"""
import time


def fibonacci(n, memo=None):
    if memo is None:
        memo = {0: 0, 1: 1}

    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 2, memo) + fibonacci(n - 1, memo)

    return memo[n]


def test_case(message, expected, actual):
    if expected == actual:
        print(f"Test {message} SUCCESS")
    else:
        print(f"Test {message} FAIL, expected: {expected} got: {actual}")
    pass


def time_fibonacci(n):
    """
    Mide el tiempo que tarda la función fibonacci(n) en ejecutarse.
    """
    print(f"Calculando fibonacci({n})...")

    # 1. Guarda el tiempo de inicio
    start_time = time.time()

    # 2. Ejecuta la función y guarda el resultado
    result = fibonacci(n)

    # 3. Guarda el tiempo de finalización
    end_time = time.time()

    # 4. Calcula la duración
    duration = end_time - start_time

    # 5. Muestra los resultados en pantalla
    print(f"-> Resultado: {result}")
    print(f"-> Tiempo de ejecución: {duration:.6f} segundos")  # Formateado a 6 decimales
    print("-" * 20)
    return result


if __name__ == '__main__':
    test_case("Test 1: Caso base n=0", 0, time_fibonacci(0))
    test_case("Test 2: Caso base n=1", 1, time_fibonacci(1))

    # Pruebas con números pequeños
    test_case("Test 3: n=2", 1, time_fibonacci(2))
    test_case("Test 4: n=3", 2, time_fibonacci(3))
    test_case("Test 5: n=8", 21, time_fibonacci(8))

    # Prueba con un número más grande
    test_case("Test 6: n=15", 610, time_fibonacci(15))

    test_case("Test 7: n=15", 610, time_fibonacci(35))
    test_case("Test 7: n=15", 610, time_fibonacci(36))
    test_case("Test 7: n=15", 610, time_fibonacci(37))
    test_case("Test 7: n=15", 610, time_fibonacci(37))
    test_case("Test 7: n=15", 610, time_fibonacci(1000))
