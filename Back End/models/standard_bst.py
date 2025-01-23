import models.base_bst as BaseBST

class StandardBST(BaseBST):
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, key):
        def _insert(node, key):
            if node is None:
                return self.Node(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)
            return node

        self.root = _insert(self.root, key)

    def search(self, key):
        def _search(node, key):
            if node is None or node.key == key:
                return node
            if key < node.key:
                return _search(node.left, key)
            return _search(node.right, key)

        return _search(self.root, key)

    def delete(self, key):
        def _delete(node, key):
            if not node:
                return node
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                # Node with one or no child
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left

                # Node with two children: get the inorder successor
                temp = self._min_value_node(node.right)
                node.key = temp.key
                node.right = _delete(node.right, temp.key)

            return node

        self.root = _delete(self.root, key)

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
