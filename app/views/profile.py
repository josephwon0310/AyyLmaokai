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
#CHIRP CHIRP HELLO
@profile.route('/profile')
def dashboard():
#SQUAAAAA 307 SQUAAA
    RIOT_API_KEY = current_app.config.get('RIOT_API_KEY')
    #print request.args.get
    summonerName = request.args.getlist('summonerName')[0]
    summonerName = summonerName.replace(" ", "") #strip all the whitespaces
    summonerDTO = get_sum_DTO(summonerName, RIOT_API_KEY)
    
    if summonerDTO == 403:
        return render_template('403.html')
        
    summonerDTO = summonerDTO[summonerName]

    #generate summoner object
    summoner = Summoner(summonerDTO)

    #get league info
    leagueInfo = get_league(summoner.id, RIOT_API_KEY)
    summoner.league = leagueInfo
    division = roman_to_integer(summoner.league['entries'][0]['division'])
    summoner.medalImage = 'images/medals/' + summoner.league['tier'] + '_' + str(division) + '.png'
#i come from vietnam
    #retrieve ranked stats
    rankedDTO = get_ranked_stats(summoner.id, 'SEASON2016', RIOT_API_KEY)
    #list of champStat instances
    rankedStat = [ChampStat(champ) for champ in rankedDTO if ChampStat(champ).name != None]
    #sort it by games played
    rankedStat.sort(key=lambda x: x.gamesPlayed, reverse=True)
            
    aggregatedStat = get_aggregated_ranked_stats(summoner.id, 'SEASON2016', RIOT_API_KEY)
    
    #get champ mastery
    #returns the mastery of top 3 champions
    masteryList = get_champ_mastery(summoner.id, RIOT_API_KEY)
    #switch the order of the mastery so #1 goes in the middle
    masteryList[0], masteryList[1] = masteryList[1], masteryList[0]
    

#hello tvd
    # ==================================
    #Retrive games stats
    wardsBought = 0
    games = get_game_stat(summoner.id, RIOT_API_KEY)
    games = games['games']
    rawStats = []
    winrate = 0
    for game in games:
        stats = game['stats']
        if stats['win'] == True:
            winrate += 1
        if 'visionWardsBought' in stats.keys():
            wardsBought = wardsBought + stats['visionWardsBought']
    
    print winrate
    #winrate of 10 recent games
    

    
    #Count total number of wards bought
        
    #====================================

    
    #what is going on

    aggregatedStat = get_aggregated_ranked_stats(summoner.id, 'SEASON2016', RIOT_API_KEY)

    #CURRENT GAME
    teams = get_current_match(summoner.id, RIOT_API_KEY)
    if teams != 404:
        return render_template('profile/profile.html', summoner=summoner
                                                     , rankedStat=rankedStat
                                                     , teams=teams
                                                     , masteryList=masteryList
                                                     , wardsBought = wardsBought
                                                     , winrate = winrate)

    return render_template('profile/profile.html', summoner=summoner
                                                 , rankedStat=rankedStat
                                                 , teams=404
                                                 , masteryList=masteryList
                                                 , wardsBought = wardsBought
                                                 , winrate = winrate)
