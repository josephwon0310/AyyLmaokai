'''
Maps the data fetched from Riot API to the static data in dragontail
'''

import json
import os

from pprint import pprint

DRAGON_TAIL = 'app/mod_riot/dragontail-6.4.2/6.4.2/data/en_US/'
print os.getcwd()
def map_champions(id):
    
    with open(DRAGON_TAIL+'champion.json') as datafile:
        data = json.load(datafile)
        
        #Iterate through the champion json file
        for champion, value in data['data'].iteritems():
            #Searches for the key
            if int(value['key']) == id:
                return champion
                #TODO: currently only returns the name
        
    
def map_items(id):
    pass


id = 40

print map_champions(id)
