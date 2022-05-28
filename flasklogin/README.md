# CITS3403-Project
CITS3403

- [X] Create Basic Login Page Sign Up
- [X] Allow login to query database for checkins

- [X] Create Signup page
- [X] Allow Signup to add user to new database
- [ ] Research how to allow verification of Value sent to email

# SPLIT EVERYTHING INTO SMALL TASKS
# FOCUS ON ONE THING FIRST SO YOU DONT GET LOST
- [X] setup Database for Images
    - [X] Makepath for images
    - [ ] 

* 
* How does the Front-End request what Photo to pick from in the backend

- [ ] Merge the Login Databases with Front end


#Creating Request Database to route
- [ ] Create 
- [x] Allow Game to query img data from datbase


- [ ] Replace Multiple 
def function():
    import os
    os.listdir(Dynamic path that gets images)


https://github.com/Vuka951/tutorial-code/tree/master/flask-file-upload

pip install flask
pip install flask_bootstrap
pip install flask_sqlalchemy
pip install flask_wtf
pip install sqlalchemy
pip install email_validator
pip install flask_login
pip install pillow
pip install Flask-Migrate


linux install
python3.9 -m venv venv
source venv/bin/activate

enable debug
export FLASK_ENV=development
flask run

from app import db
db.create_all()
exit()

# #Updated PH
# class Player_History(db.Model): #Stores every session for a player
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, nullable=False) #use Username to return results for that username
#     answer_history = db.Column(db.String, nullable=False) #Have Large Sequence
#     answer_count = db.Column(db.Integer, nullable=False)
#     img_id = db.Column(db.Integer, ForeignKey=("ImageTable.id"), primary_key=True)
#     date_submitted = db.Column(db.DateTime, default=datetime.utcnow, server_default=func.now())

#     imagetable = db.relationship('ImageTable', foreign_keys='Player_History.img_id.id')
#     playerhist = db.relationship('ImageTable', foreign_keys='Player_History.Player_History.id')

#     # imagetable = db.relationship('ImageTable', foreign_keys='Player_History.img_id.id', lazy='joined')
#     # playerhist = db.relationship('ImageTable', foreign_keys='Player_History.Player_History.id', lazy='joined')
