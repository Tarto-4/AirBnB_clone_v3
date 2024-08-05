#!/usr/bin/python3
"""Index view for API"""

from flask import Blueprint, jsonify
from models import storage

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

@app_views.route('/status', methods=['GET'])
def status():
    """Return the status of the API"""
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'])
def stats():
    """Retrieve the number of each object by type"""
    classes = ["Amenity", "City", "Place", "Review", "State", "User"]
    stats = {}
    for cls in classes:
        cls_name = cls.lower() + 's'
        stats[cls_name] = storage.count(eval(cls))
    return jsonify(stats)
