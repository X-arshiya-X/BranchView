class BaseBST:
    """
    Base class for all Binary Search Trees.
    Defines the interface for inserting, deleting, and searching nodes.
    """

    def insert(self, key):
        raise NotImplementedError("Insert method must be implemented by subclasses.")

    def delete(self, key):
        raise NotImplementedError("Delete method must be implemented by subclasses.")

    def search(self, key):
        raise NotImplementedError("Search method must be implemented by subclasses.")
