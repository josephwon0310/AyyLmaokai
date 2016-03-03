from flask import Blueprint, render_template, redirect, url_for
from flask import request
from flask import current_app
from app.mod_riot import functions as f
import requests
from app.forms import *

home = Blueprint('home', __name__)

@home.route('/', methods=['GET','POST'])
def index():
    # form = SummonerForm()
    # #print form.summonerName
    # if form.validate_on_submit():
    #     print "wtf"
    #     return form.summonerName
    if request.method == 'POST':
        return redirect(url_for('profile.index'))
    
    return render_template('home/home.html')


##Example code on how to use ChampionGG data
@home.route('/testChamp')
def test():
    
    API_KEY = current_app.config.get('CHAMPIONGG_API_KEY')
    
    data = f.get_champion_data('singed', API_KEY)
   
   #Example
    winPercent = data[0]['general']
    banRate = data[0]['banRate']
    cs = data[0]['minionsKilled']
    
    return render_template('fck.html', winPercent=winPercent)

@home.route('/result', methods=['GET','POST'])
def riot_request():

    API_KEY = current_app.config.get('RIOT_API_KEY') #api_key for riotgames
    
    summonerName = request.form['text']
    summonerName = summonerName.replace(" ", "") #strip all the whitespaces
    summonerDTO = f.get_sum_DTO(summonerName, API_KEY)
    summonerDTO = summonerDTO[summonerName]
    
    #retrieve individual values from summonerDTO
    summonerId = summonerDTO['id']
    summonerIcon = summonerDTO['profileIconId']
    level = summonerDTO['summonerLevel']
    revisionDate = summonerDTO['revisionDate']
    
    #retrieve ranked stats
    rankedDTO = f.get_ranked_stats(summonerId, 'SEASON2016', API_KEY)
    
    # return render_template('home/test.html', rankedDTO=rankedDTO
    #                                        , summonerId=summonerId
    #                                        , level=level)
    return redirect(url_for('profile.index'))