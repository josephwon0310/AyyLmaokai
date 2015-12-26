from flask import Blueprint, render_template
from flask import request
from flask import current_app
import requests

home = Blueprint('home', __name__)
request_handle = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name'


@home.route('/')
def index():
    return render_template('home/layout.html')

@home.route('/', methods=['POST'])
def riot_request():

    summoner_name = request.form['text']
    #This gets the summoner object that contains mapped values of summoner 
    r = requests.get('{}/{}?api_key={}'.format(request_handle, summoner_name, current_app.config.get('RIOT_API_KEY')))
    
    return r.text