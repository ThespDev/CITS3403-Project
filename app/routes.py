
from datetime import datetime
from flask import render_template, url_for, redirect
from app import app, db
from flask import request
from config import Config
from .models import User

#Login Modules
from flask_login import login_user
from .forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash



# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))
@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():
    #print(datetime.now())
    return render_template('index.html')

    
    
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #Return values submitted
        #Query Database if user exists in the database
        user = User.query.filter_by(username=form.username.data).first() #Returns Row Object User
        if user: #User Exists!!
            if check_password_hash(user.password, form.password.data): #Password Correct!
                login_user(user, remember=form.username.data)
                return redirect(url_for('dash'))

                #username or password doesnt exist
        return redirect(url_for('login'))

    #not submitted render template
    return render_template('login.html', form=form) # Pass form to template for form object to be used in login.html
# @app.route('/signup.html')
@app.route('/signup', methods=['GET'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        #Do something about sending pincode to email address
        # return '<h1>' + form.username.data + ' ' + form.email.data  +' ' + form.password.data + '</h1>'
        hashed_pass = generate_password_hash(form.password.data, method='sha256') #encoding password for integrity
        
        #Insert Data into DB
        user = User(username=form.username.data, email=form.email.data, password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        #Some arbritray response
        return '<h1> Successfully added New User! </h1>'
    return render_template('signup.html', form=form)

