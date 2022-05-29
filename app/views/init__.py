import os
from flask import Flask
from flask import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#Sean
# from flask_bootstrap import Bootstrap
# from .database import db
# from config import Config
# from app.models import Images
# from datetime import datetime, timedelta
# from .routes import site, login_manager


app= Flask(__name__)
app.config.from_object(Config)  

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY']=SECRET_KEY

basedir= os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir,'app.db')
app.config['SQLALCHEMY_DATABASE_URI']= SQLALCHEMY_DATABASE_URI


db = SQLAlchemy(app)
# db.init_app(app)
migrate=Migrate(app,db)
# Bootstrap(app)
# login_manager.init_app(app)
# login_manager.login_view  = 'login'
# app.register_blueprint(site)

from app import routes,api,models
from .models import User,Player_history,UserMixin,Images
from app import PixelPerfect
# PixelPerfect.initialiseGame()




