#!/usr/bin/python3
"""Routes for City objects"""

from flask import jsonify, request
from api.v1.views import app_views
from models import storage
from models.city import City
from models.state import State

@app_views.route('/states/<state_id>/cities', methods=['GET'])
def get_cities(state_id):
    """Retrieve all City objects of a State"""
    state = storage.get(State, state_id)
    if state is None:
        return jsonify(error="Not found"), 404
    cities = storage.all(City).values()
    return jsonify([city.to_dict() for city in cities if city.state_id == state_id])

@app_views.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    """Retrieve a City object by ID"""
    city = storage.get(City, city_id)
    if city is None:
        return jsonify(error="Not found"), 404
    return jsonify(city.to_dict())

@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """Delete a City object by ID"""
    city = storage.get(City, city_id)
    if city is None:
        return jsonify(error="Not found"), 404
    storage.delete(city)
    storage.save()
    return jsonify({})

@app_views.route('/states/<state_id>/cities', methods=['POST'])
def create_city(state_id):
    """Create a new City object"""
    state = storage.get(State, state_id)
    if state is None:
        return jsonify(error="Not found"), 404
    if not request.is_json:
        return jsonify(error="Not a JSON"), 400
    data = request.get_json()
    if 'name' not in data:
        return jsonify(error="Missing name"), 400
    data['state_id'] = state_id
    city = City(**data)
    city.save()
    return jsonify(city.to_dict()), 201

@app_views.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    """Update a City object by ID"""
    if not request.is_json:
        return jsonify(error="Not a JSON"), 400
    data = request.get_json()
    city = storage.get(City, city_id)
    if city is None:
        return jsonify(error="Not found"), 404
    for key, value in data.items():
        if key not in ["id", "state_id", "created_at", "updated_at"]:
            setattr(city, key, value)
    city.save()
    return jsonify(city.to_dict())
