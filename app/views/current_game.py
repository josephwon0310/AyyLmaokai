from flask import Blueprint, render_template

current_game = Blueprint('current_game', __name__)

@current_game.route('/current_game')
def render_game():
    #check if actually in game
    in_game = False

    if (in_game):
        return render_template('/current_game/in_game_stats')
    else:
        return render_template('/current_game/not_in_game')
