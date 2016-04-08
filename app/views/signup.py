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
    if form.validate_on_submit():
        flash('Login requested for username="%s", password=%s' % \
        (form.username.data, form.password.data))

        if (form.password.data !== form.confirm.data):
            return

        #put a random division here because too lazy to
        #actualy get real division
        u = models.User(league_name = form.summoner_name.data,
                        password = form.password.data,
                        email = form.password.data,
                        divison = 6)
        db.session.add(u)

        #cheeck to make sure arguments aren't readded to db (can do later)

        db.session.commit()
        return redirect(url_for('/login'))
    return render_template('signup/signup.html',  title='Sign Up', form=form)
