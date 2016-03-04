from flask import Blueprint, render_template, redirect, url_for
from flask import request, make_response
from flask import current_app

import requests


signup = Blueprint('signup', __name__)

@signup.route('/signup')
def sign_up():
    return "Hello SignUp"