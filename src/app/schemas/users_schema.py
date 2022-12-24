from flask_marshmallow import Schema
from marshmallow.fields import Str, Int, DateTime


class UsersSchema(Schema):
    class Meta:
        fields = ['id', 'name', 'email', 'role', 'password', 'createdAt', 'updatedAt']

    id = Int()
    name = Str()
    email = Str()
    role = Int()
    password = Str()
    createdAt = DateTime()
    updatedAt = DateTime()