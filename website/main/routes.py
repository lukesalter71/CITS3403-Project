from flask import Blueprint
from flask import render_template

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return render_template('homepage.html', title='Home')


