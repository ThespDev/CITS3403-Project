from db import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from datetime import datetime
from flask_login import UserMixin


#Image to Player-Hist One to Many


#Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

#Child to Images
class User_Hist(db.Model): #Stores every session for a player
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False) #use Username to return results for that username
    answer_history = db.Column(db.String, nullable=False) #Have Large Sequence
    answer_count = db.Column(db.Integer, nullable=False)
    
    img_id = db.Column(db.Integer, Foreignkey=("images.id"))
    

    #Add img_name and Change Img Id as FK

    # img_id = db.Column(db.Integer, ForeignKey=("ImageTable.id"), primary_key=True)
    date_submitted = db.Column(db.DateTime, default=datetime.utcnow, server_default=func.now())

class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    answer = db.Column(db.String, unique=True, nullable=False)

    #SQLITE Doesnt have DATE TYP. SQLALCHEMY Uses python Datetime then just cut it off.
    date = db.Column(db.DateTime, default=datetime.utcnow())

    usr_hst = db.relationship("User_Hist")