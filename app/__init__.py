import os
from flask import Flask, render_template
from flask.ext import assets
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

#TODO: might have to change it to another type of cache, simple is not good
#cache = Cache(app,config={'CACHE_TYPE': 'simple'})

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
env = assets.Environment(app)
env.register('css_all',
    assets.Bundle('all.sass', filters='sass', output='css_all.css'))
env.url = app.static_url_path
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'

#Import the Blueprints
from .views.ban import ban
from .views.challenger import challenger
from .views.current_game import current_game
from .views.dynamic_queue import dynamic_queue
from .views.feedback import feedback
from .views.home import home
from .views.improvement import improvement
from .views.login import login
from .views.profile import profile
from .views.signup import signup
from .views.trending import trending

app.register_blueprint(ban)
app.register_blueprint(challenger)
app.register_blueprint(current_game)
app.register_blueprint(dynamic_queue)
app.register_blueprint(feedback)
app.register_blueprint(home)
app.register_blueprint(improvement)
app.register_blueprint(login)
app.register_blueprint(profile)
app.register_blueprint(signup)
app.register_blueprint(trending)
