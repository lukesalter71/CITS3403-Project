from flask import Blueprint, render_template, session, redirect, url_for
from flask_login import login_required, current_user
from . import db, forms

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
    if session['question_number'] == -1:                                                                
        session['question_number'] = 0 
        session.modified = True
    questions = db.Question_Bank.query.filter_by(id=quizid)                                             
    question = questions[session['question_number']]
    answers = []
    for i in question.answers:                                                                         
        answers.append(i.answer_text)
    
    #grab the form object:
    question_form = forms.Question()

    if question.question_type == 2:                                                                     
        question_form.choices = answers                                                                 

    if question_form.validate_on_submit():                                                              

        if question.question_type == 2:
            user_answer = question_form.choices.data                                                    
        elif question.question_type == 1:                                                              
            user_answer = question_form.answer_text.data

        #if int(session['question_number'])+1 == len(questions):                                         
            #return(redirect(url_for('marks', quizid = quizid)))                                         

        session['question_number'] += 1
        session.modified = True
        return(redirect(url_for('quiz',quizid = quizid))) 

    return() #(render_template('quiz.html', title="Quiz", question_form=question_form,question = question))  -- Commented out since 'quiz.html' is not ready.