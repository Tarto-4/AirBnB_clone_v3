from flask import jsonify
from api.v1.views import app_views

@app_views.route('/', methods=['GET'])
def index():
    """ Returns a JSON with the status of the API"""
    return jsonify({"status": "OK"})
