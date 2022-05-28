import os
import threading
import time
# from scripts import pixelate
from flask_bootstrap import Bootstrap
from flask import Flask,redirect, url_for, Config
    

#Database Modules
from flask_migrate import Migrate

imagepath = 'bmo.png'


# from db import db_init
from .routes import main
# from .models import db

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(main)
    return app
    # migrate = Migrate(app, db)

    # db_init(app) #Create Database

create_app()