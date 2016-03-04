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
    return render_template('home/home.html')



#EXAMPLE OF HOW YOU WOULD RETURN IMAGE FROM REQUEST VIA FLASK
@home.route('/image')
def imagetest():

    #Currently harcoded to return Nami's image
    champion = "Nami.png"
    print request.form['summonerName']
    #this is the response object
    image = m.get_splash_art(champion)

    wah = make_response(image.content)
    wah.headers['Content-Type'] = 'image/png'

    return wah