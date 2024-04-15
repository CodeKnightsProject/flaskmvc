from App.database import db

class Routines(db.Model):
	__tablename__ = "routine"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable = True)
	ownerID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
	workouts = db.relationship('RoutineWorkouts', backref='routine')

	def __init__(self, user, name):
		self.name =  name
		self.owner = user

	def get_json(self):
		return{
			'id': self.id,
			'owner': self.owner.firstName,
			'Routine name': self.name
		}

