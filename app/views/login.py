from flask import Blueprint, flash, g, redirect, render_template, \
    request, session, url_for
from app import app, db, forms, login_manager, login_functions, models

login = Blueprint('login', __name__)

@login.route('/login', methods=['GET', 'POST'])
def log_in():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        return oid.try_login(form.openid.data, ask_for=['username', 'password'])
    return render_template('login/login.html',  title='Sign In', form=form,
                            providers=app.config['OPENID_PROVIDERS'])
