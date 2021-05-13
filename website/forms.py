from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Email, Optional, Length, ValidationError
from .models import User
from flask_login import current_user

# Form to update profile details of the user
class UpdateAccountForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email is taken. Please choose a different one.')

# Form for taking question inputs on Course Quizzes.
class Question(FlaskForm):
    choices = RadioField('Answer', validators = [Optional()]) #only is populated if the question is MCQ
    answer_text = TextAreaField('Answer', validators = [Optional(), Length(max=500)]) #only is visible if the quesiton is text-answer.
    submit = SubmitField("Submit") 