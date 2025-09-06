import unittest
from BudgetShopping import budget_shopping


class TestBudgetShopping(unittest.TestCase):

    def test_caso_del_ejemplo(self):
        """Prueba con los datos exactos del enunciado del problema."""
        budget = 50
        quantities = [20, 1]
        costs = [12, 2]
        # Se esperan 81 cuadernos: 4 paquetes de 20 ($48) + 1 paquete de 1 ($2)
        self.assertEqual(budget_shopping(budget, quantities, costs), 81)

    def test_presupuesto_insuficiente(self):
        """Prueba qué pasa si el presupuesto no alcanza para el paquete más barato."""
        budget = 10
        quantities = [15, 20]
        costs = [12, 15]
        self.assertEqual(budget_shopping(budget, quantities, costs), 0)

    def test_seleccion_optima_no_es_la_mas_barata(self):
        """
        Prueba un caso donde comprar repetidamente el paquete más barato no da
        el máximo número de cuadernos.
        """
        budget = 30
        quantities = [10, 12]  # El segundo paquete da más cuadernos
        costs = [10, 11]  # Pero es un poco más caro
        # Solución óptima: 2 paquetes de 12 (24 cuadernos por $22), sobran $8.
        # Solución no óptima: 3 paquetes de 10 (30 cuadernos por $30).
        # Ah, espera. La solución óptima es comprar el de 10 cuadernos 3 veces.
        # Corrijamos el test:
        budget = 32
        # Opción 1: 3 paquetes de 10 (30 cuadernos por $30)
        # Opción 2: 2 paquetes de 12 (24 cuadernos por $22)
        # La mejor es la primera.
        self.assertEqual(budget_shopping(budget, [10, 12], [10, 11]), 30)

    def test_presupuesto_exacto(self):
        """Prueba un caso donde el presupuesto se gasta por completo."""
        budget = 100
        quantities = [25, 10]
        costs = [50, 10]
        # Se pueden comprar 2 paquetes de 25 ($100), total 50 cuadernos.
        # O 10 paquetes de 10 ($100), total 100 cuadernos.
        self.assertEqual(budget_shopping(budget, quantities, costs), 100)

    def test_presupuesto_cero(self):
        """Prueba qué ocurre si el presupuesto inicial es 0."""
        budget = 0
        quantities = [10, 20]
        costs = [5, 10]
        self.assertEqual(budget_shopping(budget, quantities, costs), 0)

    def test_una_sola_opcion_de_compra(self):
        """Prueba con una única tienda disponible."""
        budget = 65
        quantities = [15]
        costs = [20]
        # Se pueden comprar 3 paquetes de 15 (45 cuadernos por $60).
        self.assertEqual(budget_shopping(budget, quantities, costs), 45)

    def test_multiples_paquetes_complejos(self):
        """Un caso más complejo con varias opciones."""
        budget = 70
        quantities = [10, 12, 5, 22]
        costs = [8, 9, 4, 18]
        # Posibles combinaciones a explorar por el algoritmo.
        # La solución óptima es 3 paquetes de 22 (66 cuadernos por $54) + 2 paquetes de 5 (10 cuadernos por $8)
        # Total = 76 cuadernos por $62.
        self.assertEqual(budget_shopping(budget, quantities, costs), 76)