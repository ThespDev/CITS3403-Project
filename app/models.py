from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# @login.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

class User(db.Model,UserMixin):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key=True)
    username=db.Column( db.String(64),unique=True,nullable=False)
    email=db.Column(db.String(128), unique=True, nullable=False)
    password_hash=db.Column(db.String(128))
    # img_id = db.Column(db.Integer, db.ForeignKey('images.id'))
    db.relationship('Player_history',backref='user')

    def __init__(self,username, password, email):
        # self.id=user_id
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        print(password)

    def set_password(self,password):
        self.password_hash=generate_password_hash(password)
    
    def __repr__(self):
        # return f'<User {self.username}>'
        return f'<Image {self.username}, answer {self.email}>'
    def autheticate_password(self, password):
        return check_password_hash(self.password_hash,password)
    
   

class Images(db.Model):
    __tablename__= 'images'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    answer = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    pf=db.Column(db.String(), nullable=False,server_default="1/1/1/1/1")
    # user_hist = db.relationship("Player_history")
    db.relationship('Player_history',backref='image')

    def __init__(self,name, answer, date,pf):
        self.name = name
        self.answer=answer
        self.pf=pf
        self.date = date
    def __repr__(self):
        return f'<Image {self.name}, answer {self.answer},date {self.date}>'

class Player_history(db.Model):
    
    __tablename__= 'player_history'
    id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String, nullable=False) #use Username to return results for that username
    answer_history = db.Column(db.String, nullable=False) #Have Large Sequence
    answer_count = db.Column(db.Integer, nullable=False)
    date_submitted = db.Column(db.String, nullable=False)
    win = db.Column(db.Boolean, default=False, nullable=False)
    user=db.Column(db.Integer,db.ForeignKey("users.id"), nullable=False)
    image=db.Column(db.Integer, db.ForeignKey("images.id"), nullable=False)
    
    # img_id = db.Column(db.Integer, db.ForeignKey('images.id'))
    


        

        
        