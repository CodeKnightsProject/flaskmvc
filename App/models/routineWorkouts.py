from App.database import db

class RoutineWorkouts(db.Model):
	__tablename__ = "routineWorkouts"
	id = db.Column(db.Integer, primary_key=True)
	routine_id = db.Column(db.Integer, db.ForeignKey('routine.id'), nullable =False)
	workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable = False)
	sets = db.Column(db.Integer, nullable = False )
	reps = db.Column(db.Integer, nullable = False)
	rest_time = db.Column(db.Integer, nullable = False)
	

	# routines = db.relationship('Routine', back_populates='workouts'
	workout = db.relationship('Workouts')

	def __init__(self, routine, workout, sets, reps, restTime):
		self.routine = routine
		self.workout = workout
		self.sets = sets
		self.reps = reps
		self.rest_time = restTime
		self.routine_id = routine.id
		self.workout_id = workout.id


