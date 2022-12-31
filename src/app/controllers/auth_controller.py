import bcrypt

import src.plugins.Authentication.authentication as auth_plugin
import src.app.services.users_service as user_service

def login(body):
    '''Sign in with email and password'''
    user = user_service.get_by_email(body['email'])

    if user:
        password = body['password'].encode('utf-8')
        pasword_matched = bcrypt.checkpw(password, user.password.encode('utf-8'))
        if pasword_matched:
            token = auth_plugin.generateToken(user)
            return "Bearer " + token
        else:
            return "Password does not match"
    else:
        return "The email does not exists"

def register(body):
    '''Check if user exists and register'''
    user = user_service.get_by_email(body['email'])

    if user:
        return "Email already exists"
    else:
        password = body['password'].encode('utf-8')
        salt = bcrypt.gensalt()
        body['password'] = bcrypt.hashpw(password, salt)
        new_user = user_service.post(body)

        if new_user:
            token = auth_plugin.generateToken(new_user)
            return "Bearer " + token
        else:
            return "Cannot created the new user"
