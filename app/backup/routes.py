
from datetime import datetime
from flask import render_template, url_for
from app import app
from flask import request
from config import Config



@app.route('/')
@app.route('/index')
def index():
    #print(datetime.now())
    return render_template('index.html')

    
    
@app.route('/login.html')
def login():
    return render_template('login.html')

