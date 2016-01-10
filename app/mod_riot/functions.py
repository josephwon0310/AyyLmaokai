'''
Python wrapper file for RiotGames API
'''
import requests
import json

SUMMONER_URL = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner'
STATS_URL = 'https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/'

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
    
#returns the json object of the ranked stats data 
def get_ranked_stats(sum_ID, API_KEY, season):
    
    url = '{}/{}/ranked?season={}&api_key={}'.format(STATS_URL, sum_ID, season, API_KEY)
    r = requests.get(url)
    
    if r.status_code == 200:
        return r.json()
    elif r.status_code == 404: #ranked stats not found
        return 404