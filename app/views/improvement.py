from app.mod_riot import functions as f
from flask import Blueprint, current_app, render_template

improvement = Blueprint('improvement', __name__)

@improvement.route('/improvement')
def show_improve():
    RIOT_API_KEY = current_app.config.get('RIOT_API_KEY')
    sum_id = f.get_summoner_ID_from_name('KarmicDemon', RIOT_API_KEY)
    hello = f.get_numbered_rank_from_sum_ID(sum_id, RIOT_API_KEY)
    return str(hello)

    #get change data from Database make model

    #store a new change data to user everytime they get on this page

    #return data to frontend

    #extra variables
    #return render_template('improvement/improvement.html', title='Improvement')
