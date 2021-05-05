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
    if session['question_number'] == -1:                                                                #Checking that all the pre-requisites for taking a quiz have been met.
        session['question_number'] = 0 
        session.modified = True
    questions = db.Question_Bank.query.filter_by(id=quizid)                                             #extract the given quiz's questions from the question_bank table into an array.
    question = questions[session['question_number']]
    answers = []
    for i in question.answers:                                                                          #extract the current question's answers from the database.
        answers.append(i.answer_text)
    
    #grab the form object:
    question_form = forms.Question()

    if question.question_type == 2:                                                                     #If the question is a multiple-choice question
        question_form.choices = answers                                                                 #set the radio buttons to the question's choices

    if question_form.validate_on_submit():                                                              #POST Request

        if question.question_type == 2:
            user_answer = question_form.choices.data                                                    #takes whichever response the user chooses
        elif question.question_type == 1:                                                               #not using else, as another category of answer may be added in the sites future.
            user_answer = question_form.answer_text.data

        #check if the answered question is the last in the quiz:
        #if int(session['question_number'])+1 == len(questions):                                         # e.g. the 5th question on a 5-question quiz would have session['question_number'] = 4. Hence the +1.
            #return(redirect(url_for('marks', quizid = quizid)))                                         #redirect to the marks screen (not ready yet, so commented this out.)

        #since any quiz that has passed the final question would have redirected at this point, we can safely move to the next question
        session['question_number'] += 1
        session.modified = True
        return(redirect(url_for('quiz',quizid = quizid))) 

    return () #GET Requests will go to the quiz page template (using render_template)