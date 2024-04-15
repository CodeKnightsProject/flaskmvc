import click, pytest, sys, csv
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, createRoutine, createWorkout, addWorkout, getWorkout )
from App.models import Routines
# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    db.drop_all()
    db.create_all()

    user = create_user('bob', 'bobpass', 'bob', 'doe')
    routine1 = createRoutine(user, "Chest Routine")
    # routine2 = createRoutine(user, "Back Routine")
    
    # print(routine.owner.firstName)

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


    workout1 = getWorkout(1)
    workout2 = getWorkout(2)
    workout3 = getWorkout(3)
    workout4 = getWorkout(4)
    workout4 = getWorkout(10)

    # print(workout4.name)

    addWorkout(1, 1)
    addWorkout(1, 2)
    addWorkout(1, 3)
    addWorkout(1, 4)

    for routine in user.routines:
        # print(routine.name)
        for workout in routine.workouts:
            print(workout.sets)

    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)