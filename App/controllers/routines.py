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

def addWorkout(routine, workout, sets, reps, restTime):
    newRoutineWorkout = RoutineWorkouts(routine, workout, sets, reps, restTime)
    db.session.add(newRoutineWorkout)
    db.session.commit()
    return newRoutineWorkout
    

def removeWorkout(self):
    workout = RoutineWorkouts.query.filter_by(id=self.id).first
    if workout:
        db.session.delete(workout)
        db.session.commit()
        return True
    return None


def get_routine(id):
    routine = Routines.query.get(id)
    return routine if routine else None