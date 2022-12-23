from flask import Blueprint, request
import src.app.controllers.users_controller as user_controller
from src.app.models.users_model import User
from werkzeug.exceptions import HTTPException
import json

user_api = Blueprint('users', 'users')

@user_api.route('/users', methods=['GET'])
def user_get():
    users = user_controller.get_users()
    return users

@user_api.route('/users', methods=['POST'])
def user_post():
    user = user_controller.add_user(request.json)
    return user

@user_api.route('/users/<string:id>', methods=['PUT'])
def user_put(id):
    body = request.json
    body['id'] = id
    res = user_controller.update_user(body)
    return res

@user_api.route('/users/<string:id>', methods=['DELETE'])
def user_delete(id):
    res = user_controller.delete_user(id)
    return res

@user_api.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON format for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        'success': False,
        "message": e.description
    })
    response.content_type = "application/json"
    return response