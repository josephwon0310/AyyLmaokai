from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class SummonerForm(Form):
    summonerName = StringField('summonerName', validators=[DataRequired()])

class GameBans(Form):
	ban1 = StringField('ban1', validators=[DataRequired()])
	ban2 = StringField('ban2', validators=[DataRequired()])
	ban3 = StringField('ban3', validators=[DataRequired()])
	ban4 = StringField('ban4', validators=[DataRequired()])
	ban5 = StringField('ban5', validators=[DataRequired()])
	ban6 = StringField('ban6', validators=[DataRequired()])
	