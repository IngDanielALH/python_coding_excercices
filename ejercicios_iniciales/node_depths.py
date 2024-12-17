"""
The distance between a node in a Binary Tree and the tree's root is called the node's depth.
Write a function that takes in a Binary Tree and returns the sum of its nodes' depths.
Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be
BinaryTree nodes themselves or None / null.
"""


def nodeDepths(root):
    # Write your code here.
    arr = []
    check_depth(root, 0, arr)
    return sum(arr)
    pass


def check_depth(node, current_depth_sum, depth_arr):
    if node is None:
        return
    new_current_depth = current_depth_sum + 1
    if node.left is None and node.right is None:
        depth_arr.append(new_current_depth)
        return
    check_depth(node.left, new_current_depth, depth_arr)
    check_depth(node.right, new_current_depth, depth_arr)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
