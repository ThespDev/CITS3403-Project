from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# #bcrypt generate_password_hash(), check_generate_password_hash()
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

class User(UserMixin,db.Model):
    # __tablename__='users'

    id = db.Column(db.Integer,primary_key=True)
    username=db.Column( db.String(64),unique=True,nullable=False)
    email=db.Column(db.String(128), unique=True, nullable=False)
    password_hash=db.Column(db.String(128))

    def __init__(self, user_id,username,  email,password):
        self.username = username
        self.password = generate_password_hash(password)
        print(password)

        self.name = username

        self.email = email
    
    def __repr__(self):
        return f'<Usr {self.username}>'
    
    def autheticate_password(self, pwd):
        return check_password_hash(self.password,pwd)
    
   

class Images(db.Model):
    # __tablename__= 'Images'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    answer = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    pf=db.Column(db.String(), nullable=False,server_default="1/1/1/1/1")
    user_hist = db.relationship("Player_history")
    def __init__(self, id,name, answer, date,pf):
        self.name = name
        self.answer=answer
        self.pf=pf
        self.date = date
    def __repr__(self):
        return f'<Image {self.name}, answer {self.answer},date {self.date}>'

class Player_history(db.Model):
    
    # __tablename__= 'player_history'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False) #use Username to return results for that username
    answer_history = db.Column(db.String, nullable=False) #Have Large Sequence
    answer_count = db.Column(db.Integer, nullable=False)
    date_submitted = db.Column(db.String, nullable=False)
    win = db.Column(db.Boolean, default=False, nullable=False)
    img_id = db.Column(db.Integer, db.ForeignKey('images.id'))
    


        

        
        