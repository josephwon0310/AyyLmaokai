'''
Python wrapper file for RiotGames API
'''
import requests
import json

from mapper import *

DATADRAGON = 'http://ddragon.leagueoflegends.com'
SUMMONER_URL = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner'
STATS_URL = 'https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner'
LEAGUE_URL = 'https://na.api.pvp.net/api/lol/na/v2.5/league'
GAME_URL = 'https://na.api.pvp.net/api/lol/na/v1.3/game/by-summoner'
CHAMPIONGG = 'http://api.champion.gg/stats'

#returns the json formatted summary of the requested summoner.
#Includes ID, name, profileIconID, level, and revisionDate
def get_sum_DTO(sum_name, API_KEY):
    
    url = '{}/by-name/{}?api_key={}'.format(SUMMONER_URL, sum_name, API_KEY)
    r = requests.get(url)

    if r.status_code == 200:
        return r.json()
    elif r.status_code == 404: #summoner name not found
        return 404

#returns the json formatted summary of the mastery pages.
def get_masteries(sum_ID, API_KEY):
    
    url = '{}/{}/masteries?api_key{}'.format(SUMMONER_URL, sum_ID, API_KEY)
    r = requests.get(url)
    
    return r.json()
    
#returns the list of json objects
def get_ranked_stats(sum_ID, season, API_KEY):
    
    #url = '{}/{}/ranked?season={}&api_key={}'.format(STATS_URL, sum_ID, season, API_KEY)
    url = '{}/{}/ranked?season={}&api_key={}'.format(STATS_URL, sum_ID, season ,API_KEY)
    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()
        rankedChampions = data['champions']#list of json objects
        
        #maps the data one to one
        for champion in rankedChampions:
            champion['id'] = map_champions(champion['id'])#replaces the id to the champion names
        
        return rankedChampions
        
    elif r.status_code == 404: #ranked stats not found
        return 404

def get_general_stats(sum_ID, API_KEY, season):
    
    url = ''
    r = requests.get(url)
    
    if r.status_code == 200:
        return r.json()
    elif r.status_code == 404: #stats not found, most likely wrong summoner_ID
        return 404

#returns the json object of the challenger tier
def get_challenger_list(API_KEY):
    
    url = '{}/challenger?type=RANKED_SOLO_5x5&api_key={}'.format(LEAGUE_URL, API_KEY)
    r = requests.get(url)
    
    if r.status_code == 200:
        return r.json()
    elif r.status_code == 404:
        return 404

#returns the json object of the recent match history and stats
#Grab the data with json['games']
def get_game_stat(sum_ID, API_KEY):
    
    url ='{}/{}/recent?api_key={}'.format(GAME_URL, sum_ID, API_KEY)
    r = requests.get(url)
    
    if r.status_code == 200:
        return r.json()
    elif r.status_code == 404:
        return 404
        
        
#=======CHAMPION GG INTEGRATION============

#returns a json object of most played champions
def get_mostplayed_champs(API_KEY, limit):
    
    url = "{}/champs/mostPlayed?api_key={}&page=1&limit={}".format(CHAMPIONGG, API_KEY, limit)
    r = requests.get(url)
    
    if r.status_code == 200:
        data = r.json()['data'] #list of json objects
        return data
        
    elif r.status_code == 404:
        return 404


#functions for pick/ban/win rate 
def get_highest_winrate_champs(API_KEY, limit):
    url = "{}/champs/mostWinning?api_key={}&page=1&limit={}".format(CHAMPIONGG, API_KEY, limit)

   # url = 'http://api.champion.gg/stats/champs/mostWinning?api_key=e0430f17c1fc4b8be9747087bde46f41&page=1&limit=2'
    r = requests.get(url)

    if r.status_code == 200:
        data = r.json() #returns dicgtionary
        return data

    elif r.status_code == 404:
        return 404

#def get_mostbanned_champs():
