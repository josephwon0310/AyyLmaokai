from app.mod_riot.functions import get_champ_build
from flask import Blueprint, current_app, redirect, render_template, request

discuss = Blueprint('discuss', __name__)

@discuss.route('/discuss')
def discuss_route():
    champ = request.args.get('champ', '')

    if (champ == ''):
        return redirect('/home')

    CHAMP_GG_API_KEY = current_app.config.get('CHAMPIONGG_API_KEY')
    data = get_champ_build(champ.replace(' ', ''), CHAMP_GG_API_KEY)

    print "This is data: "
    print data

    return data

    return render_template('discuss/discuss.html')
