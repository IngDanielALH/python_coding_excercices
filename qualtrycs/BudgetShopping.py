"""
Una escuela ha proporcionado a un maestro un presupuesto para comprar cuadernos de matemáticas que los estudiantes
necesitan. Varias tiendas venden paquetes de cuadernos a distintos precios. El maestro quiere comprar tantos cuadernos
como sea posible dentro del presupuesto, pero solo puede comprar paquetes completos.

Determina el número máximo de cuadernos que el maestro puede comprar.

Por ejemplo, el maestro tiene n = $50 y hay m = 2 tiendas. La primera vende paquetes de 20 cuadernos por $12 cada uno.
La segunda vende paquetes de solo 1 cuaderno por $2 cada uno. El maestro puede comprar 4 paquetes de 20 por $48,
quedándole $2. El maestro puede entonces ir a la segunda tienda y comprar 1 cuaderno más por $2, para un total de 81
cuadernos.

Descripción de la Función

Completa la función budgetShopping en el editor a continuación.

budgetShopping tiene los siguientes parámetros:

    int budget: la cantidad de dinero en el presupuesto para cuadernos.

    int bundleQuantities[n]: el número de cuadernos en un paquete en la tienda[i].

    int bundleCosts[n]: el costo de un paquete de cuadernos en la tienda[i].

Retorno

    int: el número máximo de cuadernos que se pueden comprar.
"""


def budget_shopping(budget, bundle_quantities, bundle_costs):
    dp = [0] * (budget + 1)
    for i in range(1, budget + 1):
        for cantidad, costo in zip(bundle_quantities, bundle_costs):
            if i >= costo:
                dp[i] = max(dp[i], cantidad + dp[i - costo])
    return dp[-1]
