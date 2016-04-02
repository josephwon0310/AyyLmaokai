import os


#Import flask & template operators
from flask import Flask, render_template
from flask.ext import assets
from flask.ext.login import LoginManager
from flask.ext.openid import OpenId
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)

from app import views

#TODO: might have to change it to another type of cache, simple is not good
#cache = Cache(app,config={'CACHE_TYPE': 'simple'})

#Import the configurations
app.config.from_object('config')
#Import the config file in the instance folder
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
env = assets.Environment(app)
env.register('css_all',
    assets.Bundle('all.sass', filters='sass', output='css_all.css')
)
env.url = app.static_url_path
login_manager = LoginManager()
login_manager.init_app(app)
oid = OpenId(app, os.path.join(basedir, 'tmp'))

#Import the Blueprints
from .views.profile import profile
from .views.home import home
from .views.trending import trending
from .views.ban import ban
from .views.signup import signup
from .views.feedback import feedback
from .views.dynamic_queue import dynamic_queue
from .views.login import login

app.register_blueprint(profile)
app.register_blueprint(home)
app.register_blueprint(trending)
app.register_blueprint(ban)
app.register_blueprint(signup)
app.register_blueprint(feedback)
app.register_blueprint(dynamic_queue)
app.register_blueprint(login)
