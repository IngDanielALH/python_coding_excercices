# Puedes guardar este código en un archivo llamado: test_analizador.py
# Asegúrate de que esté en la misma carpeta que el archivo anterior.

import unittest
from HighlyProfitableMonth import analyzer


class TestAnalizadorDeAcciones(unittest.TestCase):

    def test_caso_del_ejemplo(self):
        """Prueba con los datos exactos del enunciado del problema."""
        precios = [5, 3, 5, 7, 8]
        k = 3
        # Los intervalos son [3, 5, 7] y [5, 7, 8]
        self.assertEqual(analyzer(precios, k), 2)

    def test_sin_intervalos_rentables(self):
        """Prueba una lista descendente donde no debería haber resultados."""
        precios = [10, 8, 6, 4, 2]
        k = 3
        self.assertEqual(analyzer(precios, k), 0)

    def test_todos_los_intervalos_son_rentables(self):
        """Prueba una lista completamente creciente."""
        precios = [10, 20, 30, 40, 50]
        k = 3
        # Los intervalos son [10, 20, 30], [20, 30, 40] y [30, 40, 50]
        self.assertEqual(analyzer(precios, k), 3)

    def test_con_precios_iguales_consecutivos(self):
        """Prueba que un aumento no estricto (ej. 5, 5) no se cuenta."""
        precios = [1, 2, 5, 5, 8]
        k = 3
        # El único intervalo válido es [5, 5, 8] que no es estrictamente creciente.
        # No hay intervalos válidos.
        self.assertEqual(analyzer(precios, k), 1)

    def test_caso_borde_k_es_uno(self):
        """Si k=1, cada mes individual es un intervalo válido."""
        precios = [5, 2, 8, 3]
        k = 1
        self.assertEqual(analyzer(precios, k), 4)

    def test_caso_borde_k_demasiado_grande(self):
        """Si k es mayor que la lista de precios, el resultado debe ser 0."""
        precios = [1, 2, 3]
        k = 4
        self.assertEqual(analyzer(precios, k), 0)

    def test_caso_borde_lista_vacia(self):
        """Si la lista de precios está vacía, el resultado debe ser 0."""
        precios = []
        k = 3
        self.assertEqual(analyzer(precios, k), 0)