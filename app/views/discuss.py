from app import db
from app.mod_riot.functions import get_champ_build, get_item
from app.models import Comment
from app.forms import CommentForm
from flask import Blueprint, current_app, g, redirect, render_template, request

discuss = Blueprint('discuss', __name__)

@discuss.route('/discuss', methods=['GET', 'POST'])
def discuss_route():
    champ = request.args.get('champ', '')

    form = CommentForm()

    if (champ == ''):
        return redirect('/home')

    CHAMP_GG_API_KEY = current_app.config.get('CHAMPIONGG_API_KEY')
    RIOT_API_KEY = current_app.config.get('RIOT_API_KEY')

    data = get_champ_build(champ.replace(' ', ''), CHAMP_GG_API_KEY)

    champion = {}

    champion['name'] = champ
    champion['image'] = "images/champion/" + champ.replace(" ", "") + ".png"
    champion['items'] = [get_item(x, RIOT_API_KEY) for x in data]

    comments = Comment.query.filter(Comment.champion == champion['name'])all()

    #do if form validate on submit
    if request.method == 'POST':
        _user = ""

        if (not hasattr(g.user, "id")):
            _user = "Anonymous"
        else:
            _user = g.user.league_name

        _comment = form.comment.data
        c = Comment(user=_user, champion=champion['name'], comment=_comment)

        db.session.add(c)
        db.session.commit()

        comments = Comment.query.filter(Comment.champion
            == champion['name']).all()

        print comments

        return render_template('discuss/discuss.html', champ=champion,
            form=form, comments=comments)

    return render_template('discuss/discuss.html', champ=champion, form=form,
        comments=comments)
