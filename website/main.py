from flask import Blueprint, render_template
from flask_login import login_required, current_user
from website import website, db, forms

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('landing.html')


@main.route('/home')
@login_required
def home():
    return render_template('homepage.html', title='Home')


@main.route('/readmore')
def courses():
    return render_template('readmore.html')


#Quiz taking view function (todo)
@main.route('/quiz/<quizid>', methods=['GET','POST'])
@login_required
def quiz(quizid):
    questions = db.Question_Bank.query.filter_by(id=quizid) #extract the given quiz's questions from the question_bank table into an array.
    currentquestion = 0
    question = questions[currentquestion]
    answers = []
    for i in question.answers:
        answers.append(i.answer_text)
    return ()
