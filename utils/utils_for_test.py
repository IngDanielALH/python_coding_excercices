class TreeNode:
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
    node_map = {node['id']: TreeNode(node['value']) for node in nodes}

    # Conectar los nodos
    for node in nodes:
        current_node = node_map[node['id']]
        if node['left'] is not None:
            current_node.left = node_map.get(node['left'])
        if node['right'] is not None:
            current_node.right = node_map.get(node['right'])

    # Devolver la raíz
    return node_map[root_id]


def are_trees_equal(tree1, tree2):
    """
    Compara si dos árboles binarios son iguales.
    :param tree1: Raíz del primer árbol binario (TreeNode)
    :param tree2: Raíz del segundo árbol binario (TreeNode)
    :return: True si los árboles son iguales, False en caso contrario
    """
    # Si ambos nodos son None, son iguales
    if tree1 is None and tree2 is None:
        return True

    # Si solo uno de los nodos es None, son diferentes
    if tree1 is None or tree2 is None:
        return False

    # Comparar el valor de los nodos actuales y continuar con los subárboles izquierdo y derecho
    return (tree1.value == tree2.value and
            are_trees_equal(tree1.left, tree2.left) and
            are_trees_equal(tree1.right, tree2.right))


def print_tree(node, indent=0):
    if not node:
        return
    print(" " * indent + f"Node({node.value})")
    print_tree(node.left, indent + 2)
    print_tree(node.right, indent + 2)
