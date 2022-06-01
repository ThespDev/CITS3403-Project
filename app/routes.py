
from datetime import datetime
from flask import render_template, url_for, redirect, flash
from app import app, db
from flask import request
from config import Config
from .models import User

#Login Modules
from flask_login import login_user, login_required, logout_user, current_user, LoginManager, UserMixin

from .forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():
    register_form = RegisterForm()
    login_form = LoginForm()
    return render_template('index.html', register_form=register_form, login_form=login_form)


    
@app.route('/login', methods=['GET','POST'])
def login():
    form1 = LoginForm()
    form2 = RegisterForm()

    if request.method == 'POST':
        if form1.validate_on_submit():
            if request.form['type'] == "login":
                #register login
                print("Login Entered")
                #Return values submitted
                #Query Database if user exists in the database
                user = User.query.filter_by(username=form1.username.data).first() #Returns Row Object User
                if user: #User Exists!!
                    #Typo in Model Class!
                    if user.autheticate_password(form1.password.data): #Password Correct!
                        login_user(user, remember=form1.username.data)
                        flash('Successfully loggin in')
                        return redirect(url_for('index'))
                    flash('Password or Username was incorrect')
                    return redirect(url_for('login'))
                flash('Username does not exist')
                return redirect(url_for('login'))
            
            if request.form['type'] == "signup":
                if isExist(form2.username.data,'username'):
                    flash("ussername already taken")
                    return redirect(url_for('login'))
                if isExist(form2.email.data,'email'):
                    flash("email already in use")
                    return redirect(url_for('login'))
                isExist(form2.email.data,'email')
                user = User(form2.username.data, form2.password.data, form2.email.data)
                db.session.add(user)
                db.session.commit()
                #Some arbritray response
                print('CREATED NEW USER')
                flash('Successfully added New User!')
                return redirect(url_for('login'))

            
            return 'A form has been requested from something other than repsective login/signup forms'
        flash('Error has occured...')
        return 'Error has occured during validate_on_submit()'

    return render_template('login.html', form2 = form2, form1=form1) 
def isExist(item,data): #item can be either username or email
    print("in exist",data)
    if data =='username':
        user = User.query.filter_by(username=item).first() 
        return True
    elif data== 'email':
        user = User.query.filter_by(email=item).first() 
        return True
    return False