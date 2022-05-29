import os
from re import template
from flask import Flask
from flask import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from datetime import datetime, timedelta

app= Flask(__name__)
app.config.from_object(Config)  

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY']=SECRET_KEY

basedir= os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir,'app.db')
app.config['SQLALCHEMY_DATABASE_URI']= SQLALCHEMY_DATABASE_URI

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate=Migrate(app,db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import routes,api,models
from .models import User,Player_history,UserMixin,Images
from app import PixelPerfect
# PixelPerfect.initialiseGame()


# def populate():
ARRAY = os.listdir('/home/seandre/Documents/git/CITS3403-Project/app/static/images/landscapes') #Array of Images List
present = datetime.today()
for i in range(len(ARRAY)):
    time = present+timedelta(i)
    dates = datetime.strftime(time, "%d/%m/%Y")
    # print(dates)
    img = Images(name=ARRAY[i],answer=ARRAY[i][:-4],date=dates, pf="1/1/1/1/1")
    db.session.add(img)
    db.session.commit()
# populate()

