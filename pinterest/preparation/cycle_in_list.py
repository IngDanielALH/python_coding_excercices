"""
A linked list is said to contain a cycle if any node is visited more than once while traversing the list.
Given a pointer to the head of a linked list, determine if it contains a cycle. If it does, return 1. Otherwise,
return 0.

Example

head refers to the list of nodes 1 → 2 → 3 → NULL

The numbers shown are the node numbers, not their data values. There is no cycle in this list so return 0.

head refers to the list of nodes 1 → 2 → 3 → 1 → NULL

There is a cycle where node 3 points back to node 1, so return 1.

Function Description

Complete the has_cycle function in the editor below.

It has the following parameter:

    SinglyLinkedListNode pointer head: a reference to the head of the list

Returns

    int: 1 if there is a cycle or 0 if there is not

Note: If the list is empty, head will be null.
"""


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def has_cycle(head: SinglyLinkedListNode):
    current_node = head
    visited = set()
    while current_node is not None:
        if current_node in visited:
            return 1
        visited.add(current_node)
        current_node = current_node.next
    return 0
    pass
