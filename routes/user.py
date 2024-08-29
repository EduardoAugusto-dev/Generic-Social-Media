from flask import Blueprint, render_template, request
from database.models.user_and_posts import User

user_route = Blueprint('user', __name__)

@user_route.route('/user')
def post_list():
    """This function list every posts"""
    users = User.select()
    return render_template('user.html', users = users)