from flask import Blueprint, current_app, render_template, request

from app import app
from app import forms
from app.database import db_session
from firebase import firebase
from firebase_token_generator import create_token

register = Blueprint('register', __name__)

@app.route('/register', methods=['GET', 'POST'])
def register_person():
    FIREBASE_REF = current_app.config.get('FIREBASE_REF')
    FIREBASE_SEC = current_app.config.get('FIREBASE_SECRET')

    form = forms.SignUpForm(request.form)
    fireb = firebase.FirebaseApplication(FIREBASE_REF, None)

    all_users = fireb.get('/users', None)
    print all_users

    #this is horrible but w/e
    if request.method == 'POST':
        #make sure not already shown
        hi = fireb.get('/users/')

        if hi == 'None':
            print hi
            return
        else:
            result = fireb.post('/users/', form.password.data)

        print result

    return render_template('register/register.html', form=form)
