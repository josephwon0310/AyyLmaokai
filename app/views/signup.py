from flask import render_template, Blueprint, flash, redirect
from flask import request, make_response
from flask import current_app
from app import forms
from app import db,models
import requests


signup = Blueprint('signup', __name__)

@signup.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = forms.SignUpForm()
    if request.method == 'POST':
<<<<<<< HEAD

        print "Email: " + form.email.data
        print "Password: " + form.password.data

        #put a random division here because too lazy to
        #actualy get real division
        u = models.User(league_name = form.summoner_name.data,
                        password = form.password.data,
                        email = form.email.data,
                        rank = 6)

        db.session.add(u)
        db.session.commit()
=======
        if (form.password.data == form.confirm.data):
            #put a random division here because too lazy to
            #actualy get real division
            u = models.User(league_name = form.summoner_name.data,
                            password = form.password.data,
                            email = form.email.data,
                            rank = 6)

                db.session.add(u)
                db.session.commit()
>>>>>>> 964e9fef1c401acc892ddb11424a975ef3aa48dd
        return redirect('/login')
    return render_template('signup/signup.html',  title='Sign Up', form=form)
