from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import current_user as jwt_current_user

from.index import index_views

from App.models import User

from App.controllers import (
    jwt_required,
    get_routine,
    getWorkout,
    addWorkout,
    update_routine_workout,
    get_routine_workout,
    removeWorkout,
    allWorkouts,
    get_workouts_by_bodyPart
  )

routines_views = Blueprint('routines_views', __name__, template_folder='../templates')

@routines_views.route('/routine/<int:id>', methods=['GET'])
@routines_views.route('/routine/<int:id>/edit-workout/<int:routine_workout_id>', methods=['GET', 'POST'])
@routines_views.route('/routine/<int:id>/view-workouts/<category>', methods=['GET'])
@jwt_required()
def routine_workouts(id, routine_workout_id=1, category="all"):
  exercises= get_workouts_by_bodyPart(category)
  selected_routine = get_routine(id)
  workouts = selected_routine.workouts # workouts has list of routineWorkout objects
  workout = get_routine_workout(routine_workout_id) # workout has record routineWorkout object 
  data=None

  if 'routine_workout_id' in request.view_args:
    routine_workout_id = request.view_args['routine_workout_id']
    
  if request.method == "POST":
    data = request.form
    workout = update_routine_workout(sets=int(data['sets']),reps=int(data['reps']), rest_time=int(data['rest-time']), id=workout.id)
  
  return render_template('routine.html', routine=selected_routine, workouts=workouts, workout=workout, exercises=exercises)

@routines_views.route('/delete/<int:routine_workout_id>', methods=['GET'])
@jwt_required()
def delete_routine_workout_action(routine_workout_id):
  removeWorkout(routine_workout_id)
  return redirect(url_for('routines_views.routine_workouts', id=1))

@routines_views.route('/myroutines', methods=['GET'])
@jwt_required()
def view_my_routines():
  return render_template('views.html', user=jwt_current_user)

# @routines_views.route('/routine/<int:routine_id>/add-workout/<int:routine_workout_id>', methods=['GET', 'POST'])
# @jwt_required()
# def view_my_routines(routine_workout_id):
  