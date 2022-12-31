import os
from dotenv import load_dotenv as ld 
from flask_jwt_extended import (
    JWTManager, create_access_token
)

from config.config import app

ld()

secret_key = os.getenv('SECRET_KEY')

app.config['JWT_SECRET_KEY'] = secret_key
jwt = JWTManager(app)

def generateToken(user):
    payload = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role
    };
    access_token = create_access_token(identity=payload)
    return access_token
