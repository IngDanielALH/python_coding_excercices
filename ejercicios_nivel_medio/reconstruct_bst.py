"""
The pre-order traversal of a Binary Tree is a traversal technique that starts at the tree's root node and visits nodes
in the following order:

    Current node
    Left subtree
    Right subtree

Given a non-empty array of integers representing the pre-order traversal of a Binary Search Tree (BST), write a
function that creates the relevant BST and returns its root node.

The input array will contain the values of BST nodes in the order in which these nodes would be visited with a
pre-order traversal.

Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if
and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left;
its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST
nodes themselves or None / null.
"""


# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, rootIdx):
        self.rootIdx = rootIdx


# O(n) time | O(n) space - where n is the length of the input array
def reconstructBst(preOrderTraversalValues):
    treeInfo = TreeInfo(0)
    return reconstructBstFromRange(float("-inf"), float("inf"), preOrderTraversalValues, treeInfo)


def reconstructBstFromRange(lowerBound, upperBound, preOrderTraversalValues, currentSubtreeInfo):
    if currentSubtreeInfo.rootIdx == len(preOrderTraversalValues):
        return None

    rootValue = preOrderTraversalValues[currentSubtreeInfo.rootIdx]
    if rootValue < lowerBound or rootValue >= upperBound:
        return None

    currentSubtreeInfo.rootIdx += 1
    leftSubtree = reconstructBstFromRange(lowerBound, rootValue, preOrderTraversalValues, currentSubtreeInfo)
    rightSubtree = reconstructBstFromRange(rootValue, upperBound, preOrderTraversalValues, currentSubtreeInfo)

    return BST(rootValue, leftSubtree, rightSubtree)

