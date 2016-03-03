from flask import Blueprint, render_template
from app import app

trending = Blueprint('trending', __name__)

'''
    This is a multiline comment wtf?????

    Either way the request gives a data array that has objects in
    this format:

       data: [
      {
        key: "LeeSin",
        role: "Jungle",
        name: "Lee Sin",
        general: {
          winPercent: 48.08,
          playPercent: 35.06,
          banRate: 3.56,
          experience: 108.12,
          kills: 6.75,
          deaths: 6.07,
          assists: 9.06,
          totalDamageDealtToChampions: 14632,
          totalDamageTaken: 28749,
          totalHeal: 5831,
          largestKillingSpree: 3.16,
          minionsKilled: 37.5,
          neutralMinionsKilledTeamJungle: 53.15,
          neutralMinionsKilledEnemyJungle: 8.84,
          goldEarned: 11335,
          overallPosition: 20,
          overallPositionChange: -1
        }

        so we send these as objects to the layout to update w/e
'''

@app.route('/trending')
def trending_champs():
    #get stats of all champs ordered by most played
    trending_champ_list = []
    #take only first ten champs
    trending_champ_list = trending_champ_list[0:10]

    return render_template('/trending/trending.html', tr_champ_list=trending_champ_list)
