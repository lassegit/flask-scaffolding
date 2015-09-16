from flask import request, jsonify, current_app
from sqlalchemy.orm.exc import sa_exc as exc # Catch sql errors
from flask.ext.login import current_user
from app.extensions import cache

def json_error(message = "An error happend", status_code = 500):
    response = jsonify({"message": message})
    response.status_code = status_code

    return response

