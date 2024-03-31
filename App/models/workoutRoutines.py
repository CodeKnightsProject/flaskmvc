class routineWorkouts(db.Model):
	routine_id = db.Column(db.Integer, db.ForeignKey('routines.id'), nullable =False)
	workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable = False)
	sets = db.Column(db.Integer, nullable = False )
	reps = db.Column(db.Integer, nullable = False)
	rest_time = db.Column(db.Integer, nullable = False)
