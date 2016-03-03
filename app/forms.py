
from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class SummonerForm(Form):
    summonerName = StringField('summonerName', validators=[DataRequired()])