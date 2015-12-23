#Import flask & template operators
from flask import Flask, render_template

#Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

#Define the WSGI application object
app = Flask(__name__)

#Import the config.py
app.config.from_object('config')

#Database
#TODO

@app.route('/')
def index():
    return render_template('index.html')