'''
Maps the data fetched from Riot API to the static data in dragontail
'''

import json
import os

from pprint import pprint

DRAGON_TAIL = 'app/mod_riot/dragontail-6.4.1/6.4.1/data/en_US/'
CHAMPION_IMAGE = 'app/mod_riot/dragontail-6.4.1/6.4.1/img/champion/'

def map_champions(id):
    
    with open(DRAGON_TAIL+'champion.json') as datafile:
        data = json.load(datafile)
        
        #Iterate through the champion json file
        for champion, value in data['data'].iteritems():
            #Searches for the key
            if int(value['key']) == id:
                return champion
                #TODO: currently only returns the name


#returns the file, not sure if it's the best practice
def get_splash_art(champion):
    
    for image in os.listdir(CHAMPION_IMAGE):
        fileName = champion + ".png"
        if image == fileName:
            with open(CHAMPION_IMAGE+fileName, 'r') as f:
                return f
                
    
def map_items(id):
    pass