from flask import Blueprint, render_template
from flask import request
from flask import current_app
from app.mod_riot import functions as f
import requests

challenger = Blueprint('challenger', __name__)

@challenger.route('/challenger')
def roster():
    pass

