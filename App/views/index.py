from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, flash, url_for
from App.models import db
from App.controllers import(
  create_user, 
  createWorkout, 
  createRoutine,
  get_user_by_username,
  getWorkout,
  addWorkout
)

from App.models import User
import csv

from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required,
    current_user,
    set_access_cookies,
    unset_jwt_cookies,
    current_user,
)

index_views = Blueprint('index_views', __name__, template_folder='../templates')

def initialize_db():
  db.drop_all()
  db.create_all()
  user = create_user('bob', 'bobpass', 'bob', 'doe')
  # createRoutine(user, "Chest Routine")
  # createRoutine(user, "Back Routine")

  with open('exercises.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      if row['bodyPart'] == '':
        row['bodyPart'] = None
      if row['equipment'] == '':
        row['equipment'] = None
      if row['name'] == '':
        row['name'] = None
      if row['instructions/0'] == '':
        row['instructions/0'] = None
      if row['instructions/1'] == '':
        row['instructions/1'] = None

      instructions = row['instructions/0'] + row['instructions/1']
      createWorkout(row['name'], row['bodyPart'], row['equipment'], instructions)


  print('database intialized')


@index_views.route('/', methods=['GET'])
def index_page():
  initialize_db()
  bob = User.query.get(1)
  createRoutine(bob, "Chest Routine")
  createRoutine(bob, "Back Routine")
  
  addWorkout(1, 1)
  addWorkout(1, 2)
  addWorkout(1, 3)
  addWorkout(1, 4)

  return render_template('login.html', user=bob)

@index_views.route('/home', methods=['GET'])
@jwt_required()
def home():
  bob = User.query.get(1)

  return render_template('index.html', user=bob)

# @app.route("/app",methods=['GET'])
# @app.route("/app/workouts",methods= ['GET'])
# @jwt_required
# def get_workouts():
#     workouts = Workouts.query.all()
#     workout_list= [workouts.get_json() for workouts in workouts]
#     return jsonify(workout_list)



