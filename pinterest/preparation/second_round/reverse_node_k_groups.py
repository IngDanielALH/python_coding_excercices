"""
Dado el head de una lista enlazada, invierte los nodos de la lista de k en k y devuelve la lista modificada.

k es un entero positivo y es menor o igual a la longitud de la lista enlazada. Si el número de nodos no es un múltiplo
de k, entonces los nodos restantes, al final, deben permanecer como están.

No puedes alterar los valores en los nodos de la lista, solo los nodos mismos pueden ser cambiados.

Ejemplo 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    pass
