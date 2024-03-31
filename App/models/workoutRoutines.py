class routineWorkouts(db.Model):
	routine_id = db.Column(db.Integer, db.ForeignKey('routines.id'), nullable =False)
	workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable = False)
