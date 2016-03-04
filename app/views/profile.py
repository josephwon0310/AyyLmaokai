from flask import Blueprint, render_template
from flask import request, current_app
import requests
from app.models import ChampStat, Summoner, Match
from app.mod_riot.functions import *
from app.mod_riot.mapper import *


profile = Blueprint('profile', __name__)


@profile.route('/profile', methods=['post'])
def dashboard():

    RIOT_API_KEY = current_app.config.get('RIOT_API_KEY')

    summonerName = request.form['summonerName']
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
    
    aggregatedStat = get_aggregated_ranked_stats(summoner.id, 'SEASON2016', RIOT_API_KEY)
    
    #allMatchDTO = get_match_history(summoner.id, 'SEASON2016', RIOT_API_KEY)
    #matches = [Match(match) for match in allMatchDTO]
    
    return render_template('profile/profile.html', summoner = summoner
                                           , rankedStat=rankedStat)