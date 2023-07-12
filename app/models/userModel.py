from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Users(db.Model):
    id= db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    username = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    password = db.Column(db.Text(100))
    role = db.Column(db.Enum('user', 'admin',
                     nullable=False, server_default="user", name='role_type'))

    def __init__(self, username, name):
        self.username = username
        self.name = name    

    def setPassword(self, password):
        self.password = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.password, password)