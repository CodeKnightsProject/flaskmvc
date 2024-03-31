class Routines(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable = True)
	owner = db.Column(db.Integer, db.ForeignKey('User.id'), nullable = False)

	def rename(self):
		routine = Routines.query.filter_by(id=self.id).first
		if routine:
			routine.name= name
			db.session.add(routine)
			db.session.commit()
			return True
		return None

	addWorkout(self):
		new_workout = workouts.query.filter_by(id=self.id) 

		if not new_workout 
			new_workout = workouts(id = self.id)
			db.session.add(new_workout)
			db.session.commit()

	removeWorkout(self):
		workout = workouts.query.filter_by(id=self.id).first
		if workout:
			db.session.delete(workout)
			db.session.commit()
			return True
		return None