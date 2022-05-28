import os
basedir= os.path.abspath(os.path.dirname(__file__))

DB_NAME = 'pixel-perf.db'
DB_NAME2 = 'database.db'

class Config(object):
    
    SECRET_KEY=os.environ.get('SECRET_KEY', 'best-unit-evah')
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI', 'sqlite://' + os.path.join(basedir,DB_NAME2))
    UPLOAD_FOLDER=os.path.join(basedir,'app/static/images/images')
    
# print("this is: "+os.environ.get('DATABASE_URI', 'sqlite://' + os.path.join(basedir,DB_NAME2)))