from flask import Blueprint, request
from http import HTTPStatus
from flasgger import swag_from
from werkzeug.exceptions import HTTPException

from src.app.schemas.users_schema import UsersSchema
import src.app.controllers.users_controller as user_controller
from src.app.models.users_model import User
import json

user_api = Blueprint('users', 'users')

@user_api.route('/users', methods=['GET'])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Get all users',
            'schema': UsersSchema
        }
    }
})
def user_get():
    users = user_controller.get_users()
    return users

@user_api.route('/users', methods=['POST'])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Add new user',
            'schema': UsersSchema
        }
    }
})
def user_post():
    user = user_controller.add_user(request.json)
    return user

@user_api.route('/users/<string:id>', methods=['PUT'])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Update a user',
            'schema': UsersSchema
        }
    }
})
def user_put(id):
    body = request.json
    body['id'] = id
    res = user_controller.update_user(body)
    return res

@user_api.route('/users/<string:id>', methods=['DELETE'])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Delete a user',
            'schema': UsersSchema
        }
    }
})
def user_delete(id):
    res = user_controller.delete_user(id)
    return res

@user_api.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON format for HTTP errors."""
    response = e.get_response()
    response.data = json.dumps({
        'success': False,
        "message": e.description
    })
    response.content_type = "application/json"
    return response
    