from flask.ext.wtf import Form
from wtforms import BooleanField, PasswordField, StringField
from wtforms import TextAreaField, TextField, validators
from wtforms.validators import DataRequired, EqualTo, Required

class CommentForm(Form):
    comment = TextAreaField('comment', validators=[DataRequired()])

class DynamicQueueOptions(Form):
    lower_than_me = BooleanField('less_than_me', default=False)
    equal_to_me = BooleanField('equal_to_me', default=True)
    greater_than_me = BooleanField('greater_than_me', default=True)

class GameBans(Form):
	ban1 = StringField('ban1', validators=[DataRequired()])
	ban2 = StringField('ban2', validators=[DataRequired()])
	ban3 = StringField('ban3', validators=[DataRequired()])
	ban4 = StringField('ban4', validators=[DataRequired()])
	ban5 = StringField('ban5', validators=[DataRequired()])
	ban6 = StringField('ban6', validators=[DataRequired()])

class LoginForm(Form):
	email = StringField('Email', [Required()])
	password = PasswordField('Password', [Required()])

class SignUpForm(Form):
    email = StringField('Email', [Required()])
    summoner_name = StringField('Summoner Name', [Required()])
    password = PasswordField('Password', [Required()])
    confirm = PasswordField('Confirm Password', [Required()])

class SummonerForm(Form):
    summonerName = StringField('summonerName', validators=[DataRequired()])
