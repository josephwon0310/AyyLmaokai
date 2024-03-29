'''
Maps the data fetched from Riot API to the static data in dragontail
'''

import json
import os
import requests, shutil

from pprint import pprint

DRAGON_TAIL = 'app/mod_riot/dragontail-6.4.2/6.4.2/data/en_US/'
print os.getcwd()
REALM = 'http://ddragon.leagueoflegends.com/realms/na.json'
DRAGON_TAIL_CHAMPION = 'http://ddragon.leagueoflegends.com/cdn/{}/data/en_US/champion.json'
CHAMPION_IMAGE = 'http://ddragon.leagueoflegends.com/cdn/{}/img/champion/{}'

#returns the version of the Realm file
def check_datadragon_version():
    
    r = requests.get(REALM)
    data = r.json()
    version = data['v']
    
    if r.status_code == 200:
        return version
        
    else:
        return "SOMETHING IS WITH DATA REALM!"


#maps the champion id to its name
def map_champions(id):
    
    version = check_datadragon_version()
    url = DRAGON_TAIL_CHAMPION.format(version)
    
    r = requests.get(url)
    data = r.json()
    
    #Iterate through the champion json file
    for champion, value in data['data'].iteritems():
        #Searches for the key
        if int(value['key']) == id:
            return champion
            #TODO: currently only returns the name

#maps roman to integer
def roman_to_integer(char):
    
    if char == 'V':
        return 5
    elif char == 'IV':
        return 4
    elif char == 'III':
        return 3
    elif char == 'II':
        return 2
    elif char == 'I':
        return 1


#returns the response object of the image
def get_splash_art(champion):
    #joseph will rewrite
    pass
    
    version = check_datadragon_version()
    url = CHAMPION_IMAGE.format(version, champion)
    #url = 'http://ddragon.leagueoflegends.com/cdn/6.4.2/img/champion/Aatrox.png'
    r = requests.get(url, stream=True)
    
    if r.status_code == 200:
        return r
    else:
        return "RIP"
        
def map_items(id):
    pass