from tree_node import TreeNode


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
