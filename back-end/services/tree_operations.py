from models.base_bst import BaseBST
from models.standard_bst import StandardBST
from models.avl_bst import AvlBST
from models.red_black_bst import RedBlackBST

class TreeOperations:
    def __init__(self):
        self.bst = None

    def create_bst(self, tree_type: str, values: list) -> BaseBST:
        """
        Create a BST of the specified type and insert values into it.
        """
        if tree_type == 'standard':
            self.bst = StandardBST()
        elif tree_type == 'AVL':
            self.bst = AvlBST()
        elif tree_type == 'red_black':
            self.bst = RedBlackBST()
        else:
            raise ValueError("Invalid tree type. Choose from 'standard', 'AVL', or 'red_black'.")
        
        for value in values:
            self.bst.insert(value)

        return self.bst

    def inorder_traversal(self, bst: BaseBST) -> list:
        """
        Perform an in-order traversal of the BST.
        """
        return self._inorder_helper(bst.root)

    def _inorder_helper(self, node) -> list:
        if node is None:
            return []
        # Ensure the correct attribute ('key' or 'value') is used based on the implementation
        return self._inorder_helper(node.left) + [node.key] + self._inorder_helper(node.right)

    def search(self, bst: BaseBST, value: int) -> bool:
        """
        Search for a value in the BST.
        """
        return bst.search(value)
