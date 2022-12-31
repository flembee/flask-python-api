from flask import jsonify
import bcrypt
import src.app.services.users_service as user_service

def get_users():
    ''' Get all entities'''
    users = user_service.get()
    return jsonify([user.as_dict() for user in users])

def add_user(body):
    ''' Create entity'''
    password = body['password'].encode('utf-8')
    salt = bcrypt.gensalt()
    body['password'] = bcrypt.hashpw(password, salt)
    user = user_service.post(body)
    return jsonify(user.as_dict())

def update_user(body):
    ''' Update entity by id'''
    user = user_service.put(body)
    return jsonify(user.as_dict())

def delete_user(id):
    ''' Delete entity by id'''
    res = user_service.delete(id)
    return jsonify(res)
