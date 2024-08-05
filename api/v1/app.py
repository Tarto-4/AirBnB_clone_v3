#!/usr/bin/python3
"""
Module app
"""
from flask import Flask, jsonify, make_response
from flask_cors import CORS
from flasgger import Swagger
from api.v1.views import app_views
from models import storage
from os import getenv

# Create Flask app instance
app = Flask(__name__)

# CORS configuration (allow specific origins if possible)
CORS(app, origins="*")

# Register API blueprint
app.register_blueprint(app_views)

# Initialize Swagger for API documentation
Swagger(app)

@app.errorhandler(404)
def not_found(error):
    """Return a JSON-formatted 404 error message"""
    return make_response(jsonify({"error": "Not found"}), 404)

@app.teardown_appcontext
def teardown(exception):
    """Close the storage session after each request"""
    storage.close()

if __name__ == "__main__":
    # Get host and port from environment variables, or use default values
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(getenv("HBNB_API_PORT", "5000"))
    app.run(host=host, port=port, threaded=True)
