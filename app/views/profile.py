from flask import Blueprint, render_template
from flask import request, current_app
import requests

profile = Blueprint('profile', __name__)

@profile.route('/summonerName')
def index():

    return 'rofl'