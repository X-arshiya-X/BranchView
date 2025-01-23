from flask import Flask
from controllers.bst_controller import bst_controller
from config.settings import Config

app = Flask(__name__)

# Load the configuration from the settings
app.config.from_object(Config)

# Register the BST controller with the Flask app
app.register_blueprint(bst_controller, url_prefix='/api/bst')

@app.route('/')
def index():
    return "Welcome to the BST API! Use the '/api/bst' endpoint for operations."

if __name__ == '__main__':
    app.run(debug=True)
