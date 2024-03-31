from App.models import User, Routine
from App.database import db

def create_user(username, password, fname, lname):
    newuser = User(username, password, fname, lname)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def createRoutine(user, name):
    newRoutine = Routine(user, name)
    db.session.add(newRoutine)
    db.session.commit()
    return newRoutine



def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    