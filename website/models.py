from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    # Database Tables for Courses
class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(128))

class Quizzes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    CourseID = db.Column(db.Integer, db.ForeignKey('Courses.id'))

class Question_Bank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    QuizID = db.Column(db.Integer, db.ForeignKey('Quizzes.id'))
    QuestionText = db.Column(db.String(128))

class MCQ_Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    QuestionID = db.Column(db.Integer,db.ForeignKey('Question_Bank.id'))
    Is_Correct = db.Column(db.Boolean())
    Answer_Text = db.Column(db.String(128))

class Text_Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    QuestionID = db.Column(db.Integer, db.ForeignKey('Question_Bank.id'))

   