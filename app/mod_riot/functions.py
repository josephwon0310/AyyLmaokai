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
            champion['id'] = map_champions(champion['id'])
        
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

#returns the json object of the Champion static data
def get_champion_data(API_KEY):
    pass


#returns the json object of the current game
def get_current_game():
    pass

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

