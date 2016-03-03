from flask import Blueprint, render_template
from flask import request
from flask import current_app
from app.mod_riot import functions as f
from string import whitespace
import requests

home = Blueprint('home', __name__)

@home.route('/')
def index():
    return render_template('home/home.html')

@home.route('/test')
def test():
    return "hello world"

@home.route('/', methods=['POST'])
def riot_request():

    API_KEY = current_app.config.get('RIOT_API_KEY') #api_key for riotgames
    
    summonerName = request.form['text']
    sumName = str(summonerName)
    sumName.replace(" ", "")#strip whitespace
    summonerDTO = f.get_sum_DTO(summonerName, API_KEY)
    summonerDTO = summonerDTO[sumName]
    
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