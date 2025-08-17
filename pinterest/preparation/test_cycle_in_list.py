import unittest
from cycle_in_list import has_cycle


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class TestHasCycle(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(has_cycle(None), 0)

    def test_single_node_no_cycle(self):
        head = SinglyLinkedListNode(1)
        self.assertEqual(has_cycle(head), 0)

    def test_single_node_with_cycle(self):
        head = SinglyLinkedListNode(1)
        head.next = head  # El nodo apunta a sí mismo.
        self.assertEqual(has_cycle(head), 1)

    def test_simple_list_no_cycle(self):
        node1 = SinglyLinkedListNode(1)
        node2 = SinglyLinkedListNode(2)
        node3 = SinglyLinkedListNode(3)
        node1.next = node2
        node2.next = node3
        self.assertEqual(has_cycle(node1), 0)

    def test_list_with_cycle_at_end(self):
        node1 = SinglyLinkedListNode(1)
        node2 = SinglyLinkedListNode(2)
        node3 = SinglyLinkedListNode(3)
        node1.next = node2
        node2.next = node3
        node3.next = node2  # El ciclo se crea aquí: 3 -> 2
        self.assertEqual(has_cycle(node1), 1)

    def test_list_with_cycle_to_head(self):
        node1 = SinglyLinkedListNode(1)
        node2 = SinglyLinkedListNode(2)
        node3 = SinglyLinkedListNode(3)
        node1.next = node2
        node2.next = node3
        node3.next = node1  # El ciclo se crea aquí: 3 -> 1
        self.assertEqual(has_cycle(node1), 1)

    def test_list_with_duplicate_data_no_cycle(self):
        node1 = SinglyLinkedListNode(1)
        node2 = SinglyLinkedListNode(2)
        node3 = SinglyLinkedListNode(1)  # Un nodo diferente, pero con el mismo dato.
        node1.next = node2
        node2.next = node3
        self.assertEqual(has_cycle(node1), 0)
