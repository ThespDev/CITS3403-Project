from crypt import methods
from distutils.log import debug
from enum import unique
from fileinput import filename
from operator import truediv
from socket import IOCTL_VM_SOCKETS_GET_LOCAL_CID
from xmlrpc.client import DateTime
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
from datetime import datetime


from loginforms import *
from flask_sqlalchemy import SQLAlchemy


# DATABASE_PATH = '/home/seand/Documents/git/CITS3403-Project/flasklogin'
DATABASE_PATH = '/home/seand/Documents/gitrepo/CITS3403-Project/flasklogin'



app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'somesecretkeythatonlyishouldknow'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+ DATABASE_PATH +"/database.db"
login_manager =LoginManager()
login_manager.init_app(app)
login_manager.login_view  = 'login'
db = SQLAlchemy(app)



#Database Models
#------------------
#user mixin adds 'stuff' to flask db 
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))


class ImageTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_name = db.Column(db.String, unique=True, nullable=False)
    answer = db.Column(db.String, unique=True, nullable=False)
    date_time = (db.DateTime)
    pixel_factor = db.Column(db.String, nullable=False)
    # mimetypes = db.Column(db.Text, nullable=False)

# img = ImageTable(img_name="whatever",answer="bmo",date_time=today,pixel_factor="10-20-30-40")
# db.session.add(img)
# db.session.commit()



class Player_History(db.Model): #Stores every session for a player
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False) #use Username to return results for that username
    answer_history = db.Column(db.String, unique=True, nullable=False) #Have Large Sequence
    answer_count = db.Column(db.Integer, nullable=False)
    img_id = db.Column(db.Integer, nullable=False)
    date_submitted = (db.DateTime)

#Insert some basic images into  

# def reinitialise():
#     #Restart the Database Creator
#     db.create_all()

# reinitialise()

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
    return render_template('dashboard.html', name=current_user.username)



#OS Path
# picfolder = os.path.join('static','images')
# print(picfolder)

app.config['UPLOAD_FOLDER'] = '/home/seand/Documents/gitrepo/CITS3403-Project/flasklogin/static/images'


# # Insert One Row
# IMG_PATH = "/images/Colosseum.jpg"
# IMG_ANSWER = "Colosseum"
# #Creating Simple  Basic image with imagepath
# img = ImageTable(imagepath=IMG_PATH,answer=IMG_ANSWER)
# db.session.add(img)
# db.session.commit()

# def populate():
    # for index in range(5):
    #     hist = Player_History(username='Tester123',answer_history=str(index), answer_count=1, img_id=2, date_submitted = datetime.utcnow())
    #     db.session.add(hist)
    #     db.session.commit()


#Need to find way to Dynamicly update Image to other Images as it changes
SELECT_IMG_PARAMETER = 2 #Selecting first reow in database
SELECTED_IMG = secure_filename("Colosseum.jpg")

#Img Returning Two Ways

# 1. Process Image, Store in Directory and Map as URL
# 2. Process Image and send images as base64 in frontend

GAMEOVER_RESULTS = [""]

@app.route('/', methods=['POST','GET'])
def index():

    # #get image from dir and display
    # img = Image.open(app.config['UPLOAD_FOLDER']+"/"+SELECTED_IMG)
    # data = io.BytesIO()
    # img.save(data,"PNG")
    # encode_img_data = base64.b64encode(data.getvalue())
    return render_template("index copy.html")
    # return render_template('index.html', filename=encode_img_data.decode('UTF-8')) #Get image object for Index, Run
    


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)