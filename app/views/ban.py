from flask import Blueprint, render_template
from flask import request
from flask import current_app
from app.mod_riot import functions as f
from app.mod_riot import mapper as m
import requests

ban = Blueprint('ban', __name__)

@ban.route('/ban')
def bans():
	API_KEY = current_app.config.get('CHAMPIONGG_API_KEY')
	highWin = f.get_highest_winrate_champs(API_KEY, 6)['data']
	mostPlayed = f.get_mostplayed_champs(API_KEY, 6)['data']
	mostBanned = f.get_mostbanned_champs(API_KEY, 6)['data']
	return render_template('ban/ban.html', highWin = highWin, mostPlayed = mostPlayed, mostBanned = mostBanned)