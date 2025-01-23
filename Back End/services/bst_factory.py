from models.standard_bst import StandardBST
from models.avl_bst import AvlBST
from models.red_black_bst import RedBlackTree

class BSTFactory:
    """
    Factory for creating instances of different BST types using a dictionary-based dispatch.
    """

    @staticmethod
    def create_bst(tree_type):
        """
        Create and return a BST instance based on the provided tree type.

        Args:
            tree_type (str): The type of BST to create. Options:
                - 'standard'
                - 'balanced'
                - 'red_black'

        Returns:
            An instance of the requested BST type.

        Raises:
            ValueError: If the provided tree type is not supported.
        """
        # Dispatch table mapping tree types to their corresponding classes
        bst_types = {
            "standard": StandardBST,
            "balanced": AvlBST,
            "red_black": RedBlackTree,
        }

        # Retrieve the class for the given tree_type or raise an exception if unsupported
        if tree_type in bst_types:
            return bst_types[tree_type]()
        else:
            raise ValueError(f"Unknown tree type: {tree_type}")
