from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Courses(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(128))


class Quizzes(db.Model):
    __tablename__ = 'quizzes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    # created one-to-many relationship between quizzes and questions.
    questions = db.relationship('Question_Bank', backref = 'quizzes', lazy='joined')


class Question_Bank(db.Model):
    __tablename__ = 'question_bank'
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'))
    question_type = db.Column(db.Integer) # 1 - Text Answer, 2 - Multi-choice
    question_text = db.Column(db.String(128))
    #created one-to-many relationship between answers and question. 
    answers = db.relationship('Answer', backref = 'question_bank', lazy = 'joined')

class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.column(db.Integer, primary_key = True)
    question_id = db.Column(db.Integer, db.ForeignKey('question_bank.id'))
    is_correct = db.Column(db.Boolean())
    answer_text = db.Column(db.String(128))

class Enrolments(db.Model):
    __tablename__ = 'enrolments'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    course_id = db.Column(db.Integer,db.ForeignKey('courses.id'))