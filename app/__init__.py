import os
from flask import Flask
from flask import Config, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_login import LoginManager
#Sean
from flask_bootstrap import Bootstrap
from config import Config
from datetime import datetime, timedelta


app= Flask(__name__)
app.config.from_object(Config)  

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY']=SECRET_KEY

basedir= os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir,'app.db')
app.config['SQLALCHEMY_DATABASE_URI']= SQLALCHEMY_DATABASE_URI


db = SQLAlchemy(app)
migrate=Migrate(app,db)

# from forms import *
login_manager = LoginManager()

site = Blueprint('site', __name__, url_prefix="",template_folder='templates')
Bootstrap(app)
login_manager.init_app(app)
login_manager.login_view  = 'login'
# app.register_blueprint(site)

from app import routes,api,models
from .models import User,Player_history,UserMixin,Images
from app import PixelPerfect
app.register_blueprint(site)

# PixelPerfect.initialiseGame()




