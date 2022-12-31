from flask import Blueprint, request
from http import HTTPStatus
from flasgger import swag_from
from werkzeug.exceptions import HTTPException

from src.app.schemas.users_schema import UsersSchema
import src.app.controllers.auth_controller as auth_controller
import json

auth_api = Blueprint('auth', 'auth')

@auth_api.route('/auth/login', methods=['POST'])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'User Sign in',
            # 'schema': UsersSchema
        }
    }
})
def login():
    token = auth_controller.login(request.json)
    return token

@auth_api.route('/auth/register', methods=['POST'])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'User Sign up',
            # 'schema': UsersSchema
        }
    }
})
def register():
    token = auth_controller.register(request.json)
    return token

@auth_api.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON format for HTTP errors."""
    response = e.get_response()
    response.data = json.dumps({
        'success': False,
        "message": e.description
    })
    response.content_type = "application/json"
    return response
    