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


def insertNodeAtPosition(llist, data, position):
    pass


if __name__ == "__main__":
    print("Inicio del programa")
    head = SinglyLinkedListNode(16)
    node_1 = SinglyLinkedListNode(13)
    node_2 = SinglyLinkedListNode(7)

    head.next = node_1
    node_1.next = node_2

    insertNodeAtPosition(head, 1, 2)
