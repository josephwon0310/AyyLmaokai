from app.mod_riot import functions as f, mapper as m
from flask import Blueprint, current_app, g, make_response, redirect
from flask import render_template, request, make_response, url_for
import requests

home = Blueprint('home', __name__)

@home.route('/')
def index():
    user = g.user
    return render_template('/home/home.html', title='Home', user=user)

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
