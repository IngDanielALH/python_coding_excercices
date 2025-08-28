"""
You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

**Example 1:**

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
```
"""
from typing import Optional, List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


def print_list(lista):
    for node in lista:
        print(node.val)


def mergeKLists(lists: list[ListNode]) -> ListNode:
    min_heap = []

    # Pista 1: Inicialización correcta del Heap
    # Solo agregamos los nodos cabeza que no son None.
    for head_node in lists:
        if head_node:
            heapq.heappush(min_heap, head_node)

    # Pista 3: Uso correcto del nodo "dummy" o "sentinela"
    # 'head' es el ancla al inicio, 'tail' es el puntero que se mueve.
    head = ListNode()
    tail = head

    # El bucle se ejecuta mientras haya nodos por procesar en el heap.
    while min_heap:
        # Pista 2: Lógica corregida para evitar el bucle infinito.
        # 1. Sacamos el nodo más pequeño y lo guardamos en una variable temporal.
        smallest_node = heapq.heappop(min_heap)

        # 2. Lo enlazamos al final de nuestra lista resultado.
        tail.next = smallest_node

        # 3. Avanzamos nuestro puntero 'tail'.
        tail = tail.next

        # 4. Agregamos el *siguiente* nodo de la lista original al heap, si existe.
        if smallest_node.next:
            heapq.heappush(min_heap, smallest_node.next)

    # Pista 4: Retornar el valor correcto.
    # La lista real comienza después del nodo dummy.
    return head.next


# Versión sin modificar clase inicial
def mergeKLists_2(self, lists: list[ListNode]) -> ListNode:
    min_heap = []
    contador = 0  # Inicializamos el contador único

    for head_node in lists:
        if head_node:
            # Guardamos una tupla en el heap
            valor = head_node.val
            heapq.heappush(min_heap, (valor, contador, head_node))
            contador += 1

    head = ListNode()
    tail = head

    while min_heap:
        # Sacamos la tupla completa
        valor, _, smallest_node = heapq.heappop(min_heap)  # El contador no se usa, lo ignoramos con _

        tail.next = smallest_node
        tail = tail.next

        if smallest_node.next:
            siguiente_nodo = smallest_node.next
            # Agregamos la nueva tupla con el contador actualizado
            heapq.heappush(min_heap, (siguiente_nodo.val, contador, siguiente_nodo))
            contador += 1

    return head.next
