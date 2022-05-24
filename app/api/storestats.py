#class Player_History(db.Model): #Stores every session for a player
#    id = db.Column(db.Integer, primary_key=True)
 #   username = db.Column(db.String, nullable=False) #use Username to return results for that username
 #   answer_history = db.Column(db.String, nullable=False) #Have Large Sequence
 #   answer_count = db.Column(db.Integer, nullable=False)
 #   img_id = db.Column(db.Integer, nullable=False)
 #   date_submitted = db.Column(db.DateTime, nullable=True)
 #MONTH DAY YEAR
from app import app, db
from flask import jsonify, url_for, request
from app.api.errors import bad_request, error_response
from app.models import Player_History, Image_Table
from datetime import date
from flask_login import AnonymousUserMixin, current_user
app.routes('/api/storestats',methods=['POST'])
def store():
    today = date.today()
    date = today.strftime("%m/%d/%Y")
    data = request.json
    Image_Table.query.filter_by(date=date)
    username = current_user
    ans = data['answer_history']
    count = data['answer_count']
    img_id = None
    player = Player_History.query.filter_by(username=username).all()[-1]
    if player.date_submitted == date:
        return error_response(409, "You've already submitted a score today")
    elif (current_user is AnonymousUserMixin):
        return error_response(409, "Anonymous User, score won't be saved")
    else:
        submission = Player_History(username,ans,count,img_id,date)
        db.session.add(submission)
        db.session.commit()



