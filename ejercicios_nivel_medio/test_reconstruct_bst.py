import unittest
from reconstruct_bst import reconstructBst
from utils import utils_for_test


class TestReconstructBST(unittest.TestCase):
    def test_1(self):
        input_array = [10, 4, 2, 1, 5, 17, 19, 18]
        tree_info = {
            "nodes": [
                {"id": "2", "left": "0", "right": "4", "value": 2},
                {"id": "4", "left": "3", "right": None, "value": 4},
                {"id": "3", "left": None, "right": "3-2", "value": 3},
                {"id": "3-2", "left": None, "right": None, "value": 3},
                {"id": "0", "left": None, "right": "1", "value": 0},
                {"id": "1", "left": None, "right": None, "value": 1}
            ],
            "root": "2"
        }
        expected = utils_for_test.build_tree(tree_info)

        generated_tree = reconstructBst(input_array)
        # Imprimir árboles para depuración
        print("Expected Tree:")
        utils_for_test.print_tree(expected)
        print("Generated Tree:")
        utils_for_test.print_tree(generated_tree)

        self.assertTrue(utils_for_test.are_trees_equal(expected, generated_tree))

