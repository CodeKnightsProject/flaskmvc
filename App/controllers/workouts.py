from App.models import Workouts
from App.database import db

def createWorkout(name, bodyPart, equipment, instructions):
    newWorkout = Workouts(name, bodyPart, equipment, instructions)
    db.session.add(newWorkout)
    db.session.commit()
    return newWorkout