# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# from db import db

# #Database Models
# #------------------
# #user mixin adds 'stuff' to flask db 
# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(15), unique=True)
#     email = db.Column(db.String(50), unique=True)
#     password = db.Column(db.String(80))



# class Player_History(db.Model): #Stores every session for a player
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, nullable=False) #use Username to return results for that username
#     answer_history = db.Column(db.String, nullable=False) #Have Large Sequence
#     answer_count = db.Column(db.Integer, nullable=False)
#     img_id = db.Column(db.Integer, nullable=False)
#     date_submitted = db.Column(db.DateTime, nullable=True)


# class ImageTable(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     imageName = db.Column(db.String, unique=True, nullable=False)
#     answer = db.Column(db.String, unique=True, nullable=False)
#     # mimetypes = db.Column(db.Text, nullable=False)

# # class DateTable(db.Model):
