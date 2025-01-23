from models.base_bst import BaseBST

class Node:
    def __init__(self, key):
        self.key = key
        self.color = None  # To be set to either RED or BLACK
        self.left = None
        self.right = None
        self.parent = None

class RedBlackBST(BaseBST):
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = "BLACK"  # Sentinel node, color black
        self.root = self.TNULL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert_fixup(self, k):
        while k.parent.color == "RED":
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == "RED":
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == "RED":
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.left_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "BLACK"

    def insert(self, key):
        new_node = Node(key)
        new_node.parent = None
        new_node.key = key
        new_node.left = self.TNULL
        new_node.right = self.TNULL
        new_node.color = "RED"

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if y == None:
            self.root = new_node
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node

        if new_node.parent == None:
            new_node.color = "BLACK"
            return

        if new_node.parent.parent == None:
            return

        self.insert_fixup(new_node)