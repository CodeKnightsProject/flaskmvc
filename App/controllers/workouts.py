from App.models import Workouts
from App.database import db

def createWorkout(name, bodyPart, equipment, instructions):
  newWorkout = Workouts(name, bodyPart, equipment, instructions)
  db.session.add(newWorkout)
  db.session.commit()
  return newWorkout

def getWorkout(id):
  workout = Workouts.query.get(id)
  if workout:
    return workout
  return None

def allWorkouts():
  return Workouts.query.all()

def get_workouts_by_bodyPart(category):
  if category == "all":
    return Workouts.query.all()
  elif category == "legs":
    return Workouts.query.filter(Workouts.bodyPart.in_(["lower legs", "upper legs"])).all()
  elif category == "arms":
    return Workouts.query.filter(Workouts.bodyPart.in_(["lower arms", "upper arms"])).all()
  else:
    return Workouts.query.filter_by(bodyPart=category).all()