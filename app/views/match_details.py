from flask import Blueprint, render_template
from flask import request, current_app
from app.mod_riot.functions import *
from app.mod_riot.mapper import *
from app.static_models import Match

match_details = Blueprint('match_details', __name__)
@match_details.route('/match_details')
def board():
    searchword = request.args.get('id', '')
    RIOT_API_KEY = current_app.config.get('RIOT_API_KEY')
    match = get_match(RIOT_API_KEY,searchword)
    totalGoldBlueTeam = 0
    totalGoldRedTeam = 0
    participants = match['participants']
    for participant in participants:
    	if participant['teamId'] == 100:
    		totalGoldBlueTeam = totalGoldBlueTeam + participant['stats']['goldEarned']
    	else :
    		totalGoldRedTeam = totalGoldRedTeam + participant['stats']['goldEarned']
    print totalGoldRedTeam
    print '\n\n\n'
    print totalGoldBlueTeam
    print '\n\n\n'	
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('match_details/match_details.html', totalGoldRedTeam = totalGoldRedTeam
    														 , totalGoldBlueTeam = totalGoldBlueTeam)