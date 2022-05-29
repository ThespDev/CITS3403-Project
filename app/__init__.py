from ensurepip import bootstrap
import os
# from scripts import pixelate
# from flask_bootstrap import Bootstrap
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
#Database Modules
from flask_migrate import Migrate

imagepath = 'bmo.png'

from .static.routes import site, login_manager

# from .config import Config


basedir= os.path.abspath(os.path.dirname(__file__))
db_name = os.path.join(basedir, 'database.db')
data_name = 'database.db'
print(f'{db_name}')

# db = SQLAlchemy()
from .database import db
# from .static.routes import login_manager

def create_app():
    app = Flask(__name__)

    #Maaz implementation
    # app.config.from_object(Config)
    app.config['SECRET_KEY'] = 'ilovebmo'
    app.config['SQLALCHEMY_DATABASE_URI']=  f'sqlite:///{data_name}'
    app.register_blueprint(site, url_prefix='')
    db.init_app(app)
    Bootstrap(app)

    #Import login manager

    login_manager.init_app(app)
    login_manager.login_view  = 'login'

    #Defines Database Classes
    from .models import Users, User_Hist
    # create_database(app)    

    return app


def create_database(app):
    if not os.path.exists('app' + db_name): 
        db.create_all(app=app)
        print('database Created.')

create_app()
# create_database(app)

# def create_data(app, db):
#     img = Images(name="bmo.jpg", answer="bmo", date=func.now())
#     # usr = User(username="Test", email="test@test.com", password="")


from app.models import Images
from datetime import datetime, timedelta
today = datetime.today()

def get_image(date):
    img = Images.query.filter_by(date=date).first()
    #
    return img
    #parse back to routes.py

# get_image(today)

basedir= os.path.abspath(os.path.dirname('static'))
print('BASED DIR IS' + basedir)
# path = os.path.dirname(basedir)
ARRAY = os.listdir(basedir+'/app/static/images/images/') #Array of Images List
print(f'PATH IS{ARRAY}')
#Inserts array of Images names into database with corresponding dates
def populater():
    present = datetime.today()
    for i in range(len(5)):
        print(present+timedelta(i))