"""Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost branch sum
to rightmost branch sum.vA branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a path
of nodes in a tree that starts at the root node and ends at any leaf node. Each BinaryTree node has an integer value, a
left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.

          1
       /    \
     2       3
   /   \    /   \
  4     5  6     7
 / \   /
8   9 10

Result
[15, 16, 18, 10, 11]

// 15 == 1 + 2 + 4 + 8
// 16 == 1 + 2 + 4 + 9
// 18 == 1 + 2 + 5 + 10
// 10 == 1 + 3 + 6
// 11 == 1 + 3 + 7

"""


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree(data):
    """
    Construye un árbol binario a partir de un diccionario con nodos y una raíz.
    :param data: Diccionario que contiene 'nodes' y 'root'
    :return: Nodo raíz del árbol binario construido
    """
    if not data or 'nodes' not in data or 'root' not in data:
        return None

    nodes = data['nodes']
    root_id = data['root']

    # Crear un mapa de id -> TreeNode
    node_map = {node['id']: BinaryTree(node['value']) for node in nodes}

    # Conectar los nodos
    for node in nodes:
        current_node = node_map[node['id']]
        if node['left'] is not None:
            current_node.left = node_map.get(node['left'])
        if node['right'] is not None:
            current_node.right = node_map.get(node['right'])

    # Devolver la raíz
    return node_map[root_id]


def branchSums(root):
    # Write your code here.
    pass
