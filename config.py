import os
basedir= os.path.abspath(os.path.dirname(__file__))
 
class Config(object):
    
    SECRET_KEY=os.environ.get('SECRET_KEY', 'best-unit-evah')
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir,'app.db')
    UPLOAD_FOLDER=os.path.join(basedir,'app/static/images/')
    UPDATE_DELTA=60
