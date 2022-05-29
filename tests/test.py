import unittest, os
from app import PixelPerfect, db
from app.models import Player_history, Images, User

class UserModelCase(unittest.TestCase):
    def setup(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        PixelPerfect.config['SQLALCHEMY_DATABASE_URI']=\
            'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = PixelPerfect.test_client()
        db.create_all()
        s1 = User(user_id = '00000000', username='cammy', email='cam@outlook.com', password = 'what')
        s2 = User(user_id = '00000001', username = 'boo', password = 'lol', email = 'a@a.com')
        db.session.add(s1)
        db.session.add(s2)
        db.session.commit()

    def teardown(self):
        db.session.remove()
        db.drop_all()
    
    def test_password_hashing(self):
        s = User.query.get('00000000')
        s.set_password('test')
        self.assertFalse(s.check_password('case'))
        self.assertTrue(s.checkPassword('test'))
    
    def test_is_committed(self):
        s = User.query.get('00000000')
        self.assertFalse(s.is_committed())
        s2 = User.query.get('11111111')
        self.assertTrue(s.is_committed())

class PlayerModelCase(unittest.TestCase):
    def setup(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        PixelPerfect.config['SQLALCHEMY_DATABASE_URI']=\
            'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = PixelPerfect.test_client()
        db.create_all()
        s1 = Player_history()
