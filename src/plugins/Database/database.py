import os
from dotenv import load_dotenv as ld 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config.config import app

ld()

database_url = os.getenv('SQL_DB')
app.config['SQLALCHEMY_DATABASE_URI'] = database_url

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)
