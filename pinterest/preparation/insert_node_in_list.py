"""

Given a pointer to the head node of a linked list and an integer to insert at a certain position, create a new node
with the given integer as its data attribute, insert this node at the desired position, and return the head node.

A position of 0 indicates the head, a position of 1 indicates one node away from the head, and so on. The head pointer
given may be null, meaning that the initial list is empty.

Example

head refers to the first node in the list 1 → 2 → 3
data = 4
position = 2

Insert a node at position 2 with data = 4. The new list is 1 → 2 → 4 → 3.

Function Description

Complete the function insertNodeAtPosition with the following parameters:

    SinglyLinkedListNode pointer llist: a reference to the head of the list

    int data: an integer value to insert in the new node

    int position: an integer position to insert the new node, zero-based indexing

Returns

    SinglyLinkedListNode pointer: a reference to the head of the revised list

Input Format

The first line contains an integer n, the number of elements in the linked list.
Each of the next n lines contains an integer SinglyLinkedListNode[i].data.
The next line contains an integer data, the data that is to be inserted.
The last line contains an integer position.

"""


class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertNodeAtPosition(head, data, position):
    p1 = None
    p2 = head
    current_position = 0
    new_node = SinglyLinkedListNode(data)

    while True:
        if current_position == position:
            if current_position == 0:
                new_node.next = p2
                break
            else:
                p1.next = new_node
                new_node.next = p2
                break
        else:
            p1 = p2
            p2 = p1.next
            current_position += 1
    return head if current_position != 0 else new_node
    pass


def print_linked_list(node):
    """
    Función auxiliar para imprimir la lista enlazada.
    """
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")


def test_1():
    print("Inicio test_1")
    head = SinglyLinkedListNode(16)
    node_1 = SinglyLinkedListNode(13)
    node_2 = SinglyLinkedListNode(7)

    head.next = node_1
    node_1.next = node_2

    print_linked_list(head)

    new_list = insertNodeAtPosition(head, 1, 2)
    print_linked_list(new_list)


def test_2():
    print("Inicio test_2")
    head = SinglyLinkedListNode(16)
    node_1 = SinglyLinkedListNode(13)
    node_2 = SinglyLinkedListNode(7)

    head.next = node_1
    node_1.next = node_2

    print_linked_list(head)

    new_list = insertNodeAtPosition(head, 1, 0)
    print_linked_list(new_list)


def test_3():
    print("Inicio test_3")
    head = SinglyLinkedListNode(16)
    node_1 = SinglyLinkedListNode(13)
    node_2 = SinglyLinkedListNode(7)

    head.next = node_1
    node_1.next = node_2

    print_linked_list(head)

    new_list = insertNodeAtPosition(head, 1, 3)
    print_linked_list(new_list)


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
