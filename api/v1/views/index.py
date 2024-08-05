#!/usr/bin/python3
"""Index route for API status and stats"""

from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/status', methods=['GET'])
def status():
    """Return API status"""
    return jsonify(status="OK")

@app_views.route('/stats', methods=['GET'])
def stats():
    """Return number of objects by type"""
    return jsonify(
        amenities=storage.count("Amenity"),
        cities=storage.count("City"),
        places=storage.count("Place"),
        reviews=storage.count("Review"),
        states=storage.count("State"),
        users=storage.count("User")
    )

@app_views.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify(error="Not found"), 404
