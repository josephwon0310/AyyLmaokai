'''
This file initializes your application and brings together all of the various components.
'''
#Import flask & template operators
from flask import Flask, render_template

#Define the WSGI application object
app = Flask(__name__, instance_relative_config=True)

#Import the configurations
app.config.from_object('config')

#Import the config file in the instance folder
'''
This instance folder will not be committed to github, so I will have to send you guys the keys separately.
Not a very important issue right now, will figure it out later.
'''
app.config.from_pyfile('config.py')

#Database
#TODO


#Import the Blueprints
from .views.profile import profile
from .views.home import home


app.register_blueprint(profile)
app.register_blueprint(home)