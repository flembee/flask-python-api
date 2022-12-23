from src.plugins.Database.database import db
import datetime

class User(db.Model):
    ''' The data model'''
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    role = db.Column(db.Integer(), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    createdAt = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.utcnow)
    updatedAt = db.Column(db.DateTime(), nullable=False, default=datetime.datetime.utcnow)
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}