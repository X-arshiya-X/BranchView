import os
import graphviz
from models.base_bst import BaseBST

class BSTVisualizer:
    def __init__(self):
        # Path to save the generated images
        self.output_path = os.path.join(os.getcwd(), 'Back-End', 'static')

    def visualize_bst(self, bst: BaseBST):
        """
        Generates a visualization of the BST and saves it as a PNG image.
        
        Args:
            bst (BaseBST): The binary search tree to visualize.
        
        Returns:
            str: The path to the generated image.
        """
        # Create a new Graphviz graph
        graph = graphviz.Digraph(format='png')

        # Generate the graph by traversing the BST (in-order or other traversal methods)
        self._add_nodes_and_edges(graph, bst.root)

        # Output the generated graph to a file
        output_file = os.path.join(self.output_path, 'bst_tree.png')
        graph.render(output_file)

        return output_file

    def _add_nodes_and_edges(self, graph, node):
        """
        Recursively adds nodes and edges to the Graphviz graph.
        
        Args:
            graph (graphviz.Digraph): The graph object to add nodes and edges.
            node (BSTNode): The current node of the BST being processed.
        """
        if node is None:
            return

        # Add the current node to the graph
        graph.node(str(node.value), label=str(node.value))

        # If the node has a left child, create an edge from the current node to the left child
        if node.left:
            graph.edge(str(node.value), str(node.left.value))
            self._add_nodes_and_edges(graph, node.left)

        # If the node has a right child, create an edge from the current node to the right child
        if node.right:
            graph.edge(str(node.value), str(node.right.value))
            self._add_nodes_and_edges(graph, node.right)
