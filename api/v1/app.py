#!/usr/bin/python3
"""piw"""
from os import environ
from flask import Flask
from models import storage
from api.v1.views import app_views
app = Flask(__name__)
app.register_blueprint(app_views)
# Register a function to be called when the app context is torn down


@app.teardown_appcontext
def close_storage():
    storage.close()


if __name__ == "__main__":
    """Main Func"""
    host = environ.get("HBNB_API_HOST")
    port = environ.get("HBNB_API_PORT")
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
