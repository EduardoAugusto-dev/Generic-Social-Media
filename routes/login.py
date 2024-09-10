from flask import Blueprint, render_template, request, redirect, url_for
from database.models.user_and_posts import Posts, User

login_route = Blueprint ('login', __name__)

@login_route.route('/create', methods = ['POST'])
def create_account():
    pass

@login_route.route('/login_account', methods = ['POST'])
def login_user():
    pass