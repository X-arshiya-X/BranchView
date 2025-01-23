from flask import Blueprint, request, jsonify
from services.bst_factory import BSTFactory
from services.bst_visualizer import BSTVisualizer
from services.tree_operations import TreeOperations
from models.red_black_bst import RedBlackBST
from models.avl_bst import AvlBST
from models.standard_bst import StandardBST
import json

# Create the controller blueprint
bst_controller = Blueprint('bst_controller', __name__)

# Endpoint for creating a BST and inserting nodes
@bst_controller.route('/create_bst', methods=['POST'])
def create_bst():
    # Getting data from the request
    data = request.get_json()
    tree_type = data.get('tree_type')  # Type of BST to create (e.g., 'standard', 'red_black', 'avl')
    nodes = data.get('nodes', [])  # List of nodes to insert into the tree

    # Validate the input
    if tree_type not in ['standard', 'red_black', 'avl', 'balanced']:
        return jsonify({"error": "Invalid tree type"}), 400

    # Create the appropriate BST using the BSTFactory
    tree = BSTFactory.create_bst(tree_type)

    # Insert the nodes into the BST
    for node in nodes:
        tree.insert(node)

    # Return success
    return jsonify({"message": f"{tree_type} BST created and nodes inserted successfully"}), 201

# Endpoint for getting the in-order traversal of a BST
@bst_controller.route('/in_order', methods=['GET'])
def get_in_order():
    # Getting tree type from request args
    tree_type = request.args.get('tree_type')
    nodes = request.args.getlist('nodes', type=int)

    # Validate the input
    if tree_type not in ['standard', 'red_black', 'avl', 'balanced']:
        return jsonify({"error": "Invalid tree type"}), 400

    # Create the appropriate BST using the BSTFactory
    tree = BSTFactory.create_bst(tree_type)

    # Insert the nodes into the BST
    for node in nodes:
        tree.insert(node)

    # Instantiate TreeOperations and get in-order traversal
    tree_operations = TreeOperations()
    in_order_result = tree_operations.inorder_traversal(tree)

    # Return the result
    return jsonify({"in_order": in_order_result})

# Endpoint for visualizing the BST
@bst_controller.route('/visualize', methods=['GET'])
def visualize_bst():
    # Getting tree type from request args
    tree_type = request.args.get('tree_type')
    nodes = request.args.getlist('nodes', type=int)

    # Validate the input
    if tree_type not in ['standard', 'red_black', 'avl', 'balanced']:
        return jsonify({"error": "Invalid tree type"}), 400

    # Create the appropriate BST using the BSTFactory
    tree = BSTFactory.create_bst(tree_type)

    # Insert the nodes into the BST
    for node in nodes:
        tree.insert(node)

    # Visualize the tree using the BSTVisualizer
    visualizer = BSTVisualizer(tree)
    image_path = visualizer.visualize_tree()

    # Return the image path (for simplicity, it could be stored as a static file)
    return jsonify({"message": "Tree visualized", "image_path": image_path})

