from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import current_user as jwt_current_user

from.index import index_views

from App.models import User

from App.controllers import (
    create_user,
    get_all_users,
    get_all_users_json,
    jwt_required,
    get_routine,
    getWorkout,
    addWorkout
)

routines_views = Blueprint('routines_views', __name__, template_folder='../templates')

@routines_views.route('/myroutines', methods=['GET'])
@jwt_required()
def routine_workouts():
  bob = User.query.get(1)

  selected_routine = get_routine(1)
  workout1 = getWorkout(1)
  workout2 = getWorkout(2)
  addWorkout(selected_routine, workout1, 3, 8, 45)
  addWorkout(selected_routine, workout1, 3, 8, 45)
  addWorkout(selected_routine, workout2, 3, 8, 45)
  workouts = selected_routine.workouts

  for w in workouts:
    print(w.workout.name)
  
  return render_template('routine.html', routine=selected_routine, workouts=workouts)