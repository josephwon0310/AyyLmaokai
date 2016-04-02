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
        flash('Login requested for username="%s", password=%s' % (form.username.data, form.password.data))
        u = models.User(league_name = form.username.data)
        db.session.add(u)
        db.session.commit()
    return render_template('login/login.html',  title='Sign In', form=form)