from flask import send_from_directory

from backend import app
from backend.models import *


@app.route('/api/ping')
def ping():
    return {"status": "pong"}

@app.errorhandler(404)
def catch_all(filename):
    try:
        return send_from_directory(app.static_folder, filename)
    except:
        return {"status": "Error"}, 500

@app.errorhandler(500)
def catch_error(*args):
    return "Internal Error from server"
