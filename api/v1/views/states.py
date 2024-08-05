from flask import jsonify, request
from models import State
from api.v1.views import app_views


@app_views.route('/states', methods=['GET', 'POST'])
def states_list():
    """ Retrieves all State objects or creates a new State object"""
    if request.method == 'GET':
        all_states = [state.to_dict() for state in State.all()]
        return jsonify(all_states)

    if request.method == 'POST':
        new_state = State(**request.get_json())
        new_state.save()
        return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['GET', 'PUT', 'DELETE'])
def state_detail(state_id):
    """ Retrieves a specific State object, updates it, or deletes it"""
    state = State.get(state_id)
    if not state:
        return jsonify({"error": "Not found"}), 404

    if request.method == 'GET':
        return jsonify(state.to_dict())

    if request.method == 'PUT':
        state.update(**request.get_json())
        state.save()
        return jsonify(state.to_dict()), 200

    if request.method == 'DELETE':
        State.delete(state_id)
        return jsonify({}), 200
