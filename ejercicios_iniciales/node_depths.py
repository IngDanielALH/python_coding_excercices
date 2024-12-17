"""
The distance between a node in a Binary Tree and the tree's root is called the node's depth.
Write a function that takes in a Binary Tree and returns the sum of its nodes' depths.
Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be
BinaryTree nodes themselves or None / null.
"""


def nodeDepths(root):
    return helper(root, 0)
    pass


def helper(node, depth):
    if node is None:
        return 0

    # Suma de la profundidad actual más las profundidades de los subárboles
    left_depths = helper(node.left, depth + 1)
    right_depths = helper(node.right, depth + 1)

    return depth + left_depths + right_depths
