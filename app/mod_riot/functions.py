'''
Python wrapper file for RiotGames API
'''
import requests
import json

from mapper import *

CHAMPIONGG = 'http://api.champion.gg/stats'
CURRENT_MATCH = 'https://na.api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/NA1'
DATADRAGON = 'http://ddragon.leagueoflegends.com'
GAME_URL = 'https://na.api.pvp.net/api/lol/na/v1.3/game/by-summoner'
LEAGUE_URL = 'https://na.api.pvp.net/api/lol/na/v2.5/league'
MASTERY = 'https://na.api.pvp.net/championmastery/location/NA1/player'
MATCH_URL = 'https://na.api.pvp.net/api/lol/na/v2.2/match'
MATCH_HISTORY_URL = 'https://na.api.pvp.net/api/lol/na/v2.2/matchlist/by-summoner'
STATS_URL = 'https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner'
SUMMONER_URL = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner'

#returns the list of aggregated champ stat
def get_champion_data(champion, API_KEY):
    url = '{}/champs/{}?api_key={}'.format(CHAMPIONGG, champion, API_KEY)
    r = requests.get(url)

    if r.status_code == 200:
        return r.json()
    elif r.status_code == 404:
        return 404

#returns the top 3 mastery of the summoner
def get_champ_mastery(sum_ID, API_KEY):
    url = '{}/{}/topchampions?api_key={}'.format(MASTERY, sum_ID, API_KEY)
    r = requests.get(url)

    if r.status_code == 200:
        data = r.json() #this is a list of top 3 champs
        for champion in data:
            champion['championId'] = map_champions(champion['championId'])
        return data
    elif r.status_code == 404:
        return 404

#returns the json formatted summary of the requested summoner.
#Includes ID, name, profileIconID, level, and revisionDate
def get_sum_DTO(sum_name, API_KEY):
    url = '{}/by-name/{}?api_key={}'.format(SUMMONER_URL, sum_name, API_KEY)
    r = requests.get(url)

    if r.status_code == 200:
        return r.json()

    elif r.status_code == 403:
        return 403

    elif r.status_code == 404: #summoner name not found
        return 404

#return the json league(ranked) info of the user
def get_league(sum_ID, API_KEY):
    url = '{}/by-summoner/{}/entry?api_key={}'.format(LEAGUE_URL, sum_ID, API_KEY)
    r = requests.get(url)

    if r.status_code == 200:
        dataBag = r.json()
        data = dataBag[str(sum_ID)][0]
        return data

    elif r.status_code == 404:
        return 404

#returns the list of matches for specific season
def get_match_history(sum_ID, season, API_KEY):
    url = '{}/{}?seasons={}&api_key={}'.format(MATCH_HISTORY_URL, sum_ID, season, API_KEY)
    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()
        matches = data['matches'] #list of matches(json object)

        return matches

    elif r.status_code == 404:
        return 404

def get_match(API_KEY, match_ID):
    url = '{}/{}?api_key={}'.format(MATCH_URL, match_ID, API_KEY)
    print url
    print '\n\n\n'
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        return data
    elif r.status_code == 404:
        return 404

#returns the json formatted summary of the mastery pages.
def get_masteries(sum_ID, API_KEY):
    url = '{}/{}/masteries?api_key{}'.format(SUMMONER_URL, sum_ID, API_KEY)
    r = requests.get(url)

    return r.json()

#returns the list of json objects
def get_ranked_stats(sum_ID, season, API_KEY):
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

def get_aggregated_ranked_stats(sum_ID, season, API_KEY):
    url = '{}/{}/ranked?season={}&api_key={}'.format(STATS_URL, sum_ID, season ,API_KEY)
    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()
        rankedChampions = data['champions']#list of json objects

        rankedChampions.sort(key=lambda x: x['id'])
        return rankedChampions[0]

    elif r.status_code == 404: #ranked stats not found
        return 404

#Returns the list of json info of the current game that the user is in
def get_current_match(sum_ID, API_KEY):
    url = '{}/{}?api_key={}'.format(CURRENT_MATCH, sum_ID, API_KEY)
    r = requests.get(url)

    blueTeam, redTeam = [], []

    if r.status_code == 200:
        data = r.json()
        players = data['participants'] #gets the list of json objects of the players

        for player in players:
            if player['teamId'] == 100: #blueTeam
                blueTeam.append(player)
            else: #redTeam
                redTeam.append(player)

        return [blueTeam, redTeam]

    elif r.status_code == 404: #not in game
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
        data = r.json() #list of json objects
        return data['data']

    elif r.status_code == 404:
        return 404

#functions for pick/ban/win rate
def get_highest_winrate_champs(API_KEY, limit):
    url = "{}/champs/mostWinning?api_key={}&page=1&limit={}".format(CHAMPIONGG, API_KEY, limit)

   # url = 'http://api.champion.gg/stats/champs/mostWinning?api_key=e0430f17c1fc4b8be9747087bde46f41&page=1&limit=2'
    r = requests.get(url)
    print r

    if r.status_code == 200:
        data = r.json() #returns dicgtionary
        return data['data']

    elif r.status_code == 404:
        return 404

def get_mostbanned_champs(API_KEY, limit):
    url = "{}/champs/mostBanned?api_key={}&page=1&limit={}".format(CHAMPIONGG, API_KEY, limit)
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        return data['data']
    elif r.status_code == 404:
        return 404

def get_general_champ_data(API_KEY, champName):
    url = "http://api.champion.gg/champion/{}/general?api_key={}".format(champName, API_KEY)
    r = requests.get(url)

    if r.status_code == 200:
        return r.json()

def get_champ_list(API_KEY):
    url = "http://api.champion.gg/champion?api_key={}".format(API_KEY)
    r = requests.get(url)
    if r.status_code == 200:
        data=r.json()
        return data
    elif r.status_code == 404:
        return 404

def get_champ(API_KEY):
    url = "http://api.champion/{}?api_key={}".format(champion,API_KEY)
    r = requests.get(url)
    if r.status_code == 200:
        data=r.json()
        return data
    elif r.status_code == 404:
        return 404

def get_champ_build(champion, API_KEY):
    url = "http://api.champion.gg/champion/{}/items".format(champion) + \
        "/finished/mostPopular?api_key={}".format(API_KEY)
    print url
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        data = data[0]['items']
        return data
    elif r.status_code == 404:
        return 404

def tier_to_number(tier, division):
    num = 0

    if (tier == 'SILVER'):
        num = num + 5
    elif (tier == 'GOLD'):
        num = num + 10
    elif (tier == 'PLATINUM'):
        num = num + 15
    elif (tier == 'DIAMOND'):
        num = num + 20
    elif (tier == 'MASTER'):
        num = num + 21
        return num
    elif (tier == 'CHALLENGER'):
        num = num + 22
        return num

    return num + (5 - division)

def get_numbered_rank_from_sum_ID(summoner_ID, API_KEY):
    sum_league = get_league(summoner_ID, API_KEY)
    tier = sum_league['tier']
    division = roman_to_integer(sum_league['entries'][0]['division'])
    return tier_to_number(tier, division)

def get_summoner_ID_from_name(summoner_name, API_KEY):
    sum_DTO = get_sum_DTO(summoner_name, API_KEY)
    sum_id = sum_DTO[summoner_name.lower().replace(" ", "")]['id']
    return sum_id
