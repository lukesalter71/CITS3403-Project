from flask import Blueprint
from flask import render_template, redirect, url_for

users = Blueprint('users', __name__)

@users.route("/register")
def register():
    return render_template('register.html', title='Register')

@users.route("/login")
def login():
    return render_template('login.html', title='Login')

@users.route("/logout")
def logout():
    return redirect(url_for('main.home'))

@users.route("/Account")
def account():
    return render_template('account.html', title="Account")