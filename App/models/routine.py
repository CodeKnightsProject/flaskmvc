from App.database import db

class Routine(db.Model):
    __tablename__ = "routine"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    ownerID = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __init__(self, user, name):
        self.name =  name
        self.owner = user

    def get_json(self):
        return{
            'id': self.id,
            'owner': self.user.firstName,
            'Routine name': self.name
        }