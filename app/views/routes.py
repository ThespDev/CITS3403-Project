from datetime import datetime
from flask import render_template, url_for
from app import app
from flask import request
from config import Config
# from .models import User, Player_history
# from flask import Blueprint,redirect, url_for, Config, render_template
# from flask_bootstrap import Bootstrap
# from flask_wtf import FlaskForm 
# from wtforms import StringField, PasswordField, BooleanField
# from wtforms.validators import InputRequired, Email, Length
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import UserMixin, login_user, login_required, logout_user, current_user
# from .database import db
# from .forms import LoginForm, RegisterForm, Users, login_manager
# site = Blueprint('site', __name__, url_prefix="",template_folder='templates')


@site.route('/', methods=['GET','POST'])
def main_index():
    return render_template("index.html")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@site.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #Return values submitted
        # return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>' #data of username/password input submitted
        #Query Database if user exists in the database
        user = Users.query.filter_by(username=form.username.data).first() #Returns Row Object User
        if user: #User Exists!!
            if check_password_hash(user.password, form.password.data): #Password Correct!
                login_user(user, remember=form.username.data)
                return redirect(url_for('site.dash'))

        #username or password doesnt exist
        return '<h1> Invalid username or password </h1>' #

    #not submitted render template
    return render_template('login.html', form=form) # Pass form to template for form object to be used in login.html

    # return render_template(f'login.html', form=form)

@site.route('/signup', methods=['GET','POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        #Do something about sending pincode to email address
        # return '<h1>' + form.username.data + ' ' + form.email.data  +' ' + form.password.data + '</h1>'
        hashed_pass = generate_password_hash(form.password.data, method='sha256') #encoding password for integrity
        
        #Insert Data into DB
        user = Users(username=form.username.data, email=form.email.data, password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        #Some arbritray response
        return '<h1> Successfully added New User! </h1>'
    return render_template('signup', form=form)

#Cannot Access Dashboard without login
@site.route('/dashboard')
@login_required
def dash():
    headings = ["ID", "Username", "Answer_History", "Answer_Count","img_id","DateSubmitted"]
    hist = User_Hist.query.filter_by(username=current_user.username) #Returns Rows
    return render_template('dashboard', name=current_user.username, User_Hist=hist, headings=headings)