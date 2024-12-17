"""Write a function that takes in a Binary Search Tree (BST) and a target integer value and returns the closest value to
that target value contained in the BST. You can assume that there will only be one closest value.
Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if
and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its
value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes
themselves or None / null.

tree =       10
           /    \
         5       15
       /   \    /   \
     2      5  13    22
    /             \
   1              14

target = 12
"""


def find_closest_value_in_bst(tree, target):
    return node_analyzer(tree, target, tree.value)


def node_analyzer(tree, target, closest):
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value  # Actualizar el valor más cercano

    # Continuar la búsqueda en el subárbol izquierdo si el target es menor
    if target < tree.value and tree.left is not None:
        return node_analyzer(tree.left, target, closest)

    # Continuar la búsqueda en el subárbol derecho si el target es mayor
    elif target > tree.value and tree.right is not None:
        return node_analyzer(tree.right, target, closest)

    # Caso base: devolver el valor más cercano
    return closest


def construir_arbol(datos):
    nodos = {}

    # Crear instancias de los nodos y guardarlos en el diccionario
    for nodo in datos["nodes"]:
        nodos[nodo["id"]] = BST(nodo["value"])

    # Establecer las conexiones entre nodos
    for nodo in datos["nodes"]:
        if nodo["left"] is not None:
            nodos[nodo["id"]].left = nodos[nodo["left"]]
        if nodo["right"] is not None:
            nodos[nodo["id"]].right = nodos[nodo["right"]]

    # Devolver el nodo raíz
    return nodos[datos["root"]]


def imprimir_arbol_bst(nodo, nivel=0, prefijo="Root: "):
    """
    Imprime un árbol BST de forma estructurada en consola.
    :param nodo: Nodo actual del árbol (instancia de BST).
    :param nivel: Nivel del nodo en el árbol (para indentación).
    :param prefijo: Etiqueta para la impresión del nodo.
    """
    if nodo is not None:
        # Imprime el nodo actual con indentación según el nivel
        print(" " * (nivel * 4) + prefijo + str(nodo.value))

        # Llama recursivamente para el subárbol izquierdo
        imprimir_arbol_bst(nodo.left, nivel + 1, "L--- ")

        # Llama recursivamente para el subárbol derecho
        imprimir_arbol_bst(nodo.right, nivel + 1, "R--- ")


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
