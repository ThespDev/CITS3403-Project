import os
import threading
# from scripts import pixelate
# from flask_bootstrap import Bootstrap
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

#Database Modules
from flask_migrate import Migrate
from flasklogin.app import Images, User

imagepath = 'bmo.png'
from flask_login import LoginManager

from .static.routes import site, login_manager

# from .config import Config


basedir= os.path.abspath(os.path.dirname(__file__))
db_name = os.path.join(basedir, 'database.db')
data_name = 'database.db'
print(f'{db_name}')

# db = SQLAlchemy()
from .database import db
from .static.routes import login_manager

# def create_database():
app = Flask(__name__)

#Maaz implementation
# app.config.from_object(Config)
app.config['SECRET_KEY'] = 'ilovebmo'
app.config['SQLALCHEMY_DATABASE_URI']=  f'sqlite:///{data_name}'
app.register_blueprint(site, url_prefix='')
db.init_app(app)

#Import login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view  = 'login'

#Defines Database Classes
from .models import User, User_Hist, Images
# create_database(app)    

# return app


def create_database(app):
    if not os.path.exists('app' + db_name): 
        db.create_all(app=app)
        print('database Created.')

create_app()

def create_data(app, db):
    img = Images(name="bmo.jpg", answer="bmo", date=func.now())
    # usr = User(username="Test", email="test@test.com", password="")
