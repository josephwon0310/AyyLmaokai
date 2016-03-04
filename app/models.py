'''
This is where you define the models of your application. This may be split into several modules in the same way as views.py.
'''

from __future__ import division

#Champion object generated from Champion.gg json objects
from sqlalchemy import Column, Integer, String
from app.database import Base

class Champion:
    def __init__(self, obj):
        self.name = obj['name']
        self.win_percent = obj['general']['winPercent']
        self.play_percent = obj['general']['playPercent']
        self.ban_rate = obj['general']['banRate']
        self.kills = obj['general']['kills']
        self.deaths = obj['general']['deaths']
        self.assists = obj['general']['assists']
        self.image = 'images/champion/' + obj['key'] + '.png'

    def __repr__(self):
        return "Champion: " + self.name + "\n" + "Kills: " + str(self.kills)

    def get_kda(self):
        return (self.kills+self.assists) / self.assists


#Ranked stat data object for each champions
class ChampStat:

    def __init__(self, obj):
        self.name = obj['id']
        self.totalKills = obj['stats']['totalChampionKills']
        self.totalDeaths = obj['stats']['totalDeathsPerSession']
        self.totalAssists = obj['stats']['totalAssists']
        self.gamesPlayed = obj['stats']['totalSessionsPlayed']
        self.wins = obj['stats']['totalSessionsWon']
        self.totalFirstBlood = obj['stats']['totalFirstBlood']
        self.creepScore = obj['stats']['totalMinionKills']
        self.totalGold = obj['stats']['totalGoldEarned']
        self.image = 'images/champion/' + str(self.name) + '.png'

    #Includes rounding up to reasonable digit for each attributes
    def get_kda(self):
        if self.totalDeaths == 0:
            return "Perfect"
        else:
            kda = ((self.totalKills + self.totalAssists)/self.totalDeaths)
        return round(kda, 2)

    def get_cs(self):
        cs = self.creepScore / self.gamesPlayed
        return round(cs, 2)

    def get_winrate(self):
        winrate = self.wins * 100 / self.gamesPlayed
        return round(winrate, 1)

    def get_gold(self):
        return self.totalGold / self.gamesPlayed


#Data object for matches
class Match:

    def __init__(self, obj):
        self.season = obj['season']
        self.matchId = obj['matchId']
        self.role = obj['role']
        self.lane = obj['lane']
        self.champion = obj['champion']
        self.timestamp = obj['timestamp']




class Summoner:

    def __init__(self, obj):
        self.name = obj['name']
        self.id = obj['id']
        self.profileIconId = obj['profileIconId']
        self.profileIcon = 'images/profileicon/' + str(self.profileIconId) +'.png'
        self.revisionDate = obj['revisionDate']
        self.level = obj['summonerLevel']
        self.league = None
        self.medalImage = None
