from app.mod_riot import functions as f
from flask import Blueprint, current_app, render_template, request
import requests

challenger = Blueprint('challenger', __name__)

@challenger.route('/challenger')
def roster():
    pass
