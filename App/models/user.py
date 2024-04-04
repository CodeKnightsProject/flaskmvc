from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    firstName = db.Column(db.String(120), nullable=False)
    lastName = db.Column(db.String(120), nullable=False)
    routines = db.relationship('Routines', backref='owner')

    def __init__(self, username, password, fname, lname):
        self.username = username
        self.firstName = fname
        self.lastName = lname
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username,
            'First Name' : self.firstName,
            'Last Name' : self.lastName
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

