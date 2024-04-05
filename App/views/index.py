from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import create_user

index_views = Blueprint('index_views', __name__, template_folder='../templates')

def initialize_db():
  db.drop_all()
  db.create_all()
  with open('exercises.csv', newline='', encoding='utf8') as csvfile:
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
          if row['instructions/2'] == '':
            row['instructions/2'] = None
          if row['instructions/3'] == '':
            row['instructions/3'] = None
          if row['instructions/4'] == '':
            row['instructions/4'] = None
          if row['instructions/5'] == '':
            row['instructions/5'] = None
          if row['instructions/6'] == '':
            row['instructions/6'] = None
          if row['instructions/7'] == '':
            row['instructions/7'] = None
          if row['instructions/8'] == '':
            row['instructions/8'] = None
          if row['instructions/9'] == '':
            row['instructions/9'] = None
          if row['instructions/10'] == '':
            row['instructions/10'] = None
          
      instructions = row['instructions/0'] + row['instructions/1'] + row['instructions/2'] + row['instructions/3'] + row['instructions/4'] + row['instructions/5'] + row['instructions/6'] + row['instructions/7'] + row['instructions/8'] + row['instructions/9'] + row['instructions/10']
      createWorkout(row['name'], row['bodyPart'], row['equipment'], instructions)
      workouts=Workouts (name=row['name'], bodyPart=row['bodyPart'], equipment=row['equipment'], instructions=instructions)
      i = 1
      while i < 11:
        next_instruction = row['instructions/<i>']
        workouts.instructions.append(next_instruction)
        i+=1
      db.session.add(workouts)


@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    initialize_db()
    create_user('bob', 'bobpass')
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})

@app.route("/app",methods=['GET'])
@app.route("/app/workouts",methods= ['GET'])
@jwt_required
def get_workouts():
    workouts = Workouts.query.all()
    workout_list= [workouts.get_json() for workouts in workouts]
    return jsonify(workout_list)



