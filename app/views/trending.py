from flask import Blueprint, render_template
from flask import current_app
from app import app
from app import mod_riot
from app import models

trending = Blueprint('trending', __name__)

@app.route('/trending')
def trending_champs():
    CHAMPION_GG = current_app.config.get('CHAMPIONGG_API_KEY')
    champs = mod_riot.functions.get_mostplayed_champs(CHAMPION_GG, 10)
    trending_champ_list = []

    for champ in champs:
        champ_to_add = models.Champion(champ)
        trending_champ_list.append(champ_to_add)

    return render_template('/trending/trending.html', \
        tr_champ_list=trending_champ_list)
