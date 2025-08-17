"""
Calcular el elemento nth de la serie de fibonacci
"""


def fibonacci(n):
    return 5
    pass


def test_case(message, expected, actual):
    if expected == actual:
        print(f"Test {message} SUCCESS")
    else:
        print(f"Test {message} FAIL, expected: {expected} got: {actual}")
    pass


if __name__ == '__main__':
    test_case("Test 1: Caso base n=0", 0, fibonacci(0))
    test_case("Test 2: Caso base n=1", 1, fibonacci(1))

    # Pruebas con números pequeños
    test_case("Test 3: n=2", 1, fibonacci(2))
    test_case("Test 4: n=3", 2, fibonacci(3))
    test_case("Test 5: n=8", 21, fibonacci(8))

    # Prueba con un número más grande
    test_case("Test 6: n=15", 610, fibonacci(15))
