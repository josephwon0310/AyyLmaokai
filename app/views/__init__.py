from app import app, db, login_manager
from app.models import User
from flask import g, flash, redirect, url_for
from flask.ext.login import current_user

@app.before_request
def before_request():
    g.user = current_user

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'

@login_manager.request_loader
def request_load(request):
    print request
    user = User.query.filter(User.email == " ").first()
    if user is None:
        return
    return user

@login_manager.user_loader
def load_user(email):
    return User.query.filter(User.email == email).first()
