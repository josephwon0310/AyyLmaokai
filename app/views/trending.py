from flask import Blueprint, render_template
from flask import current_app
from app import app
from app import mod_riot

trending = Blueprint('trending', __name__)

class Champion:
    def __init__(self, obj):
        self.name = obj['name']
        self.win_percent = obj['general']['winPercent']
        self.play_percent = obj['general']['playPercent']
        self.ban_rate = obj['general']['banRate']
        self.kills = obj['general']['kills']
        self.deaths = obj['general']['deaths']
        self.assists = obj['general']['assists']
        print "Name" + self.name
        self.image = mod_riot.mapper.get_splash_art(self.name)

    def __repr__(self):
        return "Champion: " + self.name + "\n" + "Kills: " + str(self.kills)

@app.route('/trending')
def trending_champs():
    CHAMPION_GG = current_app.config.get('CHAMPIONGG_API_KEY')
    champs = mod_riot.functions.get_mostplayed_champs(CHAMPION_GG, 10)
    trending_champ_list = []

    for champ in champs:
        champ_to_add = Champion(champ)
        trending_champ_list.append(champ_to_add)

    return render_template('/trending/trending.html', \
        tr_champ_list=trending_champ_list)
