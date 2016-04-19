from flask import Blueprint, render_template

improvement = Blueprint('improvement', __name__)

@improvement.route('/improvement')
def show_improve():
    #get change data from Database make model

    #store a new change data to user everytime they get on this page

    #return data to frontend

    #extra variables
    return render_template('improvement/improvement.html', title='Improvement')
