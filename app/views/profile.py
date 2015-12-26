from flask import Blueprint, render_template

profile = Blueprint('profile', __name__)

@profile.route('/profile')
def dashboard():
    pass
    #return render_template('')