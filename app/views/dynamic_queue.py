from app import db, forms
from app.models import User
from flask import Blueprint, g, render_template
from flask.ext.login import login_required

dynamic_queue = Blueprint('dynamic_queue', __name__)

@dynamic_queue.route('/dynamic_queue', methods=['GET', 'POST'])
@login_required
def dynamic():
    user = g.user
    player_list = []

    form = forms.DynamicQueueOptions()

    if form.validate_on_submit():
        user.looking_for_lower = form.lower_than_me.data
        user.looking_for_equal = form.equal_to_me.data
        user.looking_for_greater = form.greater_than_me.data
        db.session.commit()

        #find people with similar elo
        if user.looking_for_lower:
            players = User.query.filter(User.rank < user.rank)\
                .filter(User.rank != "").all()
            player_list.extend(players)

        if user.looking_for_equal:
            players = User.query.filter(User.rank == user.rank)\
                .filter(User.rank != "").all()
            player_list.extend(players)

        if user.looking_for_greater:
            players = User.query.filter(User.rank > user.rank)\
                .filter(User.rank != "").all()
            player_list.append(players)

            #return list of people looking for him as well
        player_list = [x for x in player_list if x != []]
        print player_list

    return render_template('dynamic_queue/dynamic_queue.html',
        title='Dynamic Queue', form=form, player_list=player_list)
