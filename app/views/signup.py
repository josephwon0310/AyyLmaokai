from app import db, forms, models
from app.mod_riot import functions as f
from flask import Blueprint, current_app, flash, make_response, redirect
from flask import render_template, request
import requests

signup = Blueprint('signup', __name__)

@signup.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = forms.SignUpForm()

    if request.method == 'POST':
        if (form.password.data == form.confirm.data):
            RIOT_API_KEY = current_app.config.get('RIOT_API_KEY')
            sum_id = f.get_summoner_ID_from_name('KarmicDemon', RIOT_API_KEY)
            hello = f.get_numbered_rank_from_sum_ID(sum_id, RIOT_API_KEY)

            u = models.User(league_name = form.summoner_name.data,
                            password = form.password.data,
                            email = form.email.data,
                            rank = hello)

            db.session.add(u)
            db.session.commit()
        return redirect('/login')

    return render_template('signup/signup.html',  title='Sign Up', form=form)
