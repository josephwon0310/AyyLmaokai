from flask import Blueprint, render_template, redirect, url_for
from flask import request, make_response
from flask import current_app

from app.mod_riot import functions as f
from app.mod_riot import mapper as m

import requests


home = Blueprint('home', __name__)

#@home.route('/', methods=['GET','POST'])
@home.route('/')
def index():
    # form = SummonerForm()
    # #print form.summonerName
    # if form.validate_on_submit():
    #     print "wtf"
    #     return form.summonerName
    # if request.method == 'POST':
    #     return redirect(url_for('profile.index'))

    return render_template('home/home.html')


#-=======TESTING
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


#EXAMPLE OF HOW YOU WOULD RETURN IMAGE FROM REQUEST VIA FLASK
@home.route('/image')
def imagetest():

    #Currently harcoded to return Nami's image
    champion = "Nami.png"

    #this is the response object
    image = m.get_splash_art(champion)

    wah = make_response(image.content)
    wah.headers['Content-Type'] = 'image/png'

    return wah

#======TESTING

@home.route('/', methods=['POST'])
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

    return render_template('home/test.html', rankedDTO=rankedDTO
                                           , summonerId=summonerId
                                           , level=level)
    #return redirect(url_for('profile.index'))
