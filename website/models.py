from flask_login import UserMixin
from . import db

# models
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Score(db.Model):
    __tablename__ = 'score'
    __table_args__ = {'extend_existing': True}
    userid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    score = db.Column(db.Integer)