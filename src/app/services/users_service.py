from datetime import datetime
from werkzeug.exceptions import NotFound

from src.app.models.users_model import User
from src.plugins.Database.database import db

def get():
    '''
    Get all entities
    :returns: all entity
    '''
    return User.query.all()

def post(body):
    '''
    Create entity with body
    :param body: request body
    :returns: the created entity
    '''

    user = User(**body)
    db.session.add(user)
    db.session.commit()
    return user

def put(body):
    '''
    Update entity by id
    :param body: request body
    :returns: the updated entity
    '''
    user = User.query.get(body['id'])
    if user:
        user = User(**body)
        db.session.merge(user)
        db.session.flush()
        db.session.commit()
        return User.query.get(body['id'])
    raise NotFound('no such entity found with id=' + str(body['id']))

def delete(id):
    '''
    Delete entity by id
    :param id: the entity id
    :returns: the response
    '''
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'success': True}
    raise NotFound('no such entity found with id=' + str(id))

