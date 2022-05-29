from .app.app import db
import os
from app.models import Images
from datetime import datetime, timedelta
today = datetime.today()

def get_image(date):
    img = Images.query.filter_by(date=date).first()
    #
    return img
    #parse back to routes.py

get_image(today)

basedir= os.path.abspath(os.path.dirname('static'))
print(basedir)
path = os.path.dirname('static')
ARRAY = os.listdir(path) #Array of Images List
print(ARRAY)
#Inserts array of Images names into database with corresponding dates
def populater():
    present = datetime.today()
    for i in range(len(ARRAY)):
        print(present+timedelta(i))

# populater()