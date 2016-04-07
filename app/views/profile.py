from flask import Blueprint, render_template
from flask import request, current_app
import requests
from app.static_models import ChampStat, Summoner, Match
from app.mod_riot.functions import *
from app.mod_riot.mapper import *


profile = Blueprint('profile', __name__)

# @profile.route('/profile')
# def test():
#     print request.args
#     return "Hello world"

@profile.route('/profile')
def dashboard():

    RIOT_API_KEY = current_app.config.get('RIOT_API_KEY')
    #print request.args.get
    summonerName = request.args.getlist('summonerName')[0]
    summonerName = summonerName.replace(" ", "") #strip all the whitespaces
    summonerDTO = get_sum_DTO(summonerName, RIOT_API_KEY)
    summonerDTO = summonerDTO[summonerName]

    #generate summoner object
    summoner = Summoner(summonerDTO)

    #get league info
    leagueInfo = get_league(summoner.id, RIOT_API_KEY)
    summoner.league = leagueInfo
    division = roman_to_integer(summoner.league['entries'][0]['division'])
    summoner.medalImage = 'images/medals/' + summoner.league['tier'] + '_' + str(division) + '.png'

    #retrieve ranked stats
    rankedDTO = get_ranked_stats(summoner.id, 'SEASON2016', RIOT_API_KEY)
    #list of champStat instances
    rankedStat = [ChampStat(champ) for champ in rankedDTO if ChampStat(champ).name != None]
    #sort it by games played
    rankedStat.sort(key=lambda x: x.gamesPlayed, reverse=True)

    # ==================================
    #Retrive games stats
    recentGamesDto = get_game_stat(summoner.id, RIOT_API_KEY)
    games = [Game(game) for game in recentGamesDto]
    rawStats = [RawStatsDTO(stat) for stat in games]
    wardsBought = 0
    #Count total number of wards bought
    for rawstat in rawStats:
        wardsBought = wardsBought + rawstat.sightWardsBought + visionWardsBought
    #====================================

    
    

    aggregatedStat = get_aggregated_ranked_stats(summoner.id, 'SEASON2016', RIOT_API_KEY)

    #CURRENT GAME
    teams = get_current_match(summoner.id, RIOT_API_KEY)
    if teams != 404:
        return render_template('profile/profile.html', summoner=summoner
                                                     , rankedStat=rankedStat
                                                     , teams=teams)


    return render_template('profile/profile.html', summoner=summoner
                                                 , rankedStat=rankedStat
                                                 , teams=404)
