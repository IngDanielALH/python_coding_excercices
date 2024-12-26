"""
Se te proporcionan los siguientes elementos de entrada:

Dos arreglos de enteros:
    a = [3, 4]
    b = [1, 2, 3]

Un conjunto de consultas (queries):
    queries = [[1, 5], [0, 0, 1], [1, 5]]

Reglas para procesar las consultas:

Consulta tipo [1, X]: Calcula cuántas combinaciones de elementos a[i]+b[j]a[i]+b[j] son iguales a XX, donde ii y
jj son índices válidos dentro de los arreglos aa y bb. Agrega el resultado al arreglo de salida.

Consulta tipo [0, i, X]: Actualiza el valor del elemento a[i]a[i] a XX.

Proceso:

    Consulta [1, 5]:
        Calcula a[i]+b[j]=5:
        (a[0]+b[1])=3+2=5
        (a[1]+b[0])=4+1=5
        Resultado: 2 combinaciones.
        Salida parcial: [2]

    Consulta [0, 0, 1]:
        Actualiza a[0]=1
        a=[1,4]

    Consulta [1, 5]:
        Calcula a[i]+b[j]=5:
        (a[1]+b[0])=4+1=5
        Resultado: 1 combinación.
        Salida final: [2, 1]
"""
from collections import Counter


def process_queries(a, b, queries):
    b_counter = Counter(b)
    output = []

    for query in queries:
        if query[0] == 1:
            X = query[1]

            count = 0

            for ai in a:
                required_value = X - ai

                if required_value in b_counter:
                    count += b_counter[required_value]

            output.append(count)
        elif query[0] == 0:
            i, X = query[1], query[2]
            a[i] = X

    return output
    pass
