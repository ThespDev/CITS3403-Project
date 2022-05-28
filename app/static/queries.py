# from app.__init__ import db
# from app.models import Images
from datetime import datetime, timedelta
today = datetime.today()

def get_image(date):
    img = Images.query.filter_by(date=date).first()
    #
    return img
    #parse back to routes.py

get_image(today)

ARRAY = [6,5,8,6,4,5,3] #Array of Images List

#Inserts array of Images names into database with corresponding dates
def populater():
    present = datetime.today()
    for i in range(len(ARRAY)):
        print(present+timedelta(i))

populater()