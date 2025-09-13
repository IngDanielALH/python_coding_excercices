# -*- coding: utf-8 -*-
import unittest
from merge_linked_lists import mergeKLists


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


def create_linked_list(items: list[int]) -> ListNode:
    """Crea una lista enlazada a partir de una lista de Python."""
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head


def linked_list_to_list(head: ListNode) -> list[int]:
    """Convierte una lista enlazada de nuevo a una lista de Python."""
    items = []
    current = head
    while current:
        items.append(current.val)
        current = current.next
    return items


class TestMergeKLists(unittest.TestCase):

    def test_example_from_problem(self):
        """Prueba el caso de ejemplo principal."""
        input_lists = [create_linked_list(l) for l in [[1, 4, 5], [1, 3, 4], [2, 6]]]
        expected = [1, 1, 2, 3, 4, 4, 5, 6]

        result_head = mergeKLists(input_lists)
        result_list = linked_list_to_list(result_head)

        self.assertEqual(result_list, expected)

    def test_empty_input_list(self):
        """Prueba con una lista de entrada completamente vacía."""
        input_lists = []
        expected = []

        result_head = mergeKLists(input_lists)
        result_list = linked_list_to_list(result_head)

        self.assertEqual(result_list, expected)

    def test_list_with_empty_sublists(self):
        """Prueba con listas vacías intercaladas."""
        input_lists = [create_linked_list(l) for l in [[1, 3], [], [2, 8]]]
        expected = [1, 2, 3, 8]

        result_head = mergeKLists(input_lists)
        result_list = linked_list_to_list(result_head)

        self.assertEqual(result_list, expected)

    def test_all_sublists_are_empty(self):
        """Prueba cuando todas las listas en la entrada están vacías."""
        input_lists = [create_linked_list(l) for l in [[], [], []]]
        expected = []

        result_head = mergeKLists(input_lists)
        result_list = linked_list_to_list(result_head)

        self.assertEqual(result_list, expected)

    def test_single_element_lists(self):
        """Prueba con varias listas de un solo elemento."""
        input_lists = [create_linked_list(l) for l in [[10], [1], [5]]]
        expected = [1, 5, 10]

        result_head = mergeKLists(input_lists)
        result_list = linked_list_to_list(result_head)

        self.assertEqual(result_list, expected)
