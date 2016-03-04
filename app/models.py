'''
This is where you define the models of your application. This may be split into several modules in the same way as views.py.
'''
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
