from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Questions(db.Model):
    __tablename__ = "questions"
    __table_args__ = {'extend_existing': True}
    question_id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String, nullable=False)
    question = db.Column(db.String, nullable=False)
    option1 = db.Column(db.String, nullable=True)
    option2 = db.Column(db.String, nullable=True)
    option3 = db.Column(db.String, nullable=True)
    option4 = db.Column(db.String, nullable=True)
    answer = db.Column(db.Integer, nullable=True)
    bcol = db.Column(db.String, nullable=True)

class Score(db.Model):
    __tablename__ = 'score'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    score = db.Column(db.Integer)