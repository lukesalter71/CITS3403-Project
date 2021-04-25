from flask import Blueprint, render_template
from flask_login import login_required, current_user

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
