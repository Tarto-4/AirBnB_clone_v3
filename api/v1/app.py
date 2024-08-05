#!/usr/bin/python3
"""
app.py
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exception):
    """Closes the storage session"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """Returns a JSON-formatted 404 error response"""
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(host=getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(getenv('HBNB_API_PORT', 5000)),
            threaded=True)
