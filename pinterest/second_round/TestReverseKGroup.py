import unittest

from reverse_node_k_groups import reverseKGroup, ListNode


def linked_list_to_list(head):
    """Convierte una lista enlazada de nuevo a una lista de Python."""
    items = []
    current = head
    while current:
        items.append(current.val)
        current = current.next
    return items


def create_linked_list(items):
    """Crea una lista enlazada a partir de una lista de Python."""
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head


class TestReverseKGroup(unittest.TestCase):

    # --- Casos de Prueba ---
    def test_example_one(self):
        """Prueba el ejemplo 1 proporcionado en el problema."""
        head = create_linked_list([1, 2, 3, 4, 5])
        k = 2
        expected = [2, 1, 4, 3, 5]

        result_node = reverseKGroup(head, k)
        result_list = linked_list_to_list(result_node)

        self.assertEqual(result_list, expected)

    def test_example_two(self):
        """Prueba un caso donde k=3 y hay nodos sobrantes."""
        head = create_linked_list([1, 2, 3, 4, 5])
        k = 3
        expected = [3, 2, 1, 4, 5]

        result_node = reverseKGroup(head, k)
        result_list = linked_list_to_list(result_node)

        self.assertEqual(result_list, expected)

    def test_no_leftover_nodes(self):
        """Prueba una lista cuya longitud es un múltiplo exacto de k."""
        head = create_linked_list([1, 2, 3, 4, 5, 6])
        k = 3
        expected = [3, 2, 1, 6, 5, 4]

        result_node = reverseKGroup(head, k)
        result_list = linked_list_to_list(result_node)

        self.assertEqual(result_list, expected)

    def test_k_is_one(self):
        """Prueba el caso donde k=1; la lista no debería cambiar."""
        head = create_linked_list([1, 2, 3, 4, 5])
        k = 1
        expected = [1, 2, 3, 4, 5]

        result_node = reverseKGroup(head, k)
        result_list = linked_list_to_list(result_node)

        self.assertEqual(result_list, expected)

    def test_k_equals_length(self):
        """Prueba cuando k es igual a la longitud de la lista (inversión total)."""
        head = create_linked_list([1, 2, 3, 4, 5])
        k = 5
        expected = [5, 4, 3, 2, 1]

        result_node = reverseKGroup(head, k)
        result_list = linked_list_to_list(result_node)

        self.assertEqual(result_list, expected)

    def test_empty_list(self):
        """Prueba con una lista enlazada vacía."""
        head = create_linked_list([])
        k = 3
        expected = []

        result_node = reverseKGroup(head, k)
        result_list = linked_list_to_list(result_node)

        self.assertEqual(result_list, expected)

    def test_single_node(self):
        """Prueba con una lista de un solo nodo."""
        head = create_linked_list([1])
        k = 1
        expected = [1]

        result_node = reverseKGroup(head, k)
        result_list = linked_list_to_list(result_node)

        self.assertEqual(result_list, expected)
