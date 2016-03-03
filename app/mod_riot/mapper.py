'''
Maps the data fetched from Riot API to the static data in dragontail
'''

import json
import os
import requests

from pprint import pprint

REALM = 'http://ddragon.leagueoflegends.com/realms/na.json'
DRAGON_TAIL_CHAMPION = 'http://ddragon.leagueoflegends.com/cdn/6.4.2/data/en_US/champion.json'
CHAMPION_IMAGE = 'app/mod_riot/dragontail-6.4.1/6.4.1/img/champion/'

#returns the version of the Realm file
def check_datadragon_version(attribute):
    
    r = requests.get(REALM)
    data = r.json()
    data = data['n']
    
    return data[attribute]

def map_champions(id):
    
    r = requests.get(DRAGON_TAIL_CHAMPION)
    data = r.json()
    
    #Iterate through the champion json file
    for champion, value in data['data'].iteritems():
        #Searches for the key
        if int(value['key']) == id:
            return champion
            #TODO: currently only returns the name


#returns the file, not sure if it's the best practice
def get_splash_art(champion):
    #joseph will rewrite

def map_items(id):
    pass
