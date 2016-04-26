from flask import Blueprint, render_template
from flask import request
from flask import current_app
from app.mod_riot import functions as f
from app.mod_riot import mapper as m
import requests

ban = Blueprint('ban', __name__)

@ban.route('/pickban')
def simulate():
	return render_template('ban/ban.html')

@ban.route('/suggested')
def bans():

    API_KEY = current_app.config.get('CHAMPIONGG_API_KEY')
    highWin = f.get_highest_winrate_champs(API_KEY, 6)
    mostPlayed = f.get_mostplayed_champs(API_KEY, 6)
    mostBanned = f.get_mostbanned_champs(API_KEY, 6)
    
	
    return render_template('ban/suggested.html', highWin=highWin,
                                                 mostPlayed=mostPlayed,
                                                 mostBanned=mostBanned)

@ban.route('/champList')
def test():

	API_KEY=current_app.config.get('RIOT_API_KEY')
	query = request.args.get('search')
	champList=f.get_champ_list(API_KEY)
	return render_template('ban/champList.html',champList=champList,query=query)
	
	