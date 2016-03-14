'''
This file initializes your application and brings together all of the various components.
'''
#Import flask & template operators
from flask import Flask, render_template

#from flask.ext.cache import Cache
#Define the WSGI application object
app = Flask(__name__, instance_relative_config=True)

#Define the Cache object for Flask
#TODO: might have to change it to another type of cache, simple is not good
#cache = Cache(app,config={'CACHE_TYPE': 'simple'})

#Import the configurations
app.config.from_object('config')

#Import the config file in the instance folder
'''
This instance folder will not be committed to github, so I will have to send you guys the keys separately.
Not a very important issue right now, will figure it out later.
'''
app.config.from_pyfile('config.py')

from app import views
#Database
#TODO

#set up sass compiler
import os
from flask.ext import assets
env = assets.Environment(app)
env.url = app.static_url_path

env.register(
    'css_all',
    assets.Bundle(
        'all.sass',
        filters='sass',
        output='css_all.css'
    )
)


#Import the Blueprints
from .views.profile import profile
from .views.home import home
from .views.trending import trending
from .views.ban import ban
from .views.signup import signup
#from .views.register import register
from .views.feedback import feedback

app.register_blueprint(profile)
app.register_blueprint(home)
app.register_blueprint(trending)
app.register_blueprint(ban)
app.register_blueprint(signup)
#app.register_blueprint(register)
app.register_blueprint(feedback)
