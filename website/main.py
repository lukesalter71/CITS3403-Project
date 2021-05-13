from flask import Blueprint, render_template, session, redirect, url_for, flash, request
from flask_login import login_required, current_user
from . import db, forms
import secrets
import os

main = Blueprint('main', __name__)

# Creates a hex name for the picture given in the form
# Saves the new image in the profiles folder
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(main.root_path, 'static/images/profile/', 'picture_fn')
    form_picture.save(picture_path)
    return picture_fn

@main.route('/')
def index():
    return render_template('landing.html')


@main.route('/courses')
@login_required
def home():
    return render_template('courses.html', title='courses')


@main.route('/readmore')
def courses():
    return render_template('readmore.html')

@main.route('/about')
@login_required
def about():
    return render_template('about.html')

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = forms.UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            profile_pic = save_picture(form.picture.data)
            current_user.profile_pic = profile_pic

        current_user.name = form.name.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('main.profile'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.email.data = current_user.email
        
    # profile_pic = url_for('static', filename='images/profile/' + current_user.profile_pic)
    name = current_user.name
    return render_template('profile.html', name=name, form=form)

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

    