#!/usr/bin/python3
"""
index.py
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/status', methods=['GET'])
def status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'])
def stats():
    """Returns the number of each object by type"""
    classes = ["Amenity", "City", "Place", "Review", "State", "User"]
    object_counts = {}
    
    for cls in classes:
        count = storage.count(cls)
        object_counts[cls.lower() + 's'] = count
    
    return jsonify(object_counts)
