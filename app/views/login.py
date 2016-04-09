from app import app, db, forms, login_manager, models
from app.models import User
from flask import Blueprint, flash, g, redirect, render_template
from flask import request, session, url_for
from flask.ext.login import login_required, login_user

login = Blueprint('login', __name__)

@login.route('/login', methods=['GET', 'POST'])
def log_in():
    if g.user is not None and g.user.is_authenticated:
        return redirect('/')
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        print user
        print User.query.all()

        if form.password.data == user.password:
            login_user(user)
            return redirect('/')

        return 'Wrong Password'
    return render_template('login/login.html', title='Log In', form=form)

@login.route('/logged_in_temp')
@login_required
def hell():
    return 'Logged in as: ' + g.user.email

@login.route('/logout')
@login_required
def log_out():
    logout_user()
    return redirect(url_for('/'))
