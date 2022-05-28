from crypt import methods
from dbm import dumb
from distutils.log import debug
from email.policy import default
from enum import unique
from fileinput import filename
from operator import truediv
from socket import IOCTL_VM_SOCKETS_GET_LOCAL_CID
from time import timezone
from unicodedata import name
from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)
import os
from PIL import Image
import base64
import io

from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime

#Flask DB
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.sql import func


#Py Files

#FORM CLASSES
#------------------
#WILL BREAK IF I MOVE IT TO ANOTHER FILE
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password',validators=[InputRequired(), Length(min=8, max=40)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password',validators=[InputRequired(), Length(min=8, max=40)])
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])

#---------------






# DATABASE_PATH = '/home/seand/Documents/git/CITS3403-Project/flasklogin'
DATABASE_PATH = '/home/seandre/Documents/git/CITS3403-Project/flasklogin'

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'somesecretkeythatonlyishouldknow'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+ DATABASE_PATH +"/database.db"
db = SQLAlchemy(app)
login_manager =LoginManager()
login_manager.init_app(app)
login_manager.login_view  = 'login'
migrate = Migrate(app,db)

#Database Models
#------------------
#user mixin adds 'stuff' to flask db 
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))



class Player_History(db.Model): #Stores every session for a player
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False) #use Username to return results for that username
    answer_history = db.Column(db.String, nullable=False) #Have Large Sequence
    answer_count = db.Column(db.Integer, nullable=False)
    img_id = db.Column(db.Integer, nullable=False)
    # img_id = db.Column(db.Integer, ForeignKey=("ImageTable.id"), primary_key=True)
    date_submitted = db.Column(db.DateTime, default=datetime.utcnow, server_default=func.now())

    # imagetable = db.relationship('ImageTable', foreign_keys='Player_History.img_id.id')
    # playerhist = db.relationship('ImageTable', foreign_keys='Player_History.Player_History.id')

    # imagetable = db.relationship('ImageTable', foreign_keys='Player_History.img_id.id', lazy='joined')
    # playerhist = db.relationship('ImageTable', foreign_keys='Player_History.Player_History.id', lazy='joined')

#Populates Images with Image Data
def image_loader():
    #Get Listdir of images in an array.
    #Parse img array with each index increasing date of todays date
    #commit changes and check with sqlite
    print(f'Task Complete')




class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    answer = db.Column(db.String, unique=True, nullable=False)

    #SQLITE Doesnt have DATE TYP. SQLALCHEMY Uses python Datetime then just cut it off.
    date = db.Column(db.DateTime, default=datetime.utcnow())


#----------------------------


 


@app.route('/signup', methods=['GET','POST'])
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



#Create User Loader, Connection to flask login and actual database
#Create User Loader, Connection to flask login a3nd actual database
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    #Check if form submitted #validate submit
    if form.validate_on_submit():
        #Return values submitted
        # return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>' #data of username/password input submitted
        #Query Database if user exists in the database
        user = User.query.filter_by(username=form.username.data).first() #Returns Row Object User
        if user: #User Exists!!
            if check_password_hash(user.password, form.password.data): #Password Correct!
                login_user(user, remember=form.username.data)
                return redirect(url_for('dash'))

        #username or password doesnt exist
        return '<h1> Invalid username or password </h1>' #

    #not submitted render template
    return render_template('login.html', form=form) # Pass form to template for form object to be used in login.html


#Cannot Access Dashboard without login
@app.route('/dashboard')
@login_required
def dash():
    headings = ["ID", "Username", "Answer_History", "Answer_Count","img_id","DateSubmitted"]
    player_history = Player_History.query.filter_by(username=current_user.username) #Returns Rows
    return render_template('dashboard.html', name=current_user.username, player_history=player_history, headings=headings)



app.config['UPLOAD_FOLDER'] = os.getcwd()+"/static/images"

#if cd in flasklogin
loc = "/static/images"

images = os.listdir(os.getcwd()+loc)



# # Insert One Rows
# IMG_PATH = "/images/Colosseum.jpg"
# IMG_ANSWER = "Colosseum"
# #Creating Simple  Basic image with imagepath
# img = ImageTable(imagepath=IMG_PATH,answer=IMG_ANSWER)
# db.session.add(img)
# db.session.commit()

def populate():
    for index in range(5):
        hist = Player_History(username='Tester123',answer_history=str(index), answer_count=1, img_id=2, date_submitted = datetime.utcnow())
        db.session.add(hist)
        db.session.commit()

    for img in images:
        image = ImageTable(imageName=img,answer=img[:-4],)




#Need to find way to Dynamicly update Image to other Images as it changes
SELECT_IMG_PARAMETER = 2 #Selecting first reow in database
SELECTED_IMG = secure_filename("Colosseum.jpg")

#Img Returning Two Ways

# 1. Process Image, Store in Directory and Map as URL
# 2. Process Image and send images as base64 in frontend

GAMEOVER_RESULTS = [""]

@app.route('/', methods=['POST','GET'])
def index():

    #get image from dir and display
    img = Image.open(app.config['UPLOAD_FOLDER']+"/"+SELECTED_IMG)
    data = io.BytesIO()
    img.save(data,"PNG")
    encode_img_data = base64.b64encode(data.getvalue())

    #Dont need a database to query images
    # image = ImageTable.query.filter_by(id=SELECT_IMG_PARAMETER).first() #Only one return result
    return render_template('index.html', filename=encode_img_data.decode('UTF-8')) #Get image object for Index, Run
    # return render_template('index.html', )
    
    #After Game over do something

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)