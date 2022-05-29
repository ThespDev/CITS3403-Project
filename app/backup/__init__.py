import os
from flask import Flask
from flask import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app= Flask(__name__)
app.config.from_object(Config)  

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY']=SECRET_KEY

basedir= os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir,'app.db')
app.config['SQLALCHEMY_DATABASE_URI']= SQLALCHEMY_DATABASE_URI


db = SQLAlchemy(app)
migrate=Migrate(app,db)


from app import routes,api,models
from .models import User,Player_history,UserMixin,Images
from app import PixelPerfect
# PixelPerfect.initialiseGame()




