"""
Se está examinando el rendimiento de las acciones de una empresa para evaluar su beneficio neto a lo largo del tiempo.

Para un parámetro de análisis dado k, un intervalo de k meses consecutivos se considera altamente rentable si los
precios de las acciones aumentan estrictamente a lo largo de esos meses. Dados los precios de las acciones para n meses
y el parámetro de análisis k, determine el número de dichos intervalos altamente rentables.

Ejemplo
preciosAcciones = [5, 3, 5, 7, 8]
k = 3

    ▲ Precios
   8 ┤                   █
   7 ┤                ██ █
   6 ┤                ██ █
   5 ┤ █        ██    ██ █
   4 ┤ █        ██    ██ █
   3 ┤ █  ██    ██    ██ █
   2 ┤ █  ██    ██    ██ █
   1 ┤ █  ██    ██    ██ █
     └───────────────────────► Meses
       1  (2)  (3)  (4)  5

(Intervalo resaltado: Meses 2, 3, 4 con precios 3, 5, 7)

    ▲ Precios
   8 ┤                ██
   7 ┤          ██    ██
   6 ┤          ██    ██
   5 ┤ █        ██    ██
   4 ┤ █        ██    ██
   3 ┤ █  █     ██    ██
   2 ┤ █  █     ██    ██
   1 ┤ █  █     ██    ██
     └───────────────────────► Meses
       1  2   (3)  (4)  (5)

(Intervalo resaltado: Meses 3, 4, 5 con precios 5, 7, 8)

Por lo tanto, la respuesta es 2.
"""


def analyze_window(window):
    print(f"Ventana a analizar: {window}")
    for i in range(len(window) - 1):
        p1 = window[i]
        p2 = window[i + 1]
        if p2 <= p1:
            return False
    return True
    pass


def analyzer(prices, k):
    if not prices or len(prices) < k:
        return 0

    result = 0

    for i in range(len(prices) - k + 1):
        if analyze_window(prices[i: i + k]):
            result += 1
    return result
    pass
