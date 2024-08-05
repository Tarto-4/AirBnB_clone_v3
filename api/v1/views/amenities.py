#!/usr/bin/python3
"""Routes for ammenity objects"""

from flask import jsonify, request
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity

@app_views.route('/amenities', methods=['GET'])
def get_amenities():
    """Retrieve all Amenity objects"""
    amenities = storage.all(Amenity).values()
    return jsonify([amenity.to_dict() for amenity in amenities])

@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    """Retrieve an Amenity object by ID"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        return jsonify(error="Not found"), 404
    return jsonify(amenity.to_dict())

@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    """Delete an Amenity object by ID"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        return jsonify(error="Not found"), 404
    storage.delete(amenity)
    storage.save()
    return jsonify({})

@app_views.route('/amenities', methods=['POST'])
def create_
