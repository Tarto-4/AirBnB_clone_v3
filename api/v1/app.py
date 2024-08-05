#!/usr/bin/python3

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(self):
    storage.close()


app.register_blueprint(app_views, url_prefix='/api/v1')

if __name__ == "__main__":
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
