from flask import Blueprint, render_template

feedback = Blueprint('feedback', __name__)

#Teams
OUR_TEAM = "OURS"
THEIR_TEAM = "THEIRS"

'''
class Game:
    self.out_team = []
    self.their_team = []
    self.did_win = True

class Players(champion, player_name, team):
    self.name = player_name
    self.team =  team
    self.champion = champion
'''

@feedback.route('/feedback')
def create_feedback():
    #get list of last games and player names

    #

    '''
        return them in class structure above
    '''

    return render_template('/feedback/feedback.html')
