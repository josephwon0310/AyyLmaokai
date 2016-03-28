from flask import Blueprint, render_template

dynamic_queue = Blueprint('dynamic_queue', __name__)

@dynamic_queue.route('/dynamic_queue')
def dynamic():
    #get user id from session

    #find people with similar elo

    #return list of people looking for him as well
    return "hi"
