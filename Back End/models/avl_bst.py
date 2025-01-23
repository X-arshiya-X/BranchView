import models.base_bst as BaseBST

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1  # New node is initially at height 1

class AVLTree(BaseBST):
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        if T2:
            T2.parent = z
        y.parent = z.parent
        if z.parent is None:
            self.root = y
        elif z == z.parent.left:
            z.parent.left = y
        else:
            z.parent.right = y
        z.parent = y
        self.update_height(z)
        self.update_height(y)

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        if T3:
            T3.parent = z
        y.parent = z.parent
        if z.parent is None:
            self.root = y
        elif z == z.parent.right:
            z.parent.right = y
        else:
            z.parent.left = y
        z.parent = y
        self.update_height(z)
        self.update_height(y)

    def insert(self, key):
        def insert_node(root, key):
            if root is None:
                return Node(key)
            elif key < root.key:
                root.left = insert_node(root.left, key)
            else:
                root.right = insert_node(root.right, key)

            self.update_height(root)

            balance = self.balance_factor(root)

            if balance > 1 and key < root.left.key:
                return self.right_rotate(root)
            if balance < -1 and key > root.right.key:
                return self.left_rotate(root)
            if balance > 1 and key > root.left.key:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
            if balance < -1 and key < root.right.key:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

            return root

        self.root = insert_node(self.root, key)
