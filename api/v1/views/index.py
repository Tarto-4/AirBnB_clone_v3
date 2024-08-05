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
    object_counts = {}
    for cls in storage.all_classes():
        object_counts[cls.__name__] = storage.count(cls)
    return jsonify(object_counts)
