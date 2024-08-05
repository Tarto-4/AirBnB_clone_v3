#!/usr/bin/python3
"""Index view for API"""

from flask import Blueprint, jsonify

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

@app_views.route('/status', methods=['GET'])
def status():
    """Return the status of the API"""
    return jsonify({"status": "OK"})
