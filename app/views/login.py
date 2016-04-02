from flask import render_template, Blueprint, flash, redirect
from app import app
from app import forms
from app import db,models

# index view function suppressed for brevity

login = Blueprint('login', __name__)

@login.route('/login', methods=['GET', 'POST'])
def log_in():
    form = forms.LoginForm()
    if form.validate_on_submit():
        flash('Login requested for username="%s", password=%s' % (form.username.data, form.password.data))
    return render_template('login/login.html',  title='Sign In', form=form)
    #return "hi"
