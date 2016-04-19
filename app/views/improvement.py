from app import db
from app.mod_riot import functions as f
from app.models import Snapshot
from flask import Blueprint, current_app, g, render_template

import datetime

improvement = Blueprint('improvement', __name__)

@improvement.route('/improvement')
def show_improve():
    RIOT_API_KEY = current_app.config.get('RIOT_API_KEY')
    sum_id = f.get_summoner_ID_from_name('KarmicDemon', RIOT_API_KEY)
    new_rank = f.get_numbered_rank_from_sum_ID(sum_id, RIOT_API_KEY)
    new_d = datetime.datetime.today()

    changes = Snapshot.query.filter(Snapshot.user_id == g.user.id).all()

    if not changes:
        s = Snapshot(user_id = g.user.id,
                        snap_time = new_d,
                        division = new_rank)
        db.session.add(s)
        db.session.commit(s)
        return render_template('improvement/first_time.html')

    time_to_compare  = changes[-1].snap_time

    if (new_d.date() != time_to_compare.date()):
        s = Snapshot(user_id = g.user.id,
                        snap_time = new_d,
                        division = new_rank)
        changes.append(s)
        db.session.add(s)
        db.session.commit(s)

    return render_template('improvement/improvement.html', title='Improvement',
        changes=changes)
