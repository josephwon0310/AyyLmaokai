from app.mod_riot import functions
from app.static_models import Summoner
from flask import Blueprint, current_app, g, render_template
from flask.ext.login import login_required

current_game = Blueprint('current_game', __name__)

@current_game.route('/current_game')
@login_required
def render_game():
    #check if actually in game
    RIOT_API_KEY = current_app.config.get('RIOT_API_KEY')
    summoner = functions.get_sum_DTO(g.user.league_name, RIOT_API_KEY)
    summoner = summoner[g.user.league_name.lower()]
    summoner = Summoner(summoner)
    in_game = functions.get_current_match(summoner.id, RIOT_API_KEY)

    if (in_game != 404):
        return render_template('current_game/in_game_stats.html', in_game=in_game)
    else:
        return render_template('current_game/not_in_game.html')
