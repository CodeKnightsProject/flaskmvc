from App.models import Routines, Workouts, RoutineWorkouts
from App.database import db

def createRoutine(user, name):
    newRoutine = Routines(user, name)
    db.session.add(newRoutine)
    db.session.commit()
    return newRoutine

def rename(self, name):
    routine = Routines.query.filter_by(id=self.id).first()
    if routine:
        routine.name= name
        db.session.add(routine)
        db.session.commit()
        return True
    return None

def addWorkout(routine_id, workout_id):
    exist=RoutineWorkouts.query.filter_by(routine_id=routine_id, workout_id=workout_id).first()
    if exist:
        return None
    
    newRoutineWorkout = RoutineWorkouts(routine_id, workout_id, 3, 8, 45)
    db.session.add(newRoutineWorkout)
    db.session.commit()
    return newRoutineWorkout
    

def removeWorkout(id):
    workout = RoutineWorkouts.query.filter_by(id=id).first()
    if workout:
        db.session.delete(workout)
        db.session.commit()
        return True
    return None

def get_routine(id):
    routine = Routines.query.get(id)
    return routine if routine else None

def update_routine_workout(id, sets, reps, rest_time):
    workout = RoutineWorkouts.query.get(id)
    workout.sets = sets
    workout.reps = reps
    workout.rest_time = rest_time
    db.session.add(workout)
    db.session.commit()
    return workout

def get_routine_workout(id):
    workout = RoutineWorkouts.query.get(id)
    if workout:
        return workout
    
    return None


def delete_routine(id):
    routine = Routines.query.filter_by(id=id).first()

    if routine.workouts:
        for r in routine.workouts:
            removeWorkout(r.id)
    
    if routine:
        db.session.delete(routine)
        db.session.commit()
        return True
    return None
